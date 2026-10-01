from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from html import escape
import base64

ROOT=Path(__file__).parent
OUT=ROOT.parent/'assets/profile'
OUT.mkdir(parents=True,exist_ok=True)
font=instantiateVariableFont(TTFont(ROOT/'fonts/SpaceGrotesk.ttf'),{'wght':600})
glyphs=font.getGlyphSet()
cmap=font.getBestCmap()
units=font['head'].unitsPerEm

def text(label,x,y,size,color='#f0f1fa',spacing=0,weight=600):
    cursor=0;paths=[]
    for char in label:
        name=cmap.get(ord(char))
        if name is None: raise ValueError(char)
        pen=SVGPathPen(glyphs);glyphs[name].draw(pen)
        if pen.getCommands():paths.append(f'<path d="{pen.getCommands()}" transform="translate({cursor:.3f} 0)"/>')
        cursor+=glyphs[name].width+spacing*units/size
    return f'<g fill="{color}" transform="translate({x} {y}) scale({size/units} {-size/units})" aria-hidden="true">'+''.join(paths)+'</g>'

image='data:image/webp;base64,'+base64.b64encode((ROOT/'sculpture.webp').read_bytes()).decode()
for mobile in (False,True):
    w,h=(640,860) if mobile else (1200,720)
    for animated in (False,True):
        label='Mikhail Kim, also known as Misha. Software engineer working with Python, AI and backend systems.'
        s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',f'<title id="title">{escape(label)}</title>','<desc id="desc">An original glass and aluminium sculpture connects illuminated layers beside a custom MK monogram. The name and role are always visible.</desc>',f'<defs><clipPath id="frame"><rect width="{w}" height="{h}" rx="24"/></clipPath><linearGradient id="shade"><stop stop-color="#0b1120" stop-opacity="0.24"/><stop offset=".58" stop-color="#0b1120" stop-opacity="0"/></linearGradient><radialGradient id="glow"><stop stop-color="#ffeac0" stop-opacity=".56"/><stop offset="1" stop-color="#ffeac0" stop-opacity="0"/></radialGradient></defs>']
        if animated:
            s.append('<style>@keyframes breathe{0%,100%{opacity:0}45%{opacity:.56}}.light{animation:breathe 3.8s ease-in-out 1;opacity:0}@media(prefers-reduced-motion:reduce){.light{animation:none}}</style>')
        s.append(f'<g clip-path="url(#frame)"><rect width="{w}" height="{h}" fill="#0d1425"/>')
        if mobile:
            s.append(f'<image href="{image}" x="-465" y="188" width="1050" height="700"/>')
            s.append('<defs><linearGradient id="mobileTop" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#0d1425"/><stop offset="1" stop-color="#0d1425" stop-opacity="0"/></linearGradient><linearGradient id="mobileRight"><stop stop-color="#0d1425" stop-opacity="0"/><stop offset="1" stop-color="#0d1425"/></linearGradient></defs><rect x="0" y="187" width="640" height="120" fill="url(#mobileTop)"/><rect x="530" y="188" width="70" height="700" fill="url(#mobileRight)"/>')
            s.append('<path d="M0 265V0L113 151 226 0V265M226 145 352 0M226 145 352 265" transform="translate(552 45) scale(.13)" fill="none" stroke="#bfc6e3" stroke-width="18" stroke-linejoin="round"/>')
            s.append(text('HEY, I\'M MISHA.',40,82,24,'#c7cce3',1.1))
            s.append(text('Mikhail Kim',36,160,66))
            s.append(text('Python / AI / Backend systems',40,205,28,'#c7cce3'))
            if animated:s.append('<circle class="light" cx="297" cy="533" r="56" fill="url(#glow)"/>')
        else:
            s.append(f'<image href="{image}" x="0" y="-40" width="1200" height="800"/>')
            s.append('<rect width="680" height="720" fill="url(#shade)"/>')
            s.append('<path d="M0 265V0L113 151 226 0V265M226 145 352 0M226 145 352 265" transform="translate(60 46) scale(.13)" fill="none" stroke="#bfc6e3" stroke-width="18" stroke-linejoin="round"/>')
            s.append(text('HEY, I\'M MISHA.',60,116,21,'#c7cce3',1.8))
            s.append(text('Mikhail',53,270,111))
            s.append(text('Kim',53,399,148))
            s.append(text('Software engineer',60,462,31,'#d1d4e8'))
            s.append(text('PYTHON / AI / SYSTEMS',60,644,22,'#bfc6e3',1.2))
            if animated:s.append('<circle class="light" cx="871" cy="354" r="62" fill="url(#glow)"/>')
        s.append('</g></svg>')
        filename=f'identity-{ "mobile" if mobile else "desktop" }{ "" if animated else "-still" }.svg'
        (OUT/filename).write_text(''.join(s))

for key,label,accent in [('resume','Résumé',True),('telegram','Telegram',False),('email','Email',False)]:
    # 96 x 44 CSS pixels: each image remains a 44px-high link target on mobile.
    fill='#cbc9ff' if accent else '#172136';ink='#171c34' if accent else '#ebedfb'
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="144" height="66" viewBox="0 0 144 66" role="img" aria-label="{label}">',f'<rect x="1" y="1" width="142" height="64" rx="13" fill="{fill}" stroke="{ "#a9a8ed" if accent else "#485571" }"/>']
    width=sum(glyphs[cmap[ord(c)]].width for c in label)/units*22
    s.append(text(label,(144-width)/2,41,22,ink))
    s.append('</svg>')
    (OUT/f'link-{key}.svg').write_text(''.join(s))


print("Built 4 responsive identity images and 3 contact buttons.")
