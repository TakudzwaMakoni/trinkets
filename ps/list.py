# list.py by Takudzwa Makoni 2020

import sys
import os
import datetime

option = sys.argv[1]
directory = sys.argv[2]
entities = os.listdir(directory)
entities = [ entity for entity in entities if entity[0] != "." ] if option == "False" else entities

padding = len(max(entities, key=len)) + 3
entities.sort(key=str.casefold)
header = "{0:<{4}}{1:<10}{2:<10}{3}".format("entity","type","access","modified", padding)
print("\n\033[4m" + header + "\033[0m", "\n")
for entity in entities:
    fullPath = os.path.join(directory, entity)
    read = "r" if os.access(fullPath, os.R_OK) else "-"
    write = "w" if os.access(fullPath, os.R_OK) else "-"
    execute = "x" if os.access(fullPath, os.R_OK) else "-"
    try:
        modified = datetime.datetime.fromtimestamp(os.stat(fullPath).st_mtime).strftime("%d-%m-%Y %H:%M")
    except:
        modified = "unknown"
    if os.path.isfile(fullPath):
        type = "file"
    elif os.path.isdir(fullPath):
        type = "directory"
    else:
        type = "unknown"
    print("{0:<{6}}{1:<12}{2}{3}{4:<3}{5}".format(entity, type, read, write, execute, modified, padding))
print()
