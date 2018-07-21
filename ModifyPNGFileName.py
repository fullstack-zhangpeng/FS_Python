# !/bin/env python
# -*- encoding=utf8 -*-

import os,sys,shutil, time, re

def main():
    path = os.getcwd()
    files = os.listdir(os.getcwd())
    for file in files:
        # isPngFile = re.match(r"^\w+\.png$", file)
        isPngFile = file.endswith(".png")
        if isPngFile:
            print(file, end="\n")
            searchObj = re.search(r"[0-9][Xx]", file)
            nxStart = searchObj.span()[0]
            nxEnd = searchObj.span()[1]

            nx = file[nxStart : nxEnd]
            nx = nx.replace("X", "x")

            subObj = re.sub(r"[0-9][Xx]", "", file)
            if subObj.index("."):
                newName = subObj[:subObj.index(".")] + "@" + nx + subObj[subObj.index("."):]
                newName = re.sub(r"@+", "@", newName)
                print(newName)
                os.rename(path + '/' + file, newName)

if __name__ == '__main__':
    main()