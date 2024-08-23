#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonScript 
@File    ：main.py
@Author  ：金脚大王
@Date    ：2024/1/28 11:31 
@脚本说明：为所有markdown中的英文字体加上反引号
@代码思路：1、读取文件所有文本内容
         2、去除代码块部分的文本
         3、正则识别所有英文单词（识别为一个整体）
         4、为英文前后增加反引号
"""
import re

def ChangeMarkdownWord(before,after):
    # 读取Markdown文件
    with open(before,encoding='utf-8') as f:
        contents = f.readlines()

    # 打印修改前的文本
    # print('before:'+str(contents))

    # 生成0，1交替数
    def num(n):
        a = 1
        b = 0
        for i in (a,b):
            if n:
                pass
                n = n-1
            else:
                return i

    # n为代码块的控制位。
    n = 1
    # 修改后的文本存储。
    formatted_text = ''
    # 如果找到网址格式的不添加反引号。
    pattern_exclusion = r'\[[^\]]*\]\([^\)]*\)'
    # 使用正则表达式匹配所有的英文单词，并为每个单词前后添加反引号。
    for i in contents:
        # 标题部分不识别
        if i.startswith('#'):
            formatted_text += i
        # 網址部分不識別。
        elif re.findall(pattern_exclusion, i):
            formatted_text += i
        # 圖片不識別
        elif i.startswith('!['):
            formatted_text += i
        # 表格開頭不識別
        elif i.startswith('|'):
            formatted_text += i
        # 代码块部分不识别，设置n值来匹配成对的代码块标识
        elif i.startswith('```'):
            formatted_text += i
            n = num(n)
        # 如果没有遇到代码块则匹配英文字母，并且替换添加单引号
        elif n:
            pattern = r'([A-Za-z0-9\/\.\-\@\?\&\%]+)|\b([A-Za-z0-9\/\.\-\@\?\&\%]+)\b|\b([A-Za-z0-9\/\.\-\@\?\&\%]+)\B|\B([A-Za-z0-9\/\.\-\@\?\&\%]+)\b|\B([A-Za-z0-9\/\.\-\@\?\&\%]+)\B'
            if i.startswith('-'):
                if len(i) > 1:
                    startwithline = i[1:]
                    formatted_text += '- ' + re.sub(pattern, r'`\1\2\3\4`', startwithline)
                else:
                    startwithlineandnone = ""
                    formatted_text += '- ' + re.sub(pattern, r'`\1\2\3\4`', startwithlineandnone)
            else:
                formatted_text += re.sub(pattern, r'`\1\2\3\4`', i)
        # 其他的所有情况，都原样添加
        else:
            formatted_text += i

    # 打印修改后的文本
    # print('formatted:'+formatted_text)
    pattern = '(?<!`)``(?!`)'
    formatted_text = re.sub(pattern,'`',formatted_text)

    with open(after,'w',encoding='utf-8') as f:
        f.write(formatted_text)


