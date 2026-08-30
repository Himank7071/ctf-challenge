# What You See Isn't All You Get

We intercepted this image from a suspicious server. Our analyst says it's "just a PNG" — but something feels off. Can you prove them wrong?

`difficulty: Medium` <br>
`author: EH4X`

## Flag
```
EH4X{png_chunk5_4r3_y0ur_fr13nd}
```

## Solution

Every PNG file formally ends at the `IEND` chunk. Image viewers stop reading there — but the file doesn't have to. Inspect the raw bytes with `xxd` and you'll find extra data after `IEND`. The payload is XOR-encoded with a single-byte key; brute-forcing all 256 keys and checking for printable ASCII output reveals the flag.
