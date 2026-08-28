# Mira Wilden Website

Offizielle statische Website für https://mirawilden.de/

## Deployment
- Quellcode: GitHub
- Production branch: `main`
- Deployment: GitHub Actions über Cloudflare Wrangler
- Statische Website-Dateien: `public/`
- Cloudflare Worker: `website`

Jeder Push auf `main` löst den Deployment-Workflow unter `.github/workflows/` aus.

## Struktur
- `public/index.html` – Startseite
- `public/buecher/` – Bücherübersicht
- `public/ironwood-falls/` – Reihe und Buchseiten
- `public/katzenbuckel/` – Reihe und Buchseiten
- `public/die-katzen-vom-katzenbuckel/` – Kinderbuchreihe und Buchseiten
- `public/mira-wilden/` – Autorinnenprofil
- `public/assets/` – CSS und Bilder
- `public/sitemap.xml` – Sitemap
- `public/robots.txt` – Crawler-Regeln

## SEO
Die Website verwendet Canonical URLs, Open Graph Metadaten sowie strukturierte Daten (`Person`, `WebSite`, `Book`).
