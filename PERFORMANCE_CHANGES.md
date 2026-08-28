# Performance-Optimierung

- Alle PNG/JPG/JPEG-Bilder unter `public/assets/images/` nach WebP konvertiert.
- HTML-Bildpfade auf `.webp` umgestellt.
- Nicht unmittelbar sichtbare Bilder mit `loading="lazy"` und `decoding="async"` versehen.
- Das Hero-Bild der Startseite bleibt eager und erhält `fetchpriority="high"`.
- `_headers` ergänzt, damit statische Assets langfristig im Browser/CDN gecacht werden können.
- Originale Rasterdateien wurden entfernt, damit das Repository nicht doppelt belastet wird.

## Bildvolumen
Vorher: 21.02 MB
Nachher: 5.88 MB
Ersparnis: 72.1 %
