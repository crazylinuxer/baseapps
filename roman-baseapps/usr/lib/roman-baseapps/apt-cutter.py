import sys

vers = ''
for arg in sys.argv:
    vers += arg
    vers += ' '

vers = vers.split(":")[2].split(" ")[1]

print("roman-baseapps v" + vers)
