"""Draw the 26 November 2026 world-news image (1024x1024 PNG).

Original flat vector-style pictograms drawn with Pillow primitives.
No photographs, no copied artwork, no likenesses.
Run: python3 draw.py  ->  writes entry.png next to this file.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
INK = (20, 33, 61)
PAPER = (250, 247, 240)
WHITE = (255, 255, 255)
GREY = (70, 78, 94)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, fill, max_width, leading=6, align="left"):
    x, y = xy
    for line in wrap(draw, text, fnt, max_width):
        if align == "center":
            tw = draw.textlength(line, font=fnt)
            draw.text((x + (max_width - tw) / 2, y), line, font=fnt, fill=fill)
        else:
            draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + leading
    return y


# ---------- pictograms (drawn in a 150x150 box at x, y) ----------

def pic_ship(d, x, y, c):
    # container ship
    d.polygon([(x + 8, y + 96), (x + 142, y + 96), (x + 128, y + 122), (x + 22, y + 122)], fill=c)
    for i, col in enumerate([(231, 76, 60), (52, 152, 219), (46, 204, 113), (241, 196, 15)]):
        bx = x + 22 + i * 26
        d.rectangle([bx, y + 72, bx + 22, y + 94], fill=col, outline=WHITE, width=2)
        d.rectangle([bx, y + 50, bx + 22, y + 70], fill=col, outline=WHITE, width=2)
    d.rectangle([x + 112, y + 52, x + 132, y + 94], fill=(236, 240, 241), outline=c, width=2)
    d.line([(x, y + 132), (x + 150, y + 132)], fill=(52, 152, 219), width=5)
    d.arc([x + 10, y + 124, x + 50, y + 142], 0, 180, fill=(52, 152, 219), width=4)
    d.arc([x + 100, y + 124, x + 140, y + 142], 0, 180, fill=(52, 152, 219), width=4)


def pic_refinery(d, x, y, c):
    # refinery towers + droplet
    d.rectangle([x + 18, y + 40, x + 42, y + 120], fill=c)
    d.rectangle([x + 58, y + 22, x + 86, y + 120], fill=c)
    d.rectangle([x + 102, y + 56, x + 124, y + 120], fill=c)
    d.rectangle([x + 12, y + 118, x + 132, y + 126], fill=c)
    for tx, ty in [(30, 40), (72, 22), (113, 56)]:
        d.ellipse([x + tx - 9, y + ty - 16, x + tx + 9, y + ty - 2], fill=(149, 165, 166))
    # droplet
    d.polygon([(x + 72, y + 128), (x + 60, y + 142), (x + 84, y + 142)], fill=(243, 156, 18))
    d.ellipse([x + 60, y + 134, x + 84, y + 150], fill=(243, 156, 18))


def pic_rocket(d, x, y, c):
    # station with solar panels + rocket above
    d.rectangle([x + 55, y + 88, x + 95, y + 102], fill=(52, 152, 219))
    d.rectangle([x + 12, y + 91, x + 52, y + 99], fill=(93, 173, 226))
    d.rectangle([x + 98, y + 91, x + 138, y + 99], fill=(93, 173, 226))
    d.rectangle([x + 70, y + 80, x + 80, y + 110], fill=(52, 152, 219))
    # rocket (vertical, centre)
    d.polygon([(x + 75, y + 2), (x + 92, y + 34), (x + 58, y + 34)], fill=(231, 76, 60))
    d.rectangle([x + 58, y + 34, x + 92, y + 66], fill=c)
    d.ellipse([x + 68, y + 42, x + 82, y + 56], fill=WHITE, outline=c, width=2)
    d.polygon([(x + 58, y + 54), (x + 44, y + 74), (x + 58, y + 74)], fill=(231, 76, 60))
    d.polygon([(x + 92, y + 54), (x + 106, y + 74), (x + 92, y + 74)], fill=(231, 76, 60))
    d.polygon([(x + 66, y + 74), (x + 84, y + 74), (x + 75, y + 92)], fill=(243, 156, 18))
    for sx, sy in [(18, 14), (126, 20), (110, 52), (26, 60)]:
        d.ellipse([x + sx, y + sy, x + sx + 5, y + sy + 5], fill=(241, 196, 15))


def pic_gavel(d, x, y, c):
    # gavel + chip
    d.rectangle([x + 22, y + 26, x + 78, y + 82], outline=c, width=5)
    for i in range(4):
        px = x + 30 + i * 12
        d.line([(px, y + 14), (px, y + 26)], fill=c, width=4)
        d.line([(px, y + 82), (px, y + 94)], fill=c, width=4)
        py = y + 34 + i * 12
        d.line([(x + 10, py), (x + 22, py)], fill=c, width=4)
        d.line([(x + 78, py), (x + 90, py)], fill=c, width=4)
    d.rectangle([x + 38, y + 42, x + 62, y + 66], fill=(52, 152, 219))
    # gavel
    d.polygon([(x + 92, y + 44), (x + 128, y + 80), (x + 116, y + 92), (x + 80, y + 56)], fill=(160, 110, 60))
    d.rectangle([x + 84, y + 34, x + 104, y + 54], fill=(120, 80, 40))
    d.rectangle([x + 112, y + 62, x + 132, y + 82], fill=(120, 80, 40))
    d.rectangle([x + 76, y + 122, x + 140, y + 132], fill=(120, 80, 40))
    d.rectangle([x + 88, y + 112, x + 128, y + 122], fill=(160, 110, 60))


def pic_boat(d, x, y, c):
    # boat on waves + island
    d.ellipse([x + 96, y + 8, x + 126, y + 38], fill=(241, 196, 15))
    d.polygon([(x + 14, y + 88), (x + 136, y + 88), (x + 120, y + 114), (x + 30, y + 114)], fill=c)
    d.line([(x + 74, y + 30), (x + 74, y + 88)], fill=c, width=5)
    d.polygon([(x + 78, y + 34), (x + 78, y + 80), (x + 112, y + 80)], fill=(236, 240, 241), outline=c)
    d.polygon([(x + 70, y + 42), (x + 70, y + 80), (x + 44, y + 80)], fill=(236, 240, 241), outline=c)
    for wx in (6, 52, 98):
        d.arc([x + wx, y + 116, x + wx + 44, y + 138], 0, 180, fill=(52, 152, 219), width=5)
    for wx in (28, 74):
        d.arc([x + wx, y + 130, x + wx + 44, y + 150], 0, 180, fill=(93, 173, 226), width=4)


def pic_court(d, x, y, c):
    # courthouse
    d.polygon([(x + 75, y + 8), (x + 138, y + 40), (x + 12, y + 40)], fill=c)
    d.ellipse([x + 68, y + 22, x + 82, y + 36], fill=WHITE)
    for i in range(4):
        cx = x + 26 + i * 28
        d.rectangle([cx, y + 48, cx + 12, y + 106], fill=c)
    d.rectangle([x + 12, y + 40, x + 138, y + 48], fill=c)
    d.rectangle([x + 8, y + 106, x + 142, y + 114], fill=c)
    d.rectangle([x + 2, y + 120, x + 148, y + 128], fill=c)
    d.rectangle([x + 2, y + 134, x + 148, y + 142], fill=(149, 165, 166))


PANELS = [
    {
        "tag": "GLOBAL TRADE", "color": (192, 57, 43), "pic": pic_ship,
        "head": "US proposes tariffs on 14 partners",
        "cap": "Washington cites 'excess factory capacity'. China faces the highest rate: 20% on top of ~25% from Trump's first term.",
        "src": "Reuters",
    },
    {
        "tag": "MIDDLE EAST · ENERGY", "color": (211, 84, 0), "pic": pic_refinery,
        "head": "Houthis claim refinery attack; oil jumps",
        "cap": "Yemen's Houthis said they hit Saudi Arabia's Ras Tanura refinery and Riyadh. Brent settled at $94.61, up 3.5%.",
        "src": "Reuters",
    },
    {
        "tag": "SPACE", "color": (36, 113, 163), "pic": pic_rocket,
        "head": "First foreign visitor to China's station",
        "cap": "Shenzhou-24 docked with Tiangong carrying Pakistan's Muhammad Zeeshan Ali — the first foreign astronaut aboard.",
        "src": "AP / Xinhua",
    },
    {
        "tag": "TECH · LAW", "color": (108, 52, 131), "pic": pic_gavel,
        "head": "Huawei convicted in US trial",
        "cap": "A New York jury found Huawei guilty on 10 of 12 counts, incl. conspiring to steal trade secrets; acquitted of racketeering.",
        "src": "Reuters / CNN",
    },
    {
        "tag": "EUROPE · MIGRATION", "color": (23, 165, 137), "pic": pic_boat,
        "head": "Record 1,990 reach Canaries in a day",
        "cap": "Fifteen boats reached El Hierro in 24 hours — a single-day record. Over 26,000 arrived this year.",
        "src": "AP / Reuters",
    },
    {
        "tag": "AFRICA", "color": (39, 120, 70), "pic": pic_court,
        "head": "Court lifts Ramaphosa impeachment threat",
        "cap": "The Western Cape High Court declared the 2022 Phala Phala report unlawful, ending the impeachment path for now.",
        "src": "Al Jazeera",
    },
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # masthead
    d.rectangle([0, 0, W, 148], fill=INK)
    d.rectangle([0, 148, W, 156], fill=(241, 196, 15))
    d.text((W // 2, 16), "THE WORLD IN ONE DAY", font=font(BOLD, 40), fill=WHITE, anchor="ma")
    d.text((W // 2, 64), "THURSDAY 26 NOVEMBER 2026", font=font(BOLD, 46), fill=(241, 196, 15), anchor="ma")
    d.text((W // 2, 118), "Six consequential stories reported on 26 November 2026", font=font(REG, 20), fill=(200, 210, 225), anchor="ma")

    # grid 2 x 3
    margin, gap = 20, 12
    top = 164
    panel_w = (W - margin * 2 - gap) // 2
    panel_h = 244
    tag_f = font(BOLD, 16)
    head_f = font(BOLD, 26)
    cap_f = font(REG, 18)
    src_f = font(REG, 14)

    for i, p in enumerate(PANELS):
        col, row = i % 2, i // 2
        x = margin + col * (panel_w + gap)
        y = top + row * (panel_h + gap)
        d.rounded_rectangle([x, y, x + panel_w, y + panel_h], radius=12, fill=WHITE, outline=(205, 200, 188), width=2)
        # tag strip
        d.rounded_rectangle([x, y, x + panel_w, y + 32], radius=12, fill=p["color"])
        d.rectangle([x, y + 18, x + panel_w, y + 32], fill=p["color"])
        d.text((x + 12, y + 7), p["tag"], font=tag_f, fill=WHITE)
        d.text((x + panel_w - 12, y + 8), p["src"], font=src_f, fill=WHITE, anchor="ra")
        # pictogram left, text right
        p["pic"](d, x + 10, y + 48, p["color"])
        tx = x + 168
        tw = panel_w - 180
        ty = text_block(d, (tx, y + 44), p["head"], head_f, INK, tw, leading=4)
        text_block(d, (tx, ty + 4), p["cap"], cap_f, GREY, tw, leading=5)

    # UN ticker strip
    ty = top + 3 * (panel_h + gap) + 2
    d.rounded_rectangle([margin, ty, W - margin, ty + 56], radius=10, fill=(253, 237, 236), outline=(192, 57, 43), width=2)
    d.text((margin + 14, ty + 8), "ALSO REPORTED 26 NOV  ·  UN:", font=font(BOLD, 17), fill=(192, 57, 43))
    d.text((margin + 14, ty + 30), "47,000 women and girls killed by partners or family in 2025 — about five every hour (UNODC / UN Women).",
           font=font(REG, 17), fill=INK)

    # footer
    fy = ty + 64
    d.text((W // 2, fy), "All stories reported on Thursday 26 November 2026  ·  Sources: Reuters · AP · Xinhua · CNN · Al Jazeera · UN",
           font=font(REG, 15), fill=GREY, anchor="ma")

    img.save("entry.png", "PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
