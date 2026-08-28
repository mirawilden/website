# SEO-Überarbeitung – 28.08.2026

## Geändert
- echte Katzenbuckel- und Kinderbuchcover statt generischer Banner eingebunden
- weboptimierte Coverkopien mit suchfreundlichen Dateinamen erzeugt
- Startseiten-Titel und Meta-Description präzisiert
- Mira Wilden als zentrale `Person`-Entität mit stabiler `@id` modelliert
- `sameAs` um das direkte Goodreads-Autorinnenprofil ergänzt
- `WebSite`-Schema auf der Startseite ergänzt
- Book-Schema für Heimkehr und Glühende Herzen erweitert
- individuelle Buchseiten für Katzenbuckel Band 1–3 angelegt
- individuelle Buchseiten für Die Katzen vom Katzenbuckel Band 1–3 angelegt
- Bücherübersicht um alle sechs Katzenbuckel-Titel erweitert
- Reihenübersichten mit echten Covern und internen Links ausgebaut
- sitemap.xml um alle neuen Buchseiten ergänzt
- GitHub/Cloudflare-README ergänzt
- JSON-LD und interne Dateilinks validiert

## Neue URLs
- /katzenbuckel/drei-katzen-sind-zwei-zu-viel/
- /katzenbuckel/drei-katzen-und-ein-gast-zu-viel/
- /katzenbuckel/drei-katzen-im-laternenlicht/
- /die-katzen-vom-katzenbuckel/die-glocke-im-nebel/
- /die-katzen-vom-katzenbuckel/die-spur-der-sieben-schlaege/
- /die-katzen-vom-katzenbuckel/die-verschwundene-schulgeschichte/

## Deployment
Den Inhalt dieses ZIPs über den lokalen Clone des GitHub-Repositories kopieren,
Änderungen prüfen, committen und auf `main` pushen. GitHub Actions übernimmt
das Deployment zu Cloudflare.
