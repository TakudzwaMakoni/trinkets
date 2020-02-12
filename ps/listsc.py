#
# listsc
# by Takudzwa Makoni 2020

import sys
shortcuts = sys.argv[1]
f = open(shortcuts)
lines = f.readlines()
f.close()

header = "{0:<15}{1}".format("shortcut","directory")
print("\n\033[4m" + header + "\033[0m", "\n")
for line in lines:
    modLine = line.replace(';','')
    entries = modLine.split(':')
    print("{0:<15}{1}".format(entries[0], entries[1]),end="")
print("")
