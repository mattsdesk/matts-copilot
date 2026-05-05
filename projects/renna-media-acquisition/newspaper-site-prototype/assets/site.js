(function () {
  const data = window.NEWSPAPER_DATA;
  const articles = data.articles;

  function articleUrl(article) {
    return `article.html?slug=${encodeURIComponent(article.slug)}`;
  }

  function imageBlock(article, className = "story-image") {
    return `<div class="${className} tone-${article.imageTone}" role="img" aria-label="${article.imageLabel}"><span>${article.imageLabel}</span></div>`;
  }

  function card(article) {
    return `
      <article class="story-card">
        <a href="${articleUrl(article)}">${imageBlock(article)}</a>
        <h3><a href="${articleUrl(article)}">${article.title}</a></h3>
        <p>${article.dek}</p>
      </article>
    `;
  }

  function latestItem(article) {
    return `
      <article class="latest-item">
        <h3><a href="${articleUrl(article)}">${article.title}</a></h3>
      </article>
    `;
  }

  function renderHome() {
    const lead = articles[0];
    const leadMount = document.querySelector("[data-home-lead]");
    if (leadMount) {
      leadMount.innerHTML = `
        <a href="${articleUrl(lead)}">${imageBlock(lead, "lead-image")}</a>
        <h1><a href="${articleUrl(lead)}">${lead.title}</a></h1>
        <p class="lead-dek">${lead.dek}</p>
        <div class="meta">${lead.byline} · ${lead.date}</div>
      `;
    }

    const latestMount = document.querySelector("[data-latest-list]");
    if (latestMount) {
      latestMount.innerHTML = articles.slice(1, 5).map(latestItem).join("");
    }

    const allStoriesMount = document.querySelector("[data-all-stories]");
    if (allStoriesMount) {
      allStoriesMount.innerHTML = articles.slice(1).map(card).join("");
    }

    const eventsMount = document.querySelector("[data-events-list]");
    if (eventsMount) {
      eventsMount.innerHTML = data.events.map((event) => `
        <article class="event-card">
          <time>${event.date}</time>
          <h3>${event.title}</h3>
          <p>${event.location}</p>
        </article>
      `).join("");
    }
  }

  function renderBodyBlock(block) {
    if (typeof block === "string") {
      return `<p>${block}</p>`;
    }

    if (block.type === "list") {
      return `
        <section class="article-callout">
          <h2>${block.heading}</h2>
          <ul>${block.items.map((item) => `<li>${item}</li>`).join("")}</ul>
        </section>
      `;
    }

    if (block.type === "details") {
      return `
        <section class="article-info">
          <h2>${block.heading}</h2>
          <ul>${block.items.map((item) => `<li>${item}</li>`).join("")}</ul>
        </section>
      `;
    }

    return "";
  }

  function renderArticle() {
    const params = new URLSearchParams(window.location.search);
    const slug = params.get("slug") || articles[0].slug;
    const article = articles.find((item) => item.slug === slug) || articles[0];
    const mount = document.querySelector("[data-article-detail]");
    document.title = `${article.title} | ${data.publication.name}`;

    if (mount) {
      mount.innerHTML = `
        <h1>${article.title}</h1>
        <p class="article-dek">${article.dek}</p>
        <div class="meta">${article.byline} · ${article.date}</div>
        ${imageBlock(article, "article-hero-image")}
        <div class="inline-ad">
          <span>Inline Ad</span>
          <strong>728 x 90 or responsive native unit</strong>
        </div>
        <div class="article-body">
          ${article.body.map(renderBodyBlock).join("")}
        </div>
      `;
    }

    const relatedMount = document.querySelector("[data-related-list]");
    if (relatedMount) {
      relatedMount.innerHTML = articles
        .filter((item) => item.slug !== article.slug)
        .slice(0, 4)
        .map(latestItem)
        .join("");
    }
  }

  if (document.body.dataset.page === "home") {
    renderHome();
  }

  if (document.body.dataset.page === "article") {
    renderArticle();
  }
}());
