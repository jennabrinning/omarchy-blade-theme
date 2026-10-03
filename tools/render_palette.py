"""Draw the actual 16 terminal slots from colors.toml. Requires Pillow."""
from pathlib import Path
import tomllib
from PIL import Image, ImageDraw, ImageFont

root = Path(__file__).resolve().parents[1]
p = tomllib.loads((root / 'colors.toml').read_text())
font_path = '/usr/share/fonts/TTF/JetBrainsMonoNerdFont-Regular.ttf'
title = ImageFont.truetype(font_path, 32)
body = ImageFont.truetype(font_path, 22)
small = ImageFont.truetype(font_path, 18)
slots = [
    ('Black', 'background'), ('Red', 'red'), ('Green', 'green'),
    ('Yellow', 'yellow'), ('Blue', 'blue'), ('Magenta', 'magenta'),
    ('Cyan', 'cyan'), ('White', 'foreground'),
    ('Bright black', 'muted'), ('Bright red', 'bright_red'),
    ('Bright green', 'bright_green'), ('Bright yellow', 'bright_yellow'),
    ('Bright blue', 'bright_blue'), ('Bright magenta', 'bright_magenta'),
    ('Bright cyan', 'bright_cyan'), ('Bright white', 'bright_foreground'),
]
im = Image.new('RGB', (1440, 850), p['dark_background'])
d = ImageDraw.Draw(im)
d.text((40, 28), 'BLADE / TYRELL', font=title, fill=p['accent'])
d.text((40, 78), 'Terminal colours / normal 0–7 / bright 8–15', font=body, fill=p['foreground'])
for i, (label, key) in enumerate(slots):
    x = 40 + (i % 4) * 350
    y = 145 + (i // 4) * 164
    d.rounded_rectangle((x, y, x+310, y+140), radius=8, fill=p['lighter_background'])
    d.rectangle((x+14, y+14, x+296, y+64), fill=p[key], outline=p['muted'], width=1)
    d.text((x+14, y+78), f'{i:02d}  {label}', font=body, fill=p['foreground'])
    d.text((x+14, y+109), p[key], font=small, fill=p['light_foreground'])
im.save(root / 'palette.png')
