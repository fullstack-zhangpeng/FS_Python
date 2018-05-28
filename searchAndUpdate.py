# !/bin/env python
# -*- encoding=utf8 -*-

import os,sys,shutil, time

def getDirPath():
    inputContent = input("请指定文件夹: ")
    return inputContent

def changeWorkPath(workPath):
    print(workPath.strip())
    os.chdir(workPath.strip())

def getSubItemInPath(path, isRecursive):
    subItems = os.listdir(path)
    files = []
    for item in subItems:
        itemPath = os.path.join(path, item)
        if os.path.isfile(itemPath) and not item.startswith("."):
            files.append(itemPath)
        else:
            if isRecursive:
                files.extend(getSubItemInPath(itemPath, True))
    return files

if __name__=="__main__":
    # 获取当前工作目录 os.getcwd()
    dirPath = getDirPath()
    # print("dirPath: %s" %(dirPath))
    # 改变工作目录到指定的 dirPath
    changeWorkPath(dirPath)
    # print("currentWorkPath: %s" %(os.getcwd()))
    # 获取工作目录的所有文件
    filePaths = getSubItemInPath(os.getcwd(), False) 
    # print ("指定目录下的文件列表：\n", files)
    # # 获取要查找的内容
    targetString = input("请输入要查找的内容: ")
    # # 获取要替换的内容
    replaceString = input("请输入要替换的内容: ")
    # print("targetString: %s, replaceString: %s" %(targetString, replaceString))
    bakPath = os.path.join(os.getcwd(), "bak")
    if not os.path.exists("bak"):
        os.mkdir("bak")
    else:
        os.rename(bakPath, bakPath + time.strftime("_%H:%M:%S_%Y-%m-%d", time.localtime()))
        os.mkdir("bak")

    for path in filePaths:
        shutil.copy(path, os.path.join(bakPath, os.path.basename(path)))
        f = open(path, "r+", encoding="utf-8")
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace(targetString, replaceString))
        f.close()
