#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os,builtins


#写入文件
def writeFile(filename,content):
    document = open(filename, 'w')
    # print('文件名: ', document.name)
    document.write(content)
    # print(document.tell())
    #输出当前指针位置
    # document.seek(os.SEEK_SET)
    #设置指针回到文件最初
    # con = document.read()
    # print(con)
    document.close()

#读取文件，返回list
def readFile(filename):
    datalist = []

    with open(filename, 'rt') as handle:
        datas = [ln.strip('\n').split(' ') for ln in handle]
        # print(datas)

        i = 0
        for temp1 in datas:
            datalist.append([])
            if isinstance(temp1,list):
                for temp2 in temp1:
                    if temp2 == '' or temp2 is None or temp2 == 'Average:':
                        continue
                    else:
                        datalist[i].append(temp2)
                i = i + 1
            else:
                print('It is not list!')
    handle.close()
    # print(datalist)
    return datalist

