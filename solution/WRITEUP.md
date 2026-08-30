# Writeup — "What You See Isn't All You Get"

## Summary
The challenge PNG has data appended after the `IEND` chunk (the formal end of any PNG file).
Image viewers ignore everything past `IEND`, but the bytes are still physically present in the file.
The hidden payload is XOR-encoded with the single-byte key `0x5A`.

## Step-by-step

**1. Notice the file is larger than expected**
```bash
wc -c challenge.png
```

**2. Find the IEND marker and see trailing bytes**
```bash
xxd challenge.png | tail -20
# Look for: 49 45 4e 44 ae 42 60 82  (IEND signature)
# Anything after that is suspicious
```

**3. Extract bytes after IEND**
```python
data = open('challenge.png', 'rb').read()
pos  = data.find(b'IEND\xaeB\x60\x82') + 8
print(data[pos:].hex())
```

**4. Brute-force XOR key (256 possibilities)**
```python
payload = data[pos:]
for key in range(256):
    dec = bytes([b ^ key for b in payload])
    if all(32 <= c < 127 for c in dec):
        print(f"key=0x{key:02x} -> {dec}")
```

Key `0x5A` produces: `>>HIDDEN<<EH4X{png_chunk5_4r3_y0ur_fr13nd}`

## Flag
```
EH4X{png_chunk5_4r3_y0ur_fr13nd}
```
