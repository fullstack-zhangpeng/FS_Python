#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : zhang!Peng

import os, json

# 常量
jsonFilePath = "~/Desktop/tmp/doc/"

filterFiles = [
    "data_fliter.json"
]

# def getFileContent(filePath):
#     file = open(filePath, mode='r')
#     fileContent = ""
#     try:
#        fileContent = file.read()
#     finally:
#         file.close()
#     return fileContent

if __name__ == "__main__":
    print("开始执行...")
    for root, dirs, files in os.walk("./doc/", topdown=False):
        for fileItem in files:
            if fileItem in filterFiles:
                continue
            fileFullPath = os.path.join(root, fileItem)

            try:
                jsonObj = json.load(open(fileFullPath))
            except Exception as e:
                print("json.loads error file[%s]" % fileItem)
            
            print(jsonObj)
        # for name in dirs:
        #     print(os.path.join(root, name))
    print("执行完毕...")
