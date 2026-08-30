#!/usr/bin/env python3
"""
Challenge generator — run this to regenerate challenge.png with a new flag or key.
Output goes to ../handout/challenge.png
"""

from PIL import Image, ImageDraw
import os

FLAG = b"EH4X{png_chunk5_4r3_y0ur_fr13nd}"
XOR_KEY = 0x5A

def generate(flag: bytes = FLAG, key: int = XOR_KEY, out: str = "../handout/challenge.png"):
    # --- Decoy image ---
    img = Image.new("RGB", (400, 300), color=(30, 30, 60))
    draw = ImageDraw.Draw(img)
    draw.rectangle([20, 20, 380, 280], outline=(80, 120, 200), width=2)
    draw.text((40, 50),  "RECRUITMENT CHALLENGE #3",       fill=(180, 180, 255))
    draw.text((40, 90),  "Can you find what's hidden?",    fill=(140, 140, 200))
    draw.text((40, 130), "The image knows more than it shows.", fill=(100, 100, 160))
    draw.text((40, 200), "~ EH4X ~",                       fill=(80, 80, 140))
    draw.text((40, 240), "Good luck.",                     fill=(60, 60, 120))
    img.save(out, format="PNG")

    # --- XOR-encode flag and append after IEND ---
    encoded = bytes([b ^ key for b in flag])
    marker  = bytes([b ^ key for b in b">>HIDDEN<<"])
    payload = marker + encoded

    with open(out, "ab") as f:
        f.write(payload)

    print(f"[+] Challenge written to {out}")
    print(f"[+] Flag : {flag.decode()}")
    print(f"[+] Key  : 0x{key:02X}")

if __name__ == "__main__":
    generate()
