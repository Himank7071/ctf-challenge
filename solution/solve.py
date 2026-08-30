#!/usr/bin/env python3
# solve.py — organiser use only, do NOT distribute

with open("../handout/challenge.png", "rb") as f:
    data = f.read()

IEND = b'\x49\x45\x4e\x44\xae\x42\x60\x82'
pos  = data.find(IEND) + 8

print(f"[*] IEND ends at offset 0x{pos:04x}")

payload = data[pos:]
print(f"[*] {len(payload)} bytes after IEND: {payload.hex()}")

for key in range(256):
    dec = bytes([b ^ key for b in payload])
    if all(32 <= c < 127 for c in dec):
        print(f"[+] key=0x{key:02x} -> {dec.decode()}")
