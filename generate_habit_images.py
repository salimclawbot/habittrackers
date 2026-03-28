#!/usr/bin/env python3
"""Generate 9 professional images for 'How to Break a Bad Habit Permanently' article."""

from PIL import Image, ImageDraw, ImageFont
import math
import os

OUT = "/Users/openclaw/.openclaw/workspace-philly/habittracker-site/public/images/articles"
W, H = 1280, 720

# Fonts
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BLACK = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
FONT_ROUNDED = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"

# Colors
TEAL = (0, 172, 163)
TEAL_DARK = (0, 128, 120)
TEAL_DEEP = (0, 90, 85)
ORANGE = (245, 158, 66)
ORANGE_WARM = (240, 130, 50)
ORANGE_DEEP = (220, 100, 30)
WHITE = (255, 255, 255)
OFF_WHITE = (248, 249, 250)
DARK = (33, 37, 41)
DARK_BLUE = (25, 42, 65)
SLATE = (70, 80, 95)
LIGHT_GRAY = (230, 235, 240)
CORAL = (235, 87, 87)
GREEN = (46, 184, 114)
PURPLE = (130, 80, 200)
LIGHT_TEAL = (220, 245, 243)
SOFT_BLUE = (100, 150, 220)


def font(size, bold=True, black=False, rounded=False):
    if black:
        return ImageFont.truetype(FONT_BLACK, size)
    if rounded:
        return ImageFont.truetype(FONT_ROUNDED, size)
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def gradient_bg(draw, color1, color2, vertical=True):
    """Draw a smooth gradient background."""
    for i in range(H if vertical else W):
        ratio = i / (H if vertical else W)
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        if vertical:
            draw.line([(0, i), (W, i)], fill=(r, g, b))
        else:
            draw.line([(i, 0), (i, H)], fill=(r, g, b))


def gradient_rect(draw, box, color1, color2, vertical=True):
    """Draw a gradient-filled rectangle."""
    x0, y0, x1, y1 = box
    steps = (y1 - y0) if vertical else (x1 - x0)
    for i in range(int(steps)):
        ratio = i / steps
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        if vertical:
            draw.line([(x0, y0 + i), (x1, y0 + i)], fill=(r, g, b))
        else:
            draw.line([(x0 + i, y0), (x0 + i, y1)], fill=(r, g, b))


def draw_rounded_rect(draw, box, radius, fill, outline=None, width=0):
    """Draw a rounded rectangle."""
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_arrow(draw, start, end, color, width=3, head_size=12):
    """Draw an arrow from start to end."""
    draw.line([start, end], fill=color, width=width)
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = math.sqrt(dx*dx + dy*dy)
    if length == 0:
        return
    udx, udy = dx/length, dy/length
    px, py = -udy, udx
    tip = end
    left = (tip[0] - head_size*udx + head_size*0.5*px,
            tip[1] - head_size*udy + head_size*0.5*py)
    right = (tip[0] - head_size*udx - head_size*0.5*px,
             tip[1] - head_size*udy - head_size*0.5*py)
    draw.polygon([tip, left, right], fill=color)


def draw_curved_arrow(draw, cx, cy, radius, start_angle, end_angle, color, width=3, head_size=10):
    """Draw a curved arrow along an arc."""
    draw.arc([cx-radius, cy-radius, cx+radius, cy+radius],
             start=start_angle, end=end_angle, fill=color, width=width)
    end_rad = math.radians(end_angle)
    ex = cx + radius * math.cos(end_rad)
    ey = cy + radius * math.sin(end_rad)
    tangent_angle = end_rad + math.pi/2
    tip_x = ex + head_size * math.cos(tangent_angle)
    tip_y = ey + head_size * math.sin(tangent_angle)
    left = (ex + head_size*0.6 * math.cos(end_rad),
            ey + head_size*0.6 * math.sin(end_rad))
    right = (ex - head_size*0.6 * math.cos(end_rad),
             ey - head_size*0.6 * math.sin(end_rad))
    draw.polygon([(tip_x, tip_y), left, right], fill=color)


def centered_text(draw, text, y, f, fill=WHITE):
    """Draw horizontally centered text."""
    bbox = draw.textbbox((0, 0), text, font=f)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) / 2, y), text, font=f, fill=fill)


def draw_circle(draw, cx, cy, r, fill=None, outline=None, width=2):
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=fill, outline=outline, width=width)


def draw_star(draw, cx, cy, r, fill):
    """Draw a simple 5-point star."""
    points = []
    for i in range(10):
        angle = math.radians(i * 36 - 90)
        rad = r if i % 2 == 0 else r * 0.4
        points.append((cx + rad * math.cos(angle), cy + rad * math.sin(angle)))
    draw.polygon(points, fill=fill)


def draw_check(draw, cx, cy, size, color, width=3):
    """Draw a checkmark."""
    draw.line([(cx - size*0.4, cy), (cx - size*0.1, cy + size*0.3)], fill=color, width=width)
    draw.line([(cx - size*0.1, cy + size*0.3), (cx + size*0.4, cy - size*0.3)], fill=color, width=width)


def draw_x_mark(draw, cx, cy, size, color, width=3):
    """Draw an X mark."""
    draw.line([(cx-size, cy-size), (cx+size, cy+size)], fill=color, width=width)
    draw.line([(cx+size, cy-size), (cx-size, cy+size)], fill=color, width=width)


def add_watermark(draw):
    """Add subtle site branding."""
    f = font(16, bold=False)
    draw.text((W - 200, H - 30), "habittracker.site", font=f, fill=(180, 180, 180))


def add_decorative_dots(draw, color, alpha=60):
    """Add decorative dot pattern."""
    dot_color = (*color[:3], alpha) if len(color) == 4 else color
    for x in range(50, W, 80):
        for y in range(50, H, 80):
            if (x + y) % 160 == 0:
                draw.ellipse([x-2, y-2, x+2, y+2], fill=dot_color)


# ─── IMAGE 1: Hero ───
def create_hero():
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, DARK_BLUE, TEAL_DEEP)

    # Decorative geometric shapes
    for i in range(0, W, 120):
        for j in range(0, H, 120):
            if (i + j) % 240 == 0:
                draw.ellipse([i-3, j-3, i+3, j+3], fill=(0, 100, 95))

    # Top accent bar
    gradient_rect(draw, (0, 0, W, 6), ORANGE, TEAL)

    # Central content area with subtle tinted background
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.rounded_rectangle((100, 140, W-100, 580), radius=20, fill=(255, 255, 255, 18))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Badge
    badge_text = "COMPLETE GUIDE"
    bf = font(14)
    bb = draw.textbbox((0, 0), badge_text, font=bf)
    bw = bb[2] - bb[0]
    bx = (W - bw) / 2 - 16
    draw_rounded_rect(draw, (bx, 175, bx + bw + 32, 205), 12, fill=ORANGE)
    centered_text(draw, badge_text, 180, bf, DARK)

    # Main title
    title_f = font(52, black=True)
    centered_text(draw, "How to Break a", 230, title_f, WHITE)
    centered_text(draw, "Bad Habit Permanently", 295, title_f, ORANGE)

    # Divider line
    draw.line([(440, 375), (840, 375)], fill=TEAL, width=3)

    # Subtitle
    sub_f = font(22, bold=False)
    centered_text(draw, "Science-Backed Strategies That Actually Work", 400, sub_f, LIGHT_GRAY)

    # Bottom icons row
    icons_y = 470
    items = ["Neuroscience", "30-Day Plan", "Proven Methods"]
    icon_spacing = 300
    start_x = (W - icon_spacing * 2) / 2

    for i, item in enumerate(items):
        ix = start_x + i * icon_spacing
        draw_circle(draw, int(ix), icons_y, 22, fill=TEAL_DARK, outline=TEAL, width=2)
        draw_check(draw, int(ix), icons_y, 18, WHITE, width=3)
        tf = font(16, bold=False)
        tb = draw.textbbox((0, 0), item, font=tf)
        tw = tb[2] - tb[0]
        draw.text((ix - tw/2, icons_y + 32), item, font=tf, fill=LIGHT_GRAY)

    add_watermark(draw)
    img.save(os.path.join(OUT, "how-to-break-bad-habit-permanently-hero.jpg"), quality=92)
    print("1/9 Hero created")


# ─── IMAGE 2: Habit Loop ───
def create_habit_loop():
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, OFF_WHITE, LIGHT_TEAL)

    # Title area
    gradient_rect(draw, (0, 0, W, 90), DARK_BLUE, TEAL_DEEP)
    centered_text(draw, "The Habit Loop: Understanding Your Triggers", 25, font(32, black=True), WHITE)

    # Central circle (the loop)
    cx, cy = 640, 400
    loop_r = 170

    # Draw the circular path (dashed effect with arcs)
    for angle in range(0, 360, 4):
        if angle % 8 < 4:
            rad = math.radians(angle)
            rad2 = math.radians(angle + 3)
            x1 = cx + loop_r * math.cos(rad)
            y1 = cy + loop_r * math.sin(rad)
            x2 = cx + loop_r * math.cos(rad2)
            y2 = cy + loop_r * math.sin(rad2)
            draw.line([(x1, y1), (x2, y2)], fill=(90, 100, 110), width=2)

    # Three nodes on the loop
    nodes = [
        (270, "CUE", "Trigger", CORAL, (235, 67, 67)),
        (30, "ROUTINE", "Behavior", TEAL, TEAL_DARK),
        (150, "REWARD", "Payoff", ORANGE, ORANGE_DEEP),
    ]

    for angle_deg, label, sublabel, color, dark_color in nodes:
        rad = math.radians(angle_deg)
        nx = cx + loop_r * math.cos(rad)
        ny = cy + loop_r * math.sin(rad)

        # Node circle with shadow
        draw.ellipse([nx-52, ny-48, nx+52, ny+56], fill=(200, 210, 200))
        draw_circle(draw, int(nx), int(ny), 48, fill=color, outline=dark_color, width=3)

        # Label
        lf = font(18, black=True)
        lb = draw.textbbox((0, 0), label, font=lf)
        lw = lb[2] - lb[0]
        draw.text((nx - lw/2, ny - 14), label, font=lf, fill=WHITE)

        # Sublabel below circle
        sf = font(15, bold=False)
        sb = draw.textbbox((0, 0), sublabel, font=sf)
        sw = sb[2] - sb[0]
        draw.text((nx - sw/2, ny + 58), sublabel, font=sf, fill=SLATE)

    # Draw curved arrows between nodes
    arrow_angles = [(290, 20), (50, 140), (170, 260)]
    for start_a, end_a in arrow_angles:
        draw.arc([cx-loop_r-8, cy-loop_r-8, cx+loop_r+8, cy+loop_r+8],
                 start=start_a, end=end_a, fill=SLATE, width=3)
        # Arrowhead at end
        end_rad = math.radians(end_a)
        ex = cx + (loop_r + 8) * math.cos(end_rad)
        ey = cy + (loop_r + 8) * math.sin(end_rad)
        tang = end_rad + math.pi/2
        tip = (ex + 14*math.cos(tang), ey + 14*math.sin(tang))
        left = (ex + 8*math.cos(end_rad), ey + 8*math.sin(end_rad))
        right = (ex - 8*math.cos(end_rad), ey - 8*math.sin(end_rad))
        draw.polygon([tip, left, right], fill=SLATE)

    # Center text
    cf = font(16, rounded=True)
    centered_label = "HABIT"
    cb = draw.textbbox((0, 0), centered_label, font=cf)
    cw = cb[2] - cb[0]
    draw.text((cx - cw/2, cy - 12), centered_label, font=cf, fill=SLATE)
    cf2 = font(14, rounded=True)
    centered_label2 = "LOOP"
    cb2 = draw.textbbox((0, 0), centered_label2, font=cf2)
    cw2 = cb2[2] - cb2[0]
    draw.text((cx - cw2/2, cy + 8), centered_label2, font=cf2, fill=SLATE)

    # Key insight box at bottom
    draw_rounded_rect(draw, (200, 610, W-200, 680), 12, fill=DARK_BLUE)
    insight_f = font(17, bold=False)
    centered_text(draw, "KEY: To break a habit, disrupt the loop by changing the routine", 630, insight_f, WHITE)

    add_watermark(draw)
    img.save(os.path.join(OUT, "how-to-break-bad-habit-permanently-habit-loop.jpg"), quality=92)
    print("2/9 Habit Loop created")


# ─── IMAGE 3: Habit Replacement ───
def create_replacement():
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, OFF_WHITE, (240, 248, 245))

    # Title bar
    gradient_rect(draw, (0, 0, W, 90), TEAL_DEEP, TEAL)
    centered_text(draw, "The Habit Replacement Method", 25, font(34, black=True), WHITE)

    # Left side - Old Habit (red tones)
    left_x = 180
    draw_rounded_rect(draw, (60, 130, 380, 600), 16, fill=WHITE, outline=(235, 200, 200), width=2)

    # Red header
    draw_rounded_rect(draw, (60, 130, 380, 195), 16, fill=CORAL)
    draw.rectangle((60, 170, 380, 195), fill=CORAL)  # square off bottom corners
    old_f = font(22, black=True)
    ob = draw.textbbox((0, 0), "OLD HABIT", font=old_f)
    ow = ob[2] - ob[0]
    draw.text((left_x - ow/2, 148, ), "OLD HABIT", font=old_f, fill=WHITE)

    # X icon
    draw_circle(draw, left_x, 260, 35, fill=(255, 230, 230), outline=CORAL, width=2)
    draw_x_mark(draw, left_x, 260, 15, CORAL, width=4)

    old_habits = ["Stress eating", "Phone scrolling", "Nail biting", "Procrastinating"]
    for i, h in enumerate(old_habits):
        y = 320 + i * 55
        draw.ellipse([110, y+3, 120, y+13], fill=CORAL)
        draw.text((135, y-4), h, font=font(18, bold=False), fill=SLATE)

    # Arrow in center
    arrow_cx = W // 2
    draw_rounded_rect(draw, (arrow_cx - 70, 340, arrow_cx + 70, 400), 25, fill=TEAL)
    af = font(16, black=True)
    ab = draw.textbbox((0, 0), "REPLACE", font=af)
    aw = ab[2] - ab[0]
    draw.text((arrow_cx - aw/2, 352), "REPLACE", font=af, fill=WHITE)
    # Arrow tips
    draw_arrow(draw, (arrow_cx + 70, 370), (arrow_cx + 100, 370), WHITE, width=4, head_size=14)
    draw_arrow(draw, (arrow_cx - 70, 370), (arrow_cx - 100, 370), WHITE, width=4, head_size=14)

    # Right side - New Habit (green tones)
    right_x = W - 180
    draw_rounded_rect(draw, (W-380, 130, W-60, 600), 16, fill=WHITE, outline=(200, 235, 210), width=2)

    # Green header
    draw_rounded_rect(draw, (W-380, 130, W-60, 195), 16, fill=GREEN)
    draw.rectangle((W-380, 170, W-60, 195), fill=GREEN)
    nf = font(22, black=True)
    nb = draw.textbbox((0, 0), "NEW HABIT", font=nf)
    nw = nb[2] - nb[0]
    draw.text((right_x - nw/2, 148), "NEW HABIT", font=nf, fill=WHITE)

    # Check icon
    draw_circle(draw, right_x, 260, 35, fill=(220, 245, 225), outline=GREEN, width=2)
    draw_check(draw, right_x, 260, 30, GREEN, width=4)

    new_habits = ["Healthy snacking", "Reading a book", "Deep breathing", "2-min quick task"]
    for i, h in enumerate(new_habits):
        y = 320 + i * 55
        draw.ellipse([W-330, y+3, W-320, y+13], fill=GREEN)
        draw.text((W-305, y-4), h, font=font(18, bold=False), fill=SLATE)

    # Bottom tip
    draw_rounded_rect(draw, (150, 625, W-150, 690), 12, fill=DARK_BLUE)
    centered_text(draw, "Same cue + same reward = new healthy routine", 642, font(18), WHITE)

    add_watermark(draw)
    img.save(os.path.join(OUT, "how-to-break-bad-habit-permanently-replacement.jpg"), quality=92)
    print("3/9 Replacement created")


# ─── IMAGE 4: Environment Design ───
def create_environment():
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, DARK_BLUE, (20, 60, 80))

    # Title
    centered_text(draw, "Environment Design", 30, font(40, black=True), WHITE)
    centered_text(draw, "Remove Triggers, Reshape Your Space", 85, font(20, bold=False), LIGHT_GRAY)

    # Divider
    draw.line([(440, 125), (840, 125)], fill=TEAL, width=2)

    # Three columns with icons
    strategies = [
        ("REMOVE", "Triggers", [
            "Hide junk food",
            "Delete social apps",
            "Remove ashtrays",
        ], CORAL),
        ("REDESIGN", "Your Space", [
            "Prep healthy snacks",
            "Set up gym bag",
            "Organize workspace",
        ], TEAL),
        ("ADD", "Friction", [
            "Use website blocker",
            "Keep phone away",
            "Set screen limits",
        ], ORANGE),
    ]

    col_w = 340
    start_x = 70

    for i, (title, subtitle, items, color) in enumerate(strategies):
        x = start_x + i * (col_w + 30)
        cx = x + col_w // 2

        # Card background
        draw_rounded_rect(draw, (x, 155, x + col_w, 650), 16, fill=(35, 52, 72))
        draw_rounded_rect(draw, (x, 155, x + col_w, 650), 16, fill=None, outline=(55, 68, 85), width=1)

        # Icon area
        draw_circle(draw, cx, 220, 40, fill=color)

        if i == 0:  # X for remove
            draw_x_mark(draw, cx, 220, 16, WHITE, width=4)
        elif i == 1:  # Gear-like for redesign
            draw_circle(draw, cx, 220, 18, outline=WHITE, width=3)
            for angle in range(0, 360, 45):
                rad = math.radians(angle)
                draw.line([(cx + 14*math.cos(rad), 220 + 14*math.sin(rad)),
                           (cx + 22*math.cos(rad), 220 + 22*math.sin(rad))], fill=WHITE, width=3)
        else:  # Shield for friction
            points = [(cx, 198), (cx+22, 208), (cx+18, 238), (cx, 248), (cx-18, 238), (cx-22, 208)]
            draw.polygon(points, outline=WHITE, fill=None)
            draw.line([(cx, 210), (cx, 240)], fill=WHITE, width=2)
            draw.line([(cx-10, 225), (cx+10, 225)], fill=WHITE, width=2)

        # Title
        tf = font(22, black=True)
        tb = draw.textbbox((0, 0), title, font=tf)
        tw = tb[2] - tb[0]
        draw.text((cx - tw/2, 275), title, font=tf, fill=color)

        # Subtitle
        sf = font(16, bold=False)
        sb = draw.textbbox((0, 0), subtitle, font=sf)
        sw = sb[2] - sb[0]
        draw.text((cx - sw/2, 305), subtitle, font=sf, fill=LIGHT_GRAY)

        # Divider
        draw.line([(x + 40, 340), (x + col_w - 40, 340)], fill=color, width=1)

        # Items
        for j, item in enumerate(items):
            y = 365 + j * 70
            # Bullet circle
            draw_circle(draw, x + 40, y + 10, 8, fill=color)
            draw_check(draw, x + 40, y + 10, 8, WHITE, width=2)
            draw.text((x + 60, y - 2), item, font=font(17, bold=False), fill=WHITE)

    add_watermark(draw)
    img.save(os.path.join(OUT, "how-to-break-bad-habit-permanently-environment.jpg"), quality=92)
    print("4/9 Environment created")


# ─── IMAGE 5: Accountability ───
def create_accountability():
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, OFF_WHITE, (245, 240, 230))

    # Title bar
    gradient_rect(draw, (0, 0, W, 90), TEAL_DEEP, TEAL)
    centered_text(draw, "Build Your Accountability System", 25, font(34, black=True), WHITE)

    # Three pillars
    pillars = [
        ("Accountability\nPartner", TEAL, [
            "Share your goals",
            "Weekly check-ins",
            "Honest feedback",
        ]),
        ("Habit\nTracking", ORANGE, [
            "Daily logging",
            "Streak counting",
            "Progress reviews",
        ]),
        ("Community\nSupport", PURPLE, [
            "Join groups",
            "Share wins",
            "Learn from others",
        ]),
    ]

    for i, (title, color, items) in enumerate(pillars):
        x = 80 + i * 400
        cx = x + 170

        # Card
        draw_rounded_rect(draw, (x, 120, x + 340, 620), 16, fill=WHITE, outline=LIGHT_GRAY, width=1)

        # Icon
        draw_circle(draw, cx, 195, 45, fill=color)

        if i == 0:  # People icon
            draw_circle(draw, cx, 183, 12, fill=WHITE)
            draw.arc([cx-20, 193, cx+20, 220], 0, 180, fill=WHITE, width=3)
            # Second person
            draw_circle(draw, cx+18, 187, 8, fill=WHITE)
            draw.arc([cx+4, 197, cx+32, 218], 0, 180, fill=WHITE, width=2)
        elif i == 1:  # Chart icon
            draw.rectangle([cx-18, 185, cx-8, 205], fill=WHITE)
            draw.rectangle([cx-5, 175, cx+5, 205], fill=WHITE)
            draw.rectangle([cx+8, 190, cx+18, 205], fill=WHITE)
        else:  # Globe/community icon
            draw_circle(draw, cx, 195, 20, outline=WHITE, width=2)
            draw.line([(cx-20, 195), (cx+20, 195)], fill=WHITE, width=2)
            draw.line([(cx, 175), (cx, 215)], fill=WHITE, width=2)
            draw.arc([cx-8, 175, cx+8, 215], 0, 360, fill=WHITE, width=1)

        # Title
        lines = title.split("\n")
        for li, line in enumerate(lines):
            tf = font(22, black=True)
            tb = draw.textbbox((0, 0), line, font=tf)
            tw = tb[2] - tb[0]
            draw.text((cx - tw/2, 255 + li * 30), line, font=tf, fill=DARK)

        # Divider
        draw.line([(x + 40, 330), (x + 300, 330)], fill=color, width=2)

        # Items with numbers
        for j, item in enumerate(items):
            y = 355 + j * 70
            # Number circle
            draw_circle(draw, x + 45, y + 12, 16, fill=color)
            nf = font(14, black=True)
            nb = draw.textbbox((0, 0), str(j+1), font=nf)
            nw = nb[2] - nb[0]
            draw.text((x + 45 - nw/2, y + 2), str(j+1), font=nf, fill=WHITE)
            draw.text((x + 72, y), item, font=font(17, bold=False), fill=SLATE)

    # Bottom bar with stat
    draw_rounded_rect(draw, (200, 640, W-200, 695), 12, fill=DARK_BLUE)
    centered_text(draw, "People with accountability partners are 65% more likely to succeed",
                  655, font(16, bold=False), WHITE)

    add_watermark(draw)
    img.save(os.path.join(OUT, "how-to-break-bad-habit-permanently-accountability.jpg"), quality=92)
    print("5/9 Accountability created")


# ─── IMAGE 6: 30-Day Plan ───
def create_30day():
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, DARK_BLUE, (15, 35, 55))

    # Title
    centered_text(draw, "Your 30-Day Habit Breaking Plan", 20, font(36, black=True), WHITE)
    draw.line([(400, 75), (880, 75)], fill=ORANGE, width=3)

    # Timeline bar
    bar_y = 120
    bar_h = 8
    gradient_rect(draw, (100, bar_y, W-100, bar_y + bar_h), CORAL, GREEN, vertical=False)

    # Week markers on timeline
    weeks_x = [100, 370, 640, 910, W-100]
    for x in weeks_x:
        draw.line([(x, bar_y - 5), (x, bar_y + bar_h + 5)], fill=WHITE, width=2)

    # Four week cards
    weeks = [
        ("WEEK 1", "Days 1-7", "AWARENESS", CORAL, [
            "Identify all triggers",
            "Log every urge",
            "Set replacement habits",
            "Tell someone your plan",
        ]),
        ("WEEK 2", "Days 8-14", "ACTION", ORANGE, [
            "Implement replacements",
            "Design environment",
            "Practice mindfulness",
            "Track daily progress",
        ]),
        ("WEEK 3", "Days 15-21", "RESILIENCE", TEAL, [
            "Push through cravings",
            "Review what's working",
            "Adjust strategies",
            "Celebrate small wins",
        ]),
        ("WEEK 4", "Days 22-30", "SOLIDIFY", GREEN, [
            "Build on momentum",
            "Plan for future triggers",
            "Create long-term systems",
            "Lock in new identity",
        ]),
    ]

    card_w = 270
    gap = 20
    total_w = 4 * card_w + 3 * gap
    start_x = (W - total_w) / 2

    for i, (week, days, phase, color, items) in enumerate(weeks):
        x = start_x + i * (card_w + gap)
        y_top = 155

        # Card
        draw_rounded_rect(draw, (x, y_top, x + card_w, 680), 14, fill=(30, 48, 68))
        draw_rounded_rect(draw, (x, y_top, x + card_w, 680), 14, fill=None, outline=(50, 62, 80), width=1)

        # Week number header
        draw_rounded_rect(draw, (x, y_top, x + card_w, y_top + 55), 14, fill=color)
        draw.rectangle((x, y_top + 30, x + card_w, y_top + 55), fill=color)

        wf = font(20, black=True)
        wb = draw.textbbox((0, 0), week, font=wf)
        ww = wb[2] - wb[0]
        cx = x + card_w / 2
        draw.text((cx - ww/2, y_top + 10), week, font=wf, fill=WHITE)

        # Days
        df = font(14, bold=False)
        db = draw.textbbox((0, 0), days, font=df)
        dw = db[2] - db[0]
        draw.text((cx - dw/2, y_top + 70), days, font=df, fill=LIGHT_GRAY)

        # Phase badge
        pf = font(15, black=True)
        pb = draw.textbbox((0, 0), phase, font=pf)
        pw = pb[2] - pb[0]
        draw_rounded_rect(draw, (cx - pw/2 - 14, y_top + 100, cx + pw/2 + 14, y_top + 130), 10, fill=color)
        draw.text((cx - pw/2, y_top + 103), phase, font=pf, fill=WHITE)

        # Divider
        draw.line([(x + 20, y_top + 150), (x + card_w - 20, y_top + 150)], fill=color, width=1)

        # Items
        for j, item in enumerate(items):
            iy = y_top + 170 + j * 60
            # Small check circle
            draw_circle(draw, int(x + 28), iy + 10, 9, fill=color)
            draw_check(draw, int(x + 28), iy + 10, 8, WHITE, width=2)
            # Wrap text if needed
            draw.text((x + 46, iy - 2), item, font=font(14, bold=False), fill=WHITE)

    add_watermark(draw)
    img.save(os.path.join(OUT, "how-to-break-bad-habit-permanently-30day-plan.jpg"), quality=92)
    print("6/9 30-Day Plan created")


# ─── IMAGE 7: Mindfulness ───
def create_mindfulness():
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)

    # Calm gradient - deep to lighter
    gradient_bg(draw, (25, 50, 65), (45, 100, 110))

    # Subtle radial glow effect in center
    for r in range(300, 0, -2):
        alpha = int(15 * (1 - r/300))
        color = (80 + alpha*3, 180 + alpha*2, 170 + alpha*2)
        draw.ellipse([W//2-r, H//2-r-30, W//2+r, H//2+r-30], outline=color)

    # Concentric calm circles
    for r in [180, 140, 100, 60]:
        draw.ellipse([W//2-r, 320-r, W//2+r, 320+r],
                     outline=(0, int(80 + (180-r)*0.5), int(75 + (180-r)*0.5)), width=2)

    # Center meditation symbol (simple person silhouette)
    cx, cy = W//2, 300
    # Head
    draw_circle(draw, cx, cy - 30, 14, fill=TEAL)
    # Body (triangle)
    draw.polygon([(cx, cy - 12), (cx - 28, cy + 30), (cx + 28, cy + 30)], fill=TEAL)
    # Legs (crossed)
    draw.arc([cx-30, cy+15, cx+30, cy+45], 0, 180, fill=TEAL, width=4)

    # Title
    centered_text(draw, "Mindfulness & Self-Awareness", 450, font(38, black=True), WHITE)

    # Subtitle
    centered_text(draw, "Observe your urges without acting on them", 505, font(20, bold=False), LIGHT_GRAY)

    # Three technique cards at bottom
    techniques = [
        ("Pause & Breathe", "Notice the urge.\nTake 5 deep breaths."),
        ("Name the Feeling", "Label your emotion.\nReduce its power."),
        ("Surf the Urge", "Ride it like a wave.\nIt will pass in minutes."),
    ]

    card_w = 330
    gap = 30
    start_x = (W - 3*card_w - 2*gap) / 2

    for i, (title, desc) in enumerate(techniques):
        x = start_x + i * (card_w + gap)
        draw_rounded_rect(draw, (x, 560, x+card_w, 680), 12, fill=(38, 58, 75))
        draw_rounded_rect(draw, (x, 560, x+card_w, 680), 12, fill=None, outline=TEAL, width=1)

        # Number
        nf = font(16, black=True)
        draw_circle(draw, int(x + 28), 582, 14, fill=TEAL)
        nb = draw.textbbox((0, 0), str(i+1), font=nf)
        nw = nb[2] - nb[0]
        draw.text((x + 28 - nw/2, 572), str(i+1), font=nf, fill=WHITE)

        tf = font(18, black=True)
        draw.text((x + 52, 572), title, font=tf, fill=WHITE)

        lines = desc.split("\n")
        for li, line in enumerate(lines):
            draw.text((x + 20, 610 + li * 22), line, font=font(14, bold=False), fill=LIGHT_GRAY)

    add_watermark(draw)
    img.save(os.path.join(OUT, "how-to-break-bad-habit-permanently-mindfulness.jpg"), quality=92)
    print("7/9 Mindfulness created")


# ─── IMAGE 8: Neuroscience ───
def create_neuroscience():
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, (15, 20, 40), (30, 50, 75))

    # Title
    centered_text(draw, "The Neuroscience of Habits", 25, font(38, black=True), WHITE)
    centered_text(draw, "How Neural Pathways Form and Change", 78, font(18, bold=False), LIGHT_GRAY)

    # Draw a brain outline (simplified)
    brain_cx, brain_cy = 350, 370
    # Left hemisphere
    draw.arc([brain_cx - 150, brain_cy - 130, brain_cx + 10, brain_cy + 130],
             90, 270, fill=TEAL, width=3)
    # Right hemisphere
    draw.arc([brain_cx - 10, brain_cy - 130, brain_cx + 150, brain_cy + 130],
             270, 90, fill=TEAL, width=3)
    # Top connection
    draw.arc([brain_cx - 80, brain_cy - 160, brain_cx + 80, brain_cy - 80],
             200, 340, fill=TEAL, width=3)
    # Brain folds
    draw.arc([brain_cx - 100, brain_cy - 100, brain_cx - 20, brain_cy],
             0, 180, fill=(0, 130, 123), width=2)
    draw.arc([brain_cx + 20, brain_cy - 100, brain_cx + 100, brain_cy],
             0, 180, fill=(0, 130, 123), width=2)
    draw.arc([brain_cx - 80, brain_cy - 40, brain_cx + 0, brain_cy + 60],
             180, 360, fill=(0, 130, 123), width=2)
    draw.arc([brain_cx + 0, brain_cy - 40, brain_cx + 80, brain_cy + 60],
             180, 360, fill=(0, 130, 123), width=2)

    # Neural pathway dots
    import random
    random.seed(42)
    nodes = []
    for _ in range(25):
        nx = brain_cx + random.randint(-120, 120)
        ny = brain_cy + random.randint(-110, 110)
        r = random.randint(3, 7)
        color = ORANGE if random.random() > 0.6 else TEAL
        draw_circle(draw, nx, ny, r, fill=color)
        nodes.append((nx, ny))

    # Connect some nodes
    for i in range(len(nodes) - 1):
        if random.random() > 0.5:
            x1, y1 = nodes[i]
            x2, y2 = nodes[i+1]
            draw.line([(x1, y1), (x2, y2)], fill=(0, 90, 85), width=1)

    # Right side - key concepts
    concepts = [
        ("Basal Ganglia", "Controls habit formation\nand automatic behaviors", TEAL),
        ("Prefrontal Cortex", "Manages decision-making\nand conscious control", ORANGE),
        ("Dopamine Pathway", "Reward system that\nreinforces behaviors", PURPLE),
        ("Neuroplasticity", "Brain's ability to rewire\nand form new pathways", GREEN),
    ]

    rx = 650
    for i, (title, desc, color) in enumerate(concepts):
        y = 150 + i * 130

        # Card
        draw_rounded_rect(draw, (rx, y, W - 60, y + 110), 12, fill=(30, 48, 68))
        draw.line([(rx, y + 6), (rx, y + 104)], fill=color, width=4)

        # Color dot
        draw_circle(draw, rx + 24, y + 22, 8, fill=color)

        # Title
        draw.text((rx + 42, y + 12), title, font=font(19, black=True), fill=WHITE)

        # Description
        lines = desc.split("\n")
        for li, line in enumerate(lines):
            draw.text((rx + 22, y + 45 + li * 22), line, font=font(14, bold=False), fill=LIGHT_GRAY)

    # Bottom insight
    draw_rounded_rect(draw, (100, 650, W-100, 700), 10, fill=TEAL_DEEP)
    centered_text(draw, "It takes an average of 66 days for a new behavior to become automatic",
                  660, font(16, bold=False), WHITE)

    add_watermark(draw)
    img.save(os.path.join(OUT, "how-to-break-bad-habit-permanently-neuroscience.jpg"), quality=92)
    print("8/9 Neuroscience created")


# ─── IMAGE 9: Video Thumbnail ───
def create_video_thumb():
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    gradient_bg(draw, DARK_BLUE, TEAL_DEEP)

    # Background pattern - subtle grid
    for x in range(0, W, 60):
        draw.line([(x, 0), (x, H)], fill=(30, 48, 70), width=1)
    for y in range(0, H, 60):
        draw.line([(0, y), (W, y)], fill=(30, 48, 70), width=1)

    # Large play button
    play_cx, play_cy = W // 2, 300
    # Outer glow rings
    for r in [95, 85, 75]:
        brightness = 60 + int(40 * (95 - r) / 20)
        draw_circle(draw, play_cx, play_cy, r, outline=(brightness, int(brightness*0.6), 20), width=2)

    # Play button circle
    draw_circle(draw, play_cx, play_cy, 65, fill=ORANGE, outline=ORANGE_WARM, width=3)

    # Play triangle
    play_points = [
        (play_cx - 15, play_cy - 28),
        (play_cx - 15, play_cy + 28),
        (play_cx + 25, play_cy),
    ]
    draw.polygon(play_points, fill=WHITE)

    # Title
    centered_text(draw, "WATCH", 420, font(22, black=True), ORANGE)
    centered_text(draw, "Your Habit-Breaking Guide", 460, font(40, black=True), WHITE)

    # Subtitle
    centered_text(draw, "Step-by-step strategies to break any bad habit for good",
                  520, font(20, bold=False), LIGHT_GRAY)

    # Duration badge
    dur_text = "8:42"
    draw_rounded_rect(draw, (W-140, 20, W-40, 55), 8, fill=(20, 20, 20))
    df = font(18)
    db = draw.textbbox((0, 0), dur_text, font=df)
    dw = db[2] - db[0]
    draw.text((W - 90 - dw/2, 27), dur_text, font=df, fill=WHITE)

    # Bottom progress bar
    draw.rectangle([0, H-6, W, H], fill=(60, 60, 60))
    draw.rectangle([0, H-6, int(W*0.35), H], fill=ORANGE)

    # Corner branding
    draw_rounded_rect(draw, (30, 25, 210, 58), 8, fill=TEAL)
    draw.text((45, 30), "habittracker.site", font=font(16), fill=WHITE)

    # Bottom icons
    items_y = 600
    items = [("Science-Based", TEAL), ("Step-by-Step", ORANGE), ("Free Guide", GREEN)]
    spacing = 320
    sx = (W - spacing * 2) / 2

    for i, (label, color) in enumerate(items):
        ix = sx + i * spacing
        draw_circle(draw, int(ix), items_y, 14, fill=color)
        draw_check(draw, int(ix), items_y, 12, WHITE, width=2)
        lf = font(16, bold=False)
        lb = draw.textbbox((0, 0), label, font=lf)
        lw = lb[2] - lb[0]
        draw.text((ix - lw/2, items_y + 22), label, font=lf, fill=LIGHT_GRAY)

    add_watermark(draw)
    img.save(os.path.join(OUT, "break-bad-habit-video-thumb.jpg"), quality=92)
    print("9/9 Video Thumbnail created")


# ─── Run all ───
if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print(f"Generating images to: {OUT}\n")

    create_hero()
    create_habit_loop()
    create_replacement()
    create_environment()
    create_accountability()
    create_30day()
    create_mindfulness()
    create_neuroscience()
    create_video_thumb()

    print("\nAll 9 images generated successfully!")

    # Verify
    for f in sorted(os.listdir(OUT)):
        if "break" in f.lower() or "habit-loop" in f.lower() or "replacement" in f.lower() or "environment" in f.lower() or "accountability" in f.lower() or "30day" in f.lower() or "mindfulness" in f.lower() or "neuroscience" in f.lower() or "video-thumb" in f.lower():
            size = os.path.getsize(os.path.join(OUT, f))
            print(f"  {f} ({size//1024}KB)")
