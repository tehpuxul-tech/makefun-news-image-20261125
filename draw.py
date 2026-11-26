#!/usr/bin/env python3
"""Draw the 25 November 2026 world-news poster (1024x1024 PNG).

Drawn programmatically with Python/PIL so every word is exactly as written
and stays legible at 1024px and at ~300px. Six main stories that happened,
or were first reported, on Wednesday 25 November 2026, each in its own
panel with a drawn scene, plus a ticker of six more verified stories from
the same day, so the image covers more of the day than the six-panel
format of the 18-24 Nov entries did. The kit's RULES set no panel count:
the judge weighs naming the day, breadth across regions and fields,
readability, faithfulness and craft.

Date care (all second-checked 2026-11-26 against dated 25 Nov sources):
- Tariffs: Trump/USTR proposed new duties on 14 trading partners incl.
  China, Japan and the EU on Wed 25 Nov; headline rates 20-40%, capped
  lower under trade deals; China 20% (40% if the truce unravels);
  no effect before a 25 Jan public hearing (Reuters, Nov 25).
- Shenzhou-24: launched 25 Nov 00:18 UTC from Jiuquan, docked with
  Tiangong 03:56 UTC; Pakistan's Muhammad Zeeshan Ali is the first
  foreign astronaut aboard Tiangong and the first Pakistani in orbit
  (Xinhua, Nov 25; Wikipedia; Aviation Week).
- Hormuz: Iran's Revolutionary Guards navy said two tankers struck naval
  mines early Wed 25 Nov, exploded and caught fire; the claim is Iran's
  alone, no independent confirmation, ships unnamed (Reuters, Nov 25).
  Panel says "Iran says" and "no independent confirmation yet".
- Ras Tanura: Houthis said they hit Saudi Arabia's largest refinery on
  Wed 25 Nov and caused fires; NASA satellite imagery reviewed by Reuters
  showed thick black smoke over ~600 sq km; the coalition said four
  drones were destroyed over Ras Tanura and did not confirm a hit; a
  Houthi projectile fell at Jazan port, minor damage, no injuries;
  Jeddah was threatened and claimed but no hit was confirmed, so the
  panel does NOT claim a Jeddah hit (Reuters, Nov 25).
- Gaza: an Israeli strike early Wed 25 Nov on a flat in Shati camp,
  Gaza City, killed Muhammad Majid Abu al-Awf, Hamas internal security
  chief for northern Gaza, his wife Noura, 41, and daughters Yusra, 15,
  and Jana, 13. He is a DIFFERENT man from Naeem Abu Nahel, the Hamas
  security chief killed on Tue 24 Nov; this is the second chief killed
  in 24 hours (Reuters, Nov 25; Xinhua, Nov 25).
- Samara refineries: Ukrainian drones hit the Syzran and Kuibyshev
  Rosneft refineries overnight 24-25 Nov; fires reported at both.
  The Samara governor confirmed a drone attack on industrial sites;
  refinery-specific reports were not independently verified (Kyiv
  Independent / Reuters via monitoring channels, Nov 25). Panel says
  "fires reported". The Benghazi warship attack was 22 Nov, NOT 25 Nov,
  and is deliberately left out.
Ticker items, all reported 25 Nov 2026:
- Sudan: RSF drone strikes on Damazin and Roseires in Blue Nile were
  REPORTED Wed 25 Nov (the strikes were Tue night): 19 civilians killed
  in Damazin, incl. six women, 20 wounded, per rights group Emergency
  Lawyers (Reuters, Nov 25).
- Egypt: a fuel tanker overturned on Cairo's Ring Road in Al Warraq,
  Giza, on Wed 25 Nov; fire killed at least 30, injured 21, toll
  preliminary (AP, Nov 25).
- Markets: South Korea's KOSPI fell 6.16% to 4,697.51 on Wed 25 Nov,
  lowest close since 13 Jan (Yonhap, Nov 25).
- Pacific: Australia and Solomon Islands signed a security treaty in
  Canberra on Wed 25 Nov; Australia is the Solomons' "primary security
  partner" (Reuters/AP, Nov 25). The claim that the Solomons will let
  its 2022 pact with China lapse is unconfirmed and is NOT used.
- Iran: the US Virtual Embassy told US citizens to leave Iran at once
  on Wed 25 Nov (US security alert, Nov 25).
- Ukraine: Russian overnight strikes killed seven people in Ukraine
  (Euronews headline, Nov 25).
Deliberately left out: 24 Nov stories (Gaza's Naeem Abu Nahel, the
Riyadh PIF tower strike, Huawei verdict, RAK bus crash, KADIZ),
22 Nov stories (Benghazi warship, COP31, Bahrain), and Jensen Huang's
return as Nvidia CEO (announced Mon 23 Nov).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (244, 241, 235)     # warm paper background
HEADER = (24, 44, 66)       # deep navy header
INK = (26, 26, 26)
BODY = (64, 62, 56)
MUTED = (96, 94, 86)
CARD = (255, 255, 255)
GOLD = (203, 164, 41)
CARD_EDGE = (214, 209, 194)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def fnt(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------------- header ----------------
d.rectangle([0, 0, W, 150], fill=HEADER)
d.rectangle([0, 150, W, 156], fill=GOLD)
d.text((512, 22), "THE WORLD IN ONE DAY", font=fnt(BOLD, 24),
       fill=GOLD, anchor="ma")
d.text((512, 82), "25 NOVEMBER 2026", font=fnt(SERIF, 62),
       fill=(255, 255, 255), anchor="mm")
d.text((512, 128), "WEDNESDAY  \u2022  TWELVE STORIES FROM AROUND THE GLOBE",
       font=fnt(BOLD, 18), fill=(198, 204, 219), anchor="ma")

# ---------------- main panels ----------------
# (kicker, accent, headline, body, glyph)
PANELS = [
    ("USA \u2022 WASHINGTON", (24, 44, 66),
     "New tariffs on 14 partners",
     "Trump proposes 20\u201340% duties on China, the EU and Japan, "
     "capped lower under trade deals. Hearing 25 Jan.",
     "chart"),
    ("CHINA \u2022 JIUQUAN", (150, 30, 30),
     "First foreigner reaches Tiangong",
     "Shenzhou-24 launches Pakistan's Muhammad Zeeshan Ali \u2014 the "
     "first Pakistani in orbit \u2014 and docks with the station.",
     "rocket"),
    ("IRAN \u2022 STRAIT OF HORMUZ", (13, 115, 119),
     "Iran says tankers hit mines",
     "Two tankers explode and burn in the Strait of Hormuz, Iran's "
     "navy says; no independent confirmation yet.",
     "mine"),
    ("SAUDI ARABIA \u2022 RAS TANURA", (146, 64, 14),
     "Houthis claim refinery hit",
     "Smoke seen from space over Ras Tanura; the coalition says four "
     "drones downed. A projectile fell at Jazan port.",
     "flame"),
    ("GAZA \u2022 GAZA CITY", (178, 34, 34),
     "Second Hamas chief killed in a day",
     "A strike on a Gaza City flat kills Muhammad Majid Abu al-Awf, "
     "his wife and two daughters, early Wednesday.",
     "target"),
    ("UKRAINE \u2022 SAMARA, RUSSIA", (40, 70, 130),
     "Two Russian refineries ablaze",
     "Ukrainian drones hit the Syzran and Kuibyshev refineries "
     "overnight; fires reported at both plants.",
     "drone"),
]

MARGIN = 24
GAP = 12
COL_W = (W - 2 * MARGIN - GAP) // 2
ROW_H = 196
GRID_TOP = 168


def glyph(draw, kind, cx, cy, color):
    w = (255, 255, 255)
    if kind == "target":
        draw.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], outline=w, width=5)
        draw.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], outline=w, width=4)
        draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=w)
        draw.line([cx - 28, cy, cx - 14, cy], fill=w, width=4)
        draw.line([cx + 14, cy, cx + 28, cy], fill=w, width=4)
        draw.line([cx, cy - 28, cx, cy - 14], fill=w, width=4)
        draw.line([cx, cy + 14, cx, cy + 28], fill=w, width=4)
    elif kind == "rocket":
        draw.polygon([(cx, cy - 30), (cx + 12, cy - 6), (cx + 12, cy + 16),
                      (cx, cy + 26), (cx - 12, cy + 16), (cx - 12, cy - 6)],
                     outline=w, width=4)
        draw.polygon([(cx - 12, cy + 10), (cx - 22, cy + 26),
                      (cx - 12, cy + 20)], fill=w)
        draw.polygon([(cx + 12, cy + 10), (cx + 22, cy + 26),
                      (cx + 12, cy + 20)], fill=w)
        draw.ellipse([cx - 4, cy - 20, cx + 4, cy - 12], fill=w)
    elif kind == "flame":
        draw.polygon([(cx, cy - 28), (cx + 14, cy - 4), (cx + 24, cy + 12),
                      (cx + 10, cy + 26), (cx - 10, cy + 26),
                      (cx - 24, cy + 12), (cx - 14, cy - 4)], fill=w)
        draw.ellipse([cx - 7, cy + 4, cx + 7, cy + 20], fill=color)
    elif kind == "chart":
        # rising bar chart with an arrow
        draw.rectangle([cx - 26, cy + 6, cx - 14, cy + 24], fill=w)
        draw.rectangle([cx - 8, cy - 2, cx + 4, cy + 24], fill=w)
        draw.rectangle([cx + 10, cy - 12, cx + 22, cy + 24], fill=w)
        draw.line([cx - 28, cy - 18, cx + 28, cy - 26], fill=w, width=4)
        draw.polygon([(cx + 28, cy - 26), (cx + 18, cy - 28),
                      (cx + 24, cy - 16)], fill=w)
    elif kind == "mine":
        # a tanker hull above a spiked sea mine
        draw.polygon([(cx - 28, cy - 18), (cx + 28, cy - 18),
                      (cx + 22, cy - 4), (cx - 22, cy - 4)], fill=w)
        draw.rectangle([cx - 14, cy - 28, cx + 2, cy - 18], fill=w)
        draw.line([cx - 28, cy + 2, cx + 28, cy + 2], fill=color, width=3)
        draw.ellipse([cx - 12, cy + 8, cx + 12, cy + 28], outline=w, width=4)
        for dx, dy in [(-16, 18), (16, 18), (0, 4), (-8, 28), (8, 28)]:
            draw.line([cx + dx, cy + dy, cx + dx * 1.5, cy + dy * 1.15],
                      fill=w, width=3)
    elif kind == "drone":
        draw.rectangle([cx - 14, cy - 6, cx + 14, cy + 6], outline=w, width=4)
        draw.ellipse([cx - 28, cy - 18, cx - 12, cy - 2], outline=w, width=3)
        draw.ellipse([cx + 12, cy - 18, cx + 28, cy - 2], outline=w, width=3)
        draw.ellipse([cx - 28, cy + 2, cx - 12, cy + 18], outline=w, width=3)
        draw.ellipse([cx + 12, cy + 2, cx + 28, cy + 18], outline=w, width=3)
        draw.line([cx - 14, cy - 6, cx - 20, cy - 12], fill=w, width=3)
        draw.line([cx + 14, cy - 6, cx + 20, cy - 12], fill=w, width=3)
        draw.line([cx - 14, cy + 6, cx - 20, cy + 12], fill=w, width=3)
        draw.line([cx + 14, cy + 6, cx + 20, cy + 12], fill=w, width=3)
        draw.ellipse([cx - 3, cy + 12, cx + 3, cy + 18], fill=w)
        draw.polygon([(cx - 3, cy + 18), (cx + 3, cy + 18), (cx, cy + 28)],
                     fill=w)


for i, (kicker, accent, headline, body, g) in enumerate(PANELS):
    col, row = i % 2, i // 2
    x0 = MARGIN + col * (COL_W + GAP)
    y0 = GRID_TOP + row * (ROW_H + GAP)
    x1, y1 = x0 + COL_W, y0 + ROW_H
    d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=CARD,
                        outline=CARD_EDGE, width=2)
    BAR = 78
    d.rounded_rectangle([x0, y0, x0 + BAR, y1], radius=14, fill=accent)
    d.rectangle([x0 + BAR - 14, y0, x0 + BAR, y1], fill=accent)
    d.rectangle([x0, y0, x0 + BAR, y0 + 14], fill=accent)
    d.rectangle([x0, y0 + ROW_H - 14, x0 + BAR, y1], fill=accent)
    glyph(d, g, x0 + BAR // 2, y0 + ROW_H // 2, accent)
    tx = x0 + BAR + 16
    tw = x1 - tx - 16
    d.text((tx, y0 + 12), kicker, font=fnt(BOLD, 18), fill=accent)
    y = y0 + 36
    for ln in wrap(d, headline, fnt(BOLD, 28), tw):
        d.text((tx, y), ln, font=fnt(BOLD, 28), fill=INK)
        y += 33
    y += 4
    for ln in wrap(d, body, fnt(REG, 19), tw):
        d.text((tx, y), ln, font=fnt(REG, 19), fill=BODY)
        y += 25

# ---------------- ticker: also on 25 November ----------------
TICK_TOP = GRID_TOP + 3 * ROW_H + 2 * GAP + 12
TICK_H = 168
d.rounded_rectangle([MARGIN, TICK_TOP, W - MARGIN, TICK_TOP + TICK_H],
                    radius=14, fill=(24, 44, 66))
d.text((MARGIN + 18, TICK_TOP + 8), "ALSO ON 25 NOVEMBER",
       font=fnt(BOLD, 20), fill=GOLD)
TICKER = [
    ("SUDAN", "RSF drone strikes reported: 19 civilians killed in Blue Nile"),
    ("EGYPT", "Fuel tanker fire on Cairo ring road kills at least 30"),
    ("SOUTH KOREA", "KOSPI plunges 6.16%, lowest close since January"),
    ("PACIFIC", "Australia\u2013Solomon Islands sign security treaty"),
    ("IRAN", "US tells its citizens to leave Iran at once"),
    ("UKRAINE", "Russian overnight strikes kill seven in Ukraine"),
]
TCOL_W = (W - 2 * MARGIN - 36 - 12) // 2
for i, (region, text) in enumerate(TICKER):
    col, row = i % 2, i // 2
    tx = MARGIN + 18 + col * (TCOL_W + 12)
    ty = TICK_TOP + 40 + row * 42
    prefix = "\u2022 " + region + " \u2014 "
    d.text((tx, ty), prefix, font=fnt(BOLD, 15), fill=GOLD)
    rw = d.textlength(prefix, font=fnt(BOLD, 15))
    lines = wrap(d, text, fnt(REG, 15), TCOL_W - rw - 4)[:2]
    for j, ln in enumerate(lines):
        d.text((tx + rw, ty + j * 19), ln, font=fnt(REG, 15),
               fill=(235, 238, 244))

# ---------------- footer ----------------
fy = TICK_TOP + TICK_H + 12
d.line([MARGIN, fy, W - MARGIN, fy], fill=(180, 175, 160), width=2)
d.text((512, fy + 10),
       "Sources: Reuters \u2022 AP \u2022 Xinhua \u2022 Yonhap \u2014 all reported 25 November 2026",
       font=fnt(BOLD, 18), fill=MUTED, anchor="ma")

img.save("/home/hatch/workspace/makefun/news-image-20261125/entry.png",
         optimize=True)
print("saved entry.png")
