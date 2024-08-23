#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：PythonScript 
@File    ：gui.py
@Author  ：金脚大王
@Date    ：2024/1/29 15:13 
@脚本说明：
"""
import PySimpleGUI as sg
from ChangeMarkdownWord import ChangeMarkdownWord

#License Key of PySimpleGui
#e0ywJQMlaCWYNGl6benFN3lxVxHclqwrZzShI463ImkwRMlvdNmiVRstbb33BBlvcpiqIAs1Izk7xlpKYk2RVgulcS2FV8JYReC0Ix6VMrTucVyiNaDsIh55NyTrAM4hNwCzwQi3TfGAlijDZLWh5QzKZZU6RFlzcoG1x5vIeLWW1clhbKnORcWQZ0XPJezQaPWk9fu3IAjdo1xALoCTJfOWYbWl1Tl3RQmCl2yYcv3fQViiOTiXJzmLdjX6RAhXYkmYEfihLSClJiOBY7WU1lllTRGQFqz7dSCHI661IDmClS0cbGyNIosTITkmNRvDbEXXBGh3bZnHk8iLOziNI5ixLsCuJyD3d9XmNW0PbD2J1HlRcUk2loEFISjdo5inM3zhUf0tMJDugmiaLfCHJ0E5YlXYRilUSsX2NXzWd7WaVzkRIaj8oyieM4DygAvDMYjpIGvZMwjsAVyqN6CRIhsIIqkzRwhydCG6VMFfe8HfBOp7cVmsV1z5IQjQoqiLMADCgdvIMwjFIDv4M2j9AYyHNtSnIZsFIBkCVftsYQWJlLsMQXWWRlkZcOm2VOz9chy9Ib6zImmGl20Xb92SZJpoc62PhrAVcQ2ulWuGYtSz5Djzbm250cifL0CdJdJqU5EhFokhZdHaJllXcp3MM6iZOrizI41pLSjpM80gLRj0IKxEN4io4FxwMQD0Yligf1Qe=L=O41df6114dc62c454ced01cd9a3b880c59c157124b30e7d694d566daf492f00430ec48392783b11d2ae4993038ad35f3f8e3f2128f835a9c9150af1b55ebddd00db111fc88ff50e7f5070ae940c8b6d4b7c4fe995dcdd12feeefdf2918ee2795cae33ba9ac1090296059a6f4fd2dc5bf7bbcb3030e56fcd058078e039ddb8183ff2187a639b6f718b44e2d3320e7fd8f8fa6cf5ba4b559ad9ce0688dc9773d8044df24b6ace86932c1cff00c6fcfa858a7cb0329118d927da2b6d500e6905cfc5a407574863441de7479ae8aeddac7f1025b540b8d3e4cc74a6b1f6bd55b1779e5c99b5629dcc6869f2c327b27ec78696834dc7d74ac4b83076157d12715714dad2de52a5d177db2b2205a67e444cc2ee4f9c302b51c78535afdacc47668aa61978ea1b6bf4d5f78791b83f8051cc0991d708bcc7592147568b1b14b65509c11744439e406e346d5433216a69cc261b58447d547e52935eecfd913d09549431f1c319c474285a1343a42196b3d13fc638cddedd28a1650b92b5b4086b4880df369ff23d9e883dd47933dee9aae9f8fcbb7d04feaccee2bfd4cb53da83d43c1aa6d1d6c791d277f3d623b0b975be93a2b291ead63be500c2c584709e5681e175bf36e09e48360d8190d6e0d321fe44f58b8e0ad43f5698d7783d4c0075a2fe682e0567c12976d81f294b6e40e2fc2f37cd1e9d48be3d33de8b238ac7f30a759dfe
ha
sg.theme('Darkred2')

layout = [
    [sg.Text("选择处理前的文件存放位置")],
    [sg.InputText(key="-INPUT-"), sg.FileBrowse(size=(20, 1))],
    [sg.Text("选择处理后的文件存放位置")],
    [sg.InputText(key="-OUTPUT-"), sg.SaveAs(size=(20, 1))],
    [sg.Button("开始处理", size=(10, 1), pad=((150, 0), (10, 0))),
     sg.Button("退出", size=(10, 1), pad=((10, 0), (10, 0)))]
]

window = sg.Window("Markdown Add comments to English Tools", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "退出":
        break
    elif event == "开始处理":
        # 接受文件位置
        input_file = values["-INPUT-"]
        output_file = values["-OUTPUT-"]

        # TODO: 在这里添加文件处理的代码
        ChangeMarkdownWord(input_file,output_file)

        # 交互反馈
        sg.popup(f"处理完成！\n输入文件：{input_file}\n输出文件：{output_file}")

window.close()