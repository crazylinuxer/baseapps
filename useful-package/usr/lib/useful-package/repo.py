import sys

addr = ''
for arg in sys.argv:
    addr += arg
    addr += ' '
addr = addr.split("//")
addr = addr[len(addr)-1]
addr = "http://" + addr
print(addr)
