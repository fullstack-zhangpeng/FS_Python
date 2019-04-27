#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : zhang!Peng

import os
import json

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


class JsonClass(object):
    def __init__(self, fileFullPath, jsonObj):
        super(JsonClass, self).__init__()
        self.fileFullPath = fileFullPath
        self.jsonObj = jsonObj

    def parse(self):
        self.description = self.jsonObj['description'] if (
            'description' in self.jsonObj) else ''
        self.url = self.jsonObj['url'] if ('url' in self.jsonObj) else ''
        self.method = self.jsonObj['method']
        self.input = self.jsonObj['input']
        self.output = self.jsonObj['output']


class JsonModel(object):
    def __init__(self):
        super(JsonModel, self).__init__()
        self.jsons = []
        self.jsonObjs = []

        # self.json_schema_default = None
        # self.json_schema_type = None

        # self.json_schema_ios_entity = None
        # self.json_schema_ios_enum = None
        # self.json_schema_java_enum = None

        # self.schema_type = {}
        # self.schema_default = {}

    def parse_define(self, key, value):
        for subKey, subValue in value.items():
            if key == 'subDefine':
                value[key] = self.parse_define(key, subValue)
                continue
                
            if type(value[key]) is dict and 'type' in value[key] and value[key]['type'] == 'dict':
                self.parse_define('subDefine', value[key]['subDefine'])

            if type(value[key]) is dict and 'type' in value[key] and value[key]['type'] == 'list':
                value[key]['subDefine'] = self.parse_define('subDefine', value[key]['subDefine'])
        return value
        # for key in value.keys():

        #     if type(value[key]) is dict and 'type' in value[key] and value[key]['type'] in self.schema_type.keys():
        #         # value[key] = self.schema_type[value[key]['type']]
        #         pass

            

        #     if type(value[key]) is dict and 'type' in value[key] and value[key]['type'] == 'dict':
        #         self.parse_define('subDefine', value[key]['subDefine'])

        #     if type(value[key]) is dict and 'type' in value[key] and value[key]['type'] == 'list':
        #         value[key]['subDefine'] = self.parse_define(
        #             'subDefine', value[key]['subDefine'])

        #     if type(value[key]) is dict and value[key]['type'] == 'default' and key in self.schema_default.keys():
        #         value[key] = self.schema_default[key]

        #     if key == 'type' and value[key] in self.schema_type.keys():
        #         value = self.schema_type[value[key]]
        #         value['subDefine'] = self.parse_define(
        #             'subDefine', value['subDefine'])

        #     if 'type' in value and value['type'] == 'default' and aKey in self.schema_default.keys():
        #         value = self.schema_default[aKey]
        # # print value
        # return aVa

    def set_json_obj_type(self, jsonObj):
        for key, value in jsonObj.items():
            jsonObj[key] = self.parse_define(key, value)

    def parse(self):
        for jc in self.jsons:
            self.set_json_obj_type(jc.jsonObj["output"])
            self.jsonObjs.append(jc.jsonObj)
        # print ('接口总数: %d' % len(self.jsonObjs))

    def getJsonFiles(self):
        for root, dirs, files in os.walk("./doc/", topdown=False):
            for fileItem in files:
                if fileItem in filterFiles:
                    continue
                fileFullPath = os.path.join(root, fileItem)

                try:
                    jsonObj = json.load(open(fileFullPath))
                except Exception as e:
                    print("json.loads error file[%s]" % fileItem)

                jc = JsonClass(fileFullPath, jsonObj)
                self.jsons.append(jc)


if __name__ == "__main__":
    print("开始执行...")
    aJsonModel = JsonModel()
    aJsonModel.getJsonFiles()
    aJsonModel.parse()
    print("执行完毕...")
