#!/usr/bin/env python
# coding=utf-8
import string

#读取密文
clipertxt=open("c:/fuckme.txt","r", encoding='utf-8').read()

#读取去除ascii字符以外的密文字符集
mwcharset=set(clipertxt)-set(string.printable)
print(mwcharset)
#将密文字符集作为key，英文字母作为value拼成字典
dict1=dict(zip(mwcharset,string.ascii_letters))
print(dict1)
#将密文中加密的字符替换成英文字母
for key in dict1:
    clipertxt=clipertxt.replace(key,dict1[key])

print  (clipertxt)
