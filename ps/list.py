# list.py by Takudzwa Makoni 2020

import sys
from os import listdir
import os.path as path

option = sys.argv[1]
directory = sys.argv[2]
entities = listdir(directory)
entities.sort(key=str.casefold)
header = "{0:<25}{1}".format("entity","type")
print("\n\033[4m" + header + "\033[0m", "\n")
for entity in entities:
    if path.isfile(path.join(directory, entity)):
        #print("file!")
        type = " file"
    elif path.isdir(path.join(directory, entity)):
        #print("directory!")
        type = " directory"
    else:
        type = "unknown"
    if option == "False":
        if entity[0] == ".":
            pass
        else:
            print("{0:<25}{1}".format(entity, type))
    else:
        print("{0:<25}{1}".format(entity, type))
print()
