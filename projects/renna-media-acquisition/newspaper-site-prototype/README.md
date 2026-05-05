# Newspaper Site Prototype

Static May 2026 newspaper site for `Life in Roseland NJ`, built so future editions can be updated by replacing structured article data.

## Files

- `index.html` - homepage layout with section blocks and ad placements
- `article.html` - reusable article detail template
- `advertise.html` - editable advertising rates and circulation page
- `assets/site-data.js` - publication, article, and event content
- `assets/site.js` - renders homepage and article pages from the data file
- `assets/styles.css` - masthead, newspaper layout, responsive styles, and ad slot styling

## How to Use

Open `index.html` in a browser.

Article pages use the same template:

- `article.html?slug=2026-easter-egg-stravaganza`
- `article.html?slug=opera-at-florham-international-competition`
- `article.html?slug=roseland-library-may-programs-and-events`
- `article.html?slug=sanaaya-yogesh-wins-soccer-honors`

## Replacing Article Text

Edit `assets/site-data.js`.

Each article needs:

- `slug`
- `section`
- `title`
- `dek`
- `byline`
- `date`
- `imageLabel`
- `imageTone`
- `body`

## Ad Placements Included

- Homepage leaderboard
- Homepage sidebar box
- Homepage section banner
- Homepage half-page rail
- Article leaderboard
- Article sidebar box
- Article sidebar half-page
- In-article native unit
