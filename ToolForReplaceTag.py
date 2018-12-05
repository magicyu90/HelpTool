"""
替换图像类别
"""

# coding=utf-8
import codecs
import os
import shutil
import fileinput


source_dir = r'C:\Users\shenyu1.NUCTECH\Desktop\test'
files = os.listdir(source_dir)

categories = ['Control apparatus', 'Hazardous Substance', 'Gun', 'Explosives', 'charger', 'safe',
              'Sharp weapon', 'Blunt instrument', 'Fire', 'Pyrotechnic products', 'Other', 'tool', 'ammunition']


replaces = {
    'Sharp weapon': 'Sharp_weapon',
    'Blunt instrument': 'Blunt_instrument',
    'Hazardous Substance': 'Hazardous_Substance',
    'Control apparatus': 'Control_apparatus',
    'Pyrotechnic products': 'Pyrotechnic_products'
}
for file_name in files:
    name, ext = os.path.splitext(file_name)
    if ext == '.txt':
        #读取文件内容到缓存里
        with open(source_dir + '\\' + file_name, 'r') as file :
            filedata = file.read()

        if 'Sharp weapon' in filedata:
            filedata = filedata.replace('Sharp weapon', 'Sharp_weapon')
        if 'Blunt instrument' in filedata:
            filedata = filedata.replace('Blunt instrument', 'Blunt_instrument')
        if 'Hazardous Substance' in filedata:
            filedata = filedata.replace('Hazardous Substance', 'Hazardous_Substance')
        if 'Control apparatus' in filedata:
            filedata = filedata.replace('Control apparatus', 'Control_apparatus')
        if 'Pyrotechnic products' in filedata:
            filedata = filedata.replace('Pyrotechnic products', 'Pyrotechnic_products')

        # 重新把替换后的字符串写回文件里
        with open(source_dir + '\\' + file_name, 'w') as file:
            file.write(filedata)
