# !/bin/env python
# -*- encoding=utf8 -*-

import os,sys,shutil,time,re

def getSearchDirPath():
    inputContent = input("请指定搜索文件夹: ")
    return inputContent

def getSearchContent():
    inputContent = input("请输入搜索内容: ")
    return inputContent

def getDestinationDir():
    inputContent = input("请输入临时文件夹的名字(会和本python文件在同级目录下): ")
    return inputContent

### 创建多层目录
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 创建目录操作函数
        os.makedirs(path)
        # 如果不存在则创建目录
        print(path + ' 创建成功')
        return (True, path)
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return (False, path)

def getFileInPath(path, isRecursive, ignoreHidden):
    subItems = os.listdir(path)
    files = []
    for item in subItems:
        # 文件全路径
        itemPath = os.path.join(path, item)
        if ignoreHidden and item.startswith("."): # 忽略隐藏文件 并且以.开头
             continue
        else: # 不忽略隐藏文件
            if os.path.isfile(itemPath):
                files.append(itemPath)
            else:
                if isRecursive:
                    files.extend(getFileInPath(itemPath, True, ignoreHidden))
    return files

def search(searchContent, files):
    resultFiles = []
    for file in files:
        # re.search(searchContent, os.path.basename(file), re.I)
        searchResult = re.search(searchContent, os.path.basename(file), re.I)
        if searchResult:
            resultFiles.append(file)
    return resultFiles

def moveFileFromFiles(destinationDir, files):
    for file in files:
        fileName = os.path.basename(file)
        des_path = destinationDir + '/' + fileName
        try:
            shutil.copy(file, des_path)
        except IOError as e:
            # print(fileName + ", 未复制")
            print("Unable to copy file. %s" %e) 
            
if __name__ == "__main__":
    # 选择文件夹
    searchPath = getSearchDirPath()
    # searchPath = os.getcwd()
    # 获取路径下所有的文件
    files = getFileInPath(os.getcwd(), True, True)
    # 输入搜索内容
    searchContent = getSearchContent()
    # 根据搜索内容搜索
    resultFiles = search(searchContent, files)
    # 移动至新的文件夹
    destinationDir = getDestinationDir()
    # 创建新的文件夹
    result, newPath = mkdir(destinationDir)
    # 复制一份新的文件至目标文件夹
    moveFileFromFiles(newPath, resultFiles)


