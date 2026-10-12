from pathlib import Path
import re, requests, html
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
books=[('Die Glocke im Nebel','die-katzen-vom-katzenbuckel-die-glocke-im-nebel.webp'),('Die Spur der sieben Schläge','die-katzen-vom-katzenbuckel-die-spur-der-sieben-schlaege.webp'),('Die verschwundene Schulgeschichte','die-katzen-vom-katzenbuckel-die-verschwundene-schulgeschichte.webp')]
texts=[]
for p in Path('.').rglob('*'):
    if not p.is_file() or any(x in p.parts for x in {'.git','node_modules','.next','dist','build'}): continue
    if p.suffix.lower() not in {'.js','.jsx','.ts','.tsx','.json','.md','.mdx','.html','.txt','.yaml','.yml'}: continue
    try: texts.append((p,p.read_text(errors='ignore')))
    except Exception: pass
s=requests.Session();s.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36','Accept-Language':'de-DE,de;q=0.9,en;q=0.7'})
def asin_for(title):
    for p,t in texts:
        n=t.lower().find(title.lower())
        if n<0: continue
        near=t[max(0,n-5000):n+5000]
        m=re.search(r'amazon\.de[^\s\"\'<>]*(?:/dp/|/gp/product/)([A-Z0-9]{10})',near,re.I) or re.search(r'\b(B0[A-Z0-9]{8})\b',near,re.I)
        if m:return m.group(1).upper(),str(p)
    q=requests.utils.quote(title+' Mira Wilden');r=s.get('https://www.amazon.de/s?k='+q,timeout=30);r.raise_for_status();soup=BeautifulSoup(r.text,'html.parser')
    for b in soup.select('[data-asin]'):
        a=(b.get('data-asin') or '').strip()
        if len(a)==10 and title.lower() in b.get_text(' ',strip=True).lower():return a.upper(),'amazon-search'
    m=re.search(r'/dp/([A-Z0-9]{10})',r.text)
    if m:return m.group(1).upper(),'amazon-search-fallback'
    raise RuntimeError('No ASIN: '+title)
def image_url(a):
    r=s.get('https://www.amazon.de/dp/'+a,timeout=30);r.raise_for_status();t=html.unescape(r.text)
    for pat in [r'"hiRes"\s*:\s*"(https://m\.media-amazon\.com/images/I/[^"]+)"',r'"large"\s*:\s*"(https://m\.media-amazon\.com/images/I/[^"]+)"',r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"',r'<img[^>]+id="landingImage"[^>]+src="([^"]+)"']:
        m=re.search(pat,t,re.I)
        if m:return re.sub(r'\._[A-Z0-9_,]+_\.', '.',m.group(1).replace('\\u0026','&').replace('\\/','/'))
    raise RuntimeError('No image: '+a)
out=Path('public/assets/images');out.mkdir(parents=True,exist_ok=True)
for title,name in books:
    a,src=asin_for(title);u=image_url(a);print(title,a,src,u);r=s.get(u,timeout=60);r.raise_for_status();im=Image.open(BytesIO(r.content)).convert('RGB').resize((1000,1600),Image.Resampling.LANCZOS);d=out/name;im.save(d,'WEBP',quality=80,method=6);print(name,d.stat().st_size)
    if d.stat().st_size<100000:raise RuntimeError('Unexpected small cover '+name)
