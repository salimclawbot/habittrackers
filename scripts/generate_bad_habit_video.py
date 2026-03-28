#!/usr/bin/env python3
"""Generate animated MP4 for 'How to Break a Bad Habit Permanently' article."""

import os
import shutil
import subprocess
import tempfile
import math
from PIL import Image, ImageDraw, ImageFont

# --- Config ---
W, H = 1280, 720
FPS = 30
SLIDE_DURATION = 3.0       # seconds per slide
FADE_DURATION = 0.5        # seconds for crossfade
NUM_SLIDES = 3
OUTPUT = "/Users/openclaw/.openclaw/workspace-philly/habittracker-site/public/videos/how-to-break-bad-habit-permanently.mp4"

# Colors
TEAL_DARK = (13, 42, 52)
TEAL = (0, 150, 136)
TEAL_LIGHT = (77, 182, 172)
ORANGE = (255, 152, 0)
ORANGE_LIGHT = (255, 183, 77)
WHITE = (255, 255, 255)
LIGHT_GRAY = (220, 230, 230)
DARK_TEXT = (30, 50, 55)

# Fonts
def load_font(size, bold=False):
    paths = [
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except:
            pass
    return ImageFont.load_default()

FONT_TITLE = load_font(42, bold=True)
FONT_SUBTITLE = load_font(28, bold=True)
FONT_BODY = load_font(24)
FONT_BODY_BOLD = load_font(24, bold=True)
FONT_SMALL = load_font(20)
FONT_LARGE = load_font(52, bold=True)
FONT_ICON = load_font(36, bold=True)


def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=0):
    x0, y0, x1, y1 = xy
    r = radius
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def draw_gradient_bg(img):
    """Draw a vertical gradient background from TEAL_DARK to a slightly lighter shade."""
    draw = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        r = int(TEAL_DARK[0] * (1 - t) + 18 * t)
        g = int(TEAL_DARK[1] * (1 - t) + 60 * t)
        b = int(TEAL_DARK[2] * (1 - t) + 72 * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))


def draw_top_bar(draw):
    """Draw a subtle decorative top bar."""
    draw.rectangle([0, 0, W, 5], fill=ORANGE)


def draw_bottom_branding(draw):
    """Draw small branding at bottom."""
    text = "HabitTracker.site"
    bbox = draw.textbbox((0, 0), text, font=FONT_SMALL)
    tw = bbox[2] - bbox[0]
    draw.text((W - tw - 30, H - 35), text, fill=(100, 140, 145), font=FONT_SMALL)


def text_width(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def text_height(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[3] - bbox[1]


# ---- Slide 1: The Habit Loop ----
def draw_slide_1(progress=1.0):
    img = Image.new("RGB", (W, H))
    draw_gradient_bg(img)
    draw = ImageDraw.Draw(img)
    draw_top_bar(draw)

    # Title
    title = "The Habit Loop"
    tw = text_width(draw, title, FONT_LARGE)
    draw.text(((W - tw) // 2, 40), title, fill=ORANGE, font=FONT_LARGE)

    # Subtitle
    sub = "Understanding Why Bad Habits Stick"
    sw = text_width(draw, sub, FONT_BODY)
    draw.text(((W - sw) // 2, 105), sub, fill=LIGHT_GRAY, font=FONT_BODY)

    # Draw circular loop diagram
    cx, cy = W // 2, 390
    radius = 160

    # Three nodes at triangle points
    angles = [-90, 150, 30]  # top, bottom-left, bottom-right
    labels = ["CUE", "ROUTINE", "REWARD"]
    descriptions = ["Trigger", "Behavior", "Benefit"]
    colors = [ORANGE, TEAL_LIGHT, ORANGE_LIGHT]

    nodes = []
    for i, (angle, label, desc, color) in enumerate(zip(angles, labels, descriptions, colors)):
        rad = math.radians(angle)
        nx = cx + int(radius * math.cos(rad))
        ny = cy + int(radius * math.sin(rad))
        nodes.append((nx, ny))

        # Draw node circle
        node_r = 55
        draw_rounded_rect(draw, (nx - node_r, ny - node_r, nx + node_r, ny + node_r), radius=node_r, fill=color)

        # Label
        lw = text_width(draw, label, FONT_SUBTITLE)
        draw.text((nx - lw // 2, ny - 18), label, fill=DARK_TEXT, font=FONT_SUBTITLE)

        # Description below node
        dw = text_width(draw, desc, FONT_SMALL)
        draw.text((nx - dw // 2, ny + node_r + 8), desc, fill=LIGHT_GRAY, font=FONT_SMALL)

    # Draw arrows between nodes
    arrow_pairs = [(0, 1), (1, 2), (2, 0)]
    for (i, j) in arrow_pairs:
        x1, y1 = nodes[i]
        x2, y2 = nodes[j]
        # Shorten line to not overlap circles
        dx, dy = x2 - x1, y2 - y1
        dist = math.sqrt(dx * dx + dy * dy)
        ux, uy = dx / dist, dy / dist
        sx = x1 + ux * 60
        sy = y1 + uy * 60
        ex = x2 - ux * 60
        ey = y2 - uy * 60
        draw.line([(sx, sy), (ex, ey)], fill=WHITE, width=3)

        # Arrowhead
        arrow_len = 12
        ax = ex - ux * arrow_len + uy * 6
        ay = ey - uy * arrow_len - ux * 6
        bx = ex - ux * arrow_len - uy * 6
        by = ey - uy * arrow_len + ux * 6
        draw.polygon([(ex, ey), (ax, ay), (bx, by)], fill=WHITE)

    # Bottom text
    tip = "To break the loop, you must disrupt one element."
    tipw = text_width(draw, tip, FONT_BODY)
    draw.text(((W - tipw) // 2, H - 80), tip, fill=ORANGE_LIGHT, font=FONT_BODY)

    draw_bottom_branding(draw)
    return img


# ---- Slide 2: The Replacement Strategy ----
def draw_slide_2(progress=1.0):
    img = Image.new("RGB", (W, H))
    draw_gradient_bg(img)
    draw = ImageDraw.Draw(img)
    draw_top_bar(draw)

    # Title
    title = "The Replacement Strategy"
    tw = text_width(draw, title, FONT_LARGE)
    draw.text(((W - tw) // 2, 40), title, fill=ORANGE, font=FONT_LARGE)

    sub = "Swap, Don't Just Stop"
    sw = text_width(draw, sub, FONT_BODY)
    draw.text(((W - sw) // 2, 105), sub, fill=LIGHT_GRAY, font=FONT_BODY)

    # Left box: Old Habit (crossed out)
    left_x, box_y = 100, 180
    box_w, box_h = 440, 380

    # Old habit box
    draw_rounded_rect(draw, (left_x, box_y, left_x + box_w, box_y + box_h), radius=16, fill=(40, 20, 20), outline=(180, 60, 60), width=2)

    old_title = "OLD HABIT"
    otw = text_width(draw, old_title, FONT_SUBTITLE)
    draw.text((left_x + (box_w - otw) // 2, box_y + 20), old_title, fill=(220, 80, 80), font=FONT_SUBTITLE)

    old_habits = [
        ("Stress eating", "Emotional trigger"),
        ("Doom scrolling", "Boredom trigger"),
        ("Nail biting", "Anxiety trigger"),
    ]
    for i, (habit, trigger) in enumerate(old_habits):
        y = box_y + 75 + i * 90
        draw.text((left_x + 30, y), habit, fill=WHITE, font=FONT_BODY_BOLD)
        draw.text((left_x + 30, y + 30), trigger, fill=(160, 140, 140), font=FONT_SMALL)
        # Strikethrough
        hw = text_width(draw, habit, FONT_BODY_BOLD)
        draw.line([(left_x + 28, y + 12), (left_x + 32 + hw, y + 12)], fill=(220, 80, 80), width=2)

    # Arrow in the middle
    arrow_cx = W // 2
    arrow_cy = box_y + box_h // 2
    # Big arrow
    draw.text((arrow_cx - 15, arrow_cy - 20), "→", fill=ORANGE, font=FONT_LARGE)

    # Right box: New Habit
    right_x = W - 100 - box_w
    draw_rounded_rect(draw, (right_x, box_y, right_x + box_w, box_y + box_h), radius=16, fill=(10, 50, 40), outline=TEAL_LIGHT, width=2)

    new_title = "NEW HABIT"
    ntw = text_width(draw, new_title, FONT_SUBTITLE)
    draw.text((right_x + (box_w - ntw) // 2, box_y + 20), new_title, fill=TEAL_LIGHT, font=FONT_SUBTITLE)

    new_habits = [
        ("Drink water + walk", "Same cue, better routine"),
        ("Read 5 pages", "Same cue, better routine"),
        ("Squeeze stress ball", "Same cue, better routine"),
    ]
    for i, (habit, tip) in enumerate(new_habits):
        y = box_y + 75 + i * 90
        # Checkmark
        draw.text((right_x + 25, y - 2), "✓", fill=TEAL_LIGHT, font=FONT_BODY_BOLD)
        draw.text((right_x + 55, y), habit, fill=WHITE, font=FONT_BODY_BOLD)
        draw.text((right_x + 55, y + 30), tip, fill=(120, 170, 160), font=FONT_SMALL)

    # Bottom tip
    tip = "Keep the same cue and reward — only change the routine."
    tipw = text_width(draw, tip, FONT_BODY)
    draw.text(((W - tipw) // 2, H - 70), tip, fill=ORANGE_LIGHT, font=FONT_BODY)

    draw_bottom_branding(draw)
    return img


# ---- Slide 3: Your 30-Day Plan ----
def draw_slide_3(progress=1.0):
    img = Image.new("RGB", (W, H))
    draw_gradient_bg(img)
    draw = ImageDraw.Draw(img)
    draw_top_bar(draw)

    # Title
    title = "Your 30-Day Plan"
    tw = text_width(draw, title, FONT_LARGE)
    draw.text(((W - tw) // 2, 35), title, fill=ORANGE, font=FONT_LARGE)

    sub = "A Week-by-Week Roadmap to Freedom"
    sw = text_width(draw, sub, FONT_BODY)
    draw.text(((W - sw) // 2, 100), sub, fill=LIGHT_GRAY, font=FONT_BODY)

    weeks = [
        ("WEEK 1", "Awareness", "Track every trigger.\nLog cues in a journal.", ORANGE),
        ("WEEK 2", "Replacement", "Introduce your new\nroutine after each cue.", TEAL_LIGHT),
        ("WEEK 3", "Reinforcement", "Reward consistency.\nCelebrate small wins.", ORANGE_LIGHT),
        ("WEEK 4", "Automation", "The new habit feels\nnatural. Stay vigilant.", (130, 220, 130)),
    ]

    card_w = 260
    card_h = 310
    gap = 20
    total_w = 4 * card_w + 3 * gap
    start_x = (W - total_w) // 2
    card_y = 155

    for i, (week, phase, desc, color) in enumerate(weeks):
        x = start_x + i * (card_w + gap)

        # Card background
        draw_rounded_rect(draw, (x, card_y, x + card_w, card_y + card_h), radius=14, fill=(20, 55, 65), outline=color, width=2)

        # Week number badge
        badge_w = text_width(draw, week, FONT_SMALL) + 20
        badge_x = x + (card_w - badge_w) // 2
        draw_rounded_rect(draw, (badge_x, card_y - 2, badge_x + badge_w, card_y + 28), radius=14, fill=color)
        ww = text_width(draw, week, FONT_SMALL)
        draw.text((badge_x + (badge_w - ww) // 2, card_y + 1), week, fill=DARK_TEXT, font=FONT_SMALL)

        # Phase title
        pw = text_width(draw, phase, FONT_SUBTITLE)
        draw.text((x + (card_w - pw) // 2, card_y + 50), phase, fill=color, font=FONT_SUBTITLE)

        # Divider line
        draw.line([(x + 30, card_y + 90), (x + card_w - 30, card_y + 90)], fill=color, width=1)

        # Description (multiline)
        lines = desc.split("\n")
        for j, line in enumerate(lines):
            lw = text_width(draw, line, FONT_SMALL)
            draw.text((x + (card_w - lw) // 2, card_y + 110 + j * 28), line, fill=LIGHT_GRAY, font=FONT_SMALL)

        # Progress indicator (filled circles)
        dots_y = card_y + card_h - 50
        for d in range(4):
            dot_x = x + card_w // 2 - 30 + d * 20
            if d <= i:
                draw.ellipse((dot_x, dots_y, dot_x + 10, dots_y + 10), fill=color)
            else:
                draw.ellipse((dot_x, dots_y, dot_x + 10, dots_y + 10), outline=color, width=1)

    # Connecting arrows between cards
    for i in range(3):
        ax = start_x + (i + 1) * (card_w + gap) - gap // 2
        ay = card_y + card_h // 2
        draw.text((ax - 8, ay - 14), "›", fill=WHITE, font=FONT_SUBTITLE)

    # Bottom tip
    tip = "Consistency beats perfection. Track daily, adjust weekly."
    tipw = text_width(draw, tip, FONT_BODY)
    draw.text(((W - tipw) // 2, H - 60), tip, fill=ORANGE_LIGHT, font=FONT_BODY)

    draw_bottom_branding(draw)
    return img


def generate_video():
    tmpdir = tempfile.mkdtemp(prefix="habit_video_")
    print(f"Temp dir: {tmpdir}")

    slides = [draw_slide_1, draw_slide_2, draw_slide_3]
    slide_images = [fn() for fn in slides]

    frame_num = 0
    fade_frames = int(FADE_DURATION * FPS)
    hold_frames = int(SLIDE_DURATION * FPS) - fade_frames  # hold before starting fade

    for slide_idx in range(NUM_SLIDES):
        current = slide_images[slide_idx]

        # Hold frames (fully visible)
        for f in range(hold_frames):
            path = os.path.join(tmpdir, f"frame_{frame_num:05d}.png")
            current.save(path)
            frame_num += 1

        # Crossfade to next slide (or just hold last slide)
        if slide_idx < NUM_SLIDES - 1:
            next_img = slide_images[slide_idx + 1]
            for f in range(fade_frames):
                alpha = f / fade_frames
                blended = Image.blend(current, next_img, alpha)
                path = os.path.join(tmpdir, f"frame_{frame_num:05d}.png")
                blended.save(path)
                frame_num += 1
        else:
            # Hold last slide a bit longer
            for f in range(fade_frames):
                path = os.path.join(tmpdir, f"frame_{frame_num:05d}.png")
                current.save(path)
                frame_num += 1

    print(f"Generated {frame_num} frames")

    # Encode with ffmpeg
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    cmd = [
        "ffmpeg", "-y",
        "-framerate", str(FPS),
        "-i", os.path.join(tmpdir, "frame_%05d.png"),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "veryslow",
        "-crf", "30",
        "-movflags", "+faststart",
        "-vf", "scale=1280:720",
        OUTPUT,
    ]
    print("Running ffmpeg...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("FFMPEG STDERR:", result.stderr)
        raise RuntimeError("ffmpeg failed")

    size = os.path.getsize(OUTPUT)
    print(f"Output: {OUTPUT}")
    print(f"Size: {size} bytes ({size / 1024:.1f} KB)")

    # Cleanup
    shutil.rmtree(tmpdir)
    print("Done!")


if __name__ == "__main__":
    generate_video()
