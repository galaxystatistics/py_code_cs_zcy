#!/usr/bin/env python
# -*- coding: cp936 -*-

import re

##��CommView�ı��д���HEX�б�
#����˿ں�Э����ж�
def CreatHexFromCV(HexFile):
    file1=file(HexFile,'r');
    filecontent = file1.read()
    pattern='Raw Data:.*?====='
    p = re.compile(pattern,re.DOTALL)
    result = p.findall(filecontent)
    
    list = []
    
    for i in result:
        ##��'//'ע���滻��
        pattern='   [0-9a-fA-F]{2}.+?   '
        p = re.compile(pattern,re.DOTALL)
        result1 = p.findall(i)
        tmpHex = ''
        for trep in result1:
            tmpHex = tmpHex + trep
        else:
            tmpHex = tmpHex.replace(' ', '')
            tmpHex = tmpHex.replace('-', '')
            list.append(tmpHex.strip())
            tmpHex = ''
    return list

def CreatHexFromTXT(HexFile):
    list = []
    file1=file(HexFile,'r');
    for l in file1.readlines():
        list.append(l)
    return list

def CreatHexFromTXTDIR(path):
    
    file1=file(path,'r');
    filecontent = file1.read()
    
    return filecontent
