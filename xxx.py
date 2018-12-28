# !/bin/env python
# -*- encoding=utf8 -*-

import os,sys,shutil,time,re

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

def main():
    files = getFileInPath(os.getcwd(), True, True)
    result, newPath = mkdir("pngdir")
    for file in files:
        # isPngFile = re.match(r"^\w+\.png$", file)
        isPngFile = (file.find("png") >= 0)
        if isPngFile:
            fileName = os.path.basename(file)
            des_path = newPath + '/' + fileName
            # print(des_path)
            shutil.copy(file, des_path)

if __name__ == "__main__":
    main()
