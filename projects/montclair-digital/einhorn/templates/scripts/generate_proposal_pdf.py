"""
Einhorn Proposal PDF Generator
Usage: Called by Claude after populating proposal content.

Pass a ProposalData object to generate_pdf() to produce a clean, professional PDF.
Output is saved to /sessions/focused-lucid-bell/mnt/einhorn/proposals/

Install deps if needed:
  pip install reportlab --break-system-packages
"""

import os
from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER


# ── Colors ─────────────────────────────────────────────────────────────────
BODY_COLOR   = HexColor("#1a1a1a")
HEADER_COLOR = HexColor("#000000")
RULE_COLOR   = HexColor("#cccccc")
LIGHT_RULE   = HexColor("#e8e8e8")


# ── Data model ─────────────────────────────────────────────────────────────
@dataclass
class ProposalSection:
    title: str
    content: str  # Plain text or simple markdown-like text


@dataclass
class ProposalData:
    service_slug: str           # e.g. "criminal-seo" → used in filename
    sections: list[ProposalSection]
    media_budget: Optional[str] = None   # e.g. "$5,000"
    management_fee: Optional[str] = None # e.g. "$2,000"
    term_length: Optional[str] = None    # e.g. "3 months"
    launch_days: Optional[str] = None    # e.g. "14"
    proposal_date: Optional[str] = None  # Override date string (MM/DD/YYYY)


# ── Style helpers ───────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    styles = {}

    styles["title"] = ParagraphStyle(
        "ProposalTitle",
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=HEADER_COLOR,
        spaceAfter=2,
    )
    styles["subtitle"] = ParagraphStyle(
        "ProposalSubtitle",
        fontName="Helvetica",
        fontSize=11,
        leading=14,
        textColor=BODY_COLOR,
        spaceAfter=4,
    )
    styles["section_heading"] = ParagraphStyle(
        "SectionHeading",
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=16,
        textColor=HEADER_COLOR,
        spaceBefore=18,
        spaceAfter=4,
    )
    styles["subheading"] = ParagraphStyle(
        "SubHeading",
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=14,
        textColor=BODY_COLOR,
        spaceBefore=10,
        spaceAfter=2,
    )
    styles["body"] = ParagraphStyle(
        "ProposalBody",
        fontName="Helvetica",
        fontSize=10,
        leading=15,
        textColor=BODY_COLOR,
        spaceAfter=6,
    )
    styles["bullet"] = ParagraphStyle(
        "ProposalBullet",
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=BODY_COLOR,
        leftIndent=14,
        spaceAfter=3,
        bulletIndent=0,
    )
    styles["signature_label"] = ParagraphStyle(
        "SignatureLabel",
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=BODY_COLOR,
        spaceAfter=20,
    )
    styles["footer"] = ParagraphStyle(
        "Footer",
        fontName="Helvetica",
        fontSize=8,
        leading=10,
        textColor=HexColor("#888888"),
        alignment=TA_CENTER,
    )
    styles["prepared_by"] = ParagraphStyle(
        "PreparedBy",
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=HexColor("#666666"),
        spaceBefore=6,
    )

    return styles


# ── Content parser ──────────────────────────────────────────────────────────
def parse_content(text: str, styles: dict) -> list:
    """
    Parses plain-text proposal content into reportlab flowables.
    Supports:
      - Lines starting with "- " or "• " → bullet points
      - Lines starting with "**text**" → subheading
      - Blank lines → small spacers
      - Everything else → body paragraph
    """
    flowables = []
    lines = text.strip().split("\n")

    for line in lines:
        stripped = line.strip()

        if not stripped:
            flowables.append(Spacer(1, 4))
            continue

        if stripped.startswith("- ") or stripped.startswith("• "):
            content = stripped[2:].strip()
            flowables.append(Paragraph(f"• &nbsp; {content}", styles["bullet"]))
            continue

        if stripped.startswith("**") and stripped.endswith("**"):
            content = stripped[2:-2]
            flowables.append(Paragraph(content, styles["subheading"]))
            continue

        flowables.append(Paragraph(stripped, styles["body"]))

    return flowables


# ── Page numbering ──────────────────────────────────────────────────────────
class PageNumCanvas:
    """Adds 'Page X of Y' to bottom center of every page."""

    def __init__(self, canvas, doc):
        self._saved_page_states = []
        self.__dict__.update(canvas=canvas, doc=doc)
        canvas._saved_page_states = self._saved_page_states
        canvas.afterPage = self.afterPage
        canvas.save = self.save

    def afterPage(self):
        self._saved_page_states.append(dict(self.canvas.__dict__))
        self.canvas._startPage()

    def drawPageNumber(self, page_count, state):
        self.canvas.__dict__.update(state)
        self.canvas.setFont("Helvetica", 8)
        self.canvas.setFillColor(HexColor("#888888"))
        self.canvas.drawCentredString(
            letter[0] / 2,
            0.5 * inch,
            f"Page {self.canvas._pageNumber} of {page_count}"
        )
        self.canvas.restoreState()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.drawPageNumber(num_pages, state)
        self.canvas._doc.multiBuild


# ── Main generator ──────────────────────────────────────────────────────────
def generate_pdf(data: ProposalData, output_dir: str = None) -> str:
    """
    Generate the proposal PDF and return the file path.
    """
    if output_dir is None:
        output_dir = "/sessions/focused-lucid-bell/mnt/einhorn/proposals"

    os.makedirs(output_dir, exist_ok=True)

    proposal_date = data.proposal_date or date.today().strftime("%m/%d/%Y")
    date_slug = date.today().strftime("%Y-%m-%d")
    filename = f"einhorn-proposal-{data.service_slug}-{date_slug}.pdf"
    filepath = os.path.join(output_dir, filename)

    styles = build_styles()

    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
    )

    story = []

    # ── Header block ────────────────────────────────────────────────────────
    header_data = [
        [
            Paragraph("Proposal", styles["title"]),
            Paragraph(proposal_date, ParagraphStyle(
                "DateRight",
                fontName="Helvetica",
                fontSize=10,
                textColor=HexColor("#666666"),
                alignment=TA_RIGHT,
            )),
        ],
    ]
    header_table = Table(
        header_data,
        colWidths=[4.5 * inch, 2 * inch],
        style=TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]),
    )
    story.append(header_table)
    story.append(Paragraph("Prepared for Einhorn", styles["subtitle"]))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=black, spaceAfter=18))

    # ── Sections ─────────────────────────────────────────────────────────────
    for i, section in enumerate(data.sections):
        section_elements = []

        # Section header + rule
        section_elements.append(Paragraph(section.title, styles["section_heading"]))
        section_elements.append(HRFlowable(
            width="100%", thickness=0.5, color=RULE_COLOR, spaceAfter=8
        ))

        # Section content
        section_elements.extend(parse_content(section.content, styles))
        section_elements.append(Spacer(1, 6))

        story.append(KeepTogether(section_elements[:4]))  # Keep heading with first content
        story.extend(section_elements[4:])

    # ── Signature block ───────────────────────────────────────────────────────
    story.append(Spacer(1, 24))
    story.append(HRFlowable(width="100%", thickness=0.5, color=RULE_COLOR, spaceAfter=18))
    story.append(Paragraph("Approved by: ___________________________", styles["signature_label"]))
    story.append(Paragraph("Date: ___________________________", styles["signature_label"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Prepared by Matt Saunders", styles["prepared_by"]))

    # ── Build ─────────────────────────────────────────────────────────────────
    def add_page_number(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(HexColor("#888888"))
        canvas.drawCentredString(letter[0] / 2, 0.5 * inch, f"Page {doc.page}")
        canvas.restoreState()

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)

    return filepath


# ── CLI convenience ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Example usage — replace with actual content when calling from Claude
    example = ProposalData(
        service_slug="example",
        sections=[
            ProposalSection(
                title="1. Overview",
                content="This is a test proposal overview paragraph.\n\nSecond paragraph here."
            ),
            ProposalSection(
                title="2. Scope of Work",
                content="**Included:**\n- Item one\n- Item two\n\n**Not Included:**\n- Website development"
            ),
        ],
        media_budget="$5,000",
        management_fee="$2,000",
        term_length="3 months",
    )
    path = generate_pdf(example)
    print(f"PDF saved to: {path}")
