"""
对图像标注工具生成的图像进行归类和移动
"""

# coding=utf-8
import codecs
import os
import shutil


source_dir = r'C:\Users\shenyu1.NUCTECH\Desktop\安检机 图像'
files = os.listdir(source_dir)

categories = ['Control apparatus', 'Hazardous Substance', 'Gun', 'Explosives', 'charger', 'safe',
              'Sharp weapon', 'Blunt instrument', 'Fire', 'Pyrotechnic products', 'Other', 'tool', 'ammunition']

for file_name in files:

    name, ext = os.path.splitext(file_name)
    if ext == '.txt':
        text_file = open(source_dir + '\\' + file_name, "r")
        lines = text_file.readlines()
        i = 1
        origin_name = name[0:name.rfind('_')]
        img_name = origin_name+'.img'
        png_name = origin_name+'.png'
        current_categories = []
        for line in lines:
            category = line.split(' ')[0]
            if not category in categories:
                category = line.split(' ')[0]+' '+line.split(' ')[1]
            current_categories.append(category)

        if len(current_categories) <= 1:  # 单一类
            new_dir = os.path.join(source_dir, category)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            if not os.path.exists(new_dir+'\\'+file_name):
                shutil.copyfile(source_dir+'\\' + file_name, new_dir+'\\'+file_name)
                shutil.copyfile(source_dir+'\\' + img_name, new_dir+'\\'+img_name)
                shutil.copyfile(source_dir+'\\' + png_name, new_dir+'\\'+png_name)
        else:
            set_list = list(set(current_categories))
            if len(set_list) == 1:
                new_dir = os.path.join(source_dir, 'single_%s' % (set_list[0]))
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                if not os.path.exists(new_dir+'\\'+file_name):
                    shutil.copyfile(source_dir+'\\' + file_name, new_dir+'\\'+file_name)
                    shutil.copyfile(source_dir+'\\' + img_name, new_dir+'\\'+img_name)
                    shutil.copyfile(source_dir+'\\' + png_name, new_dir+'\\'+png_name)
            else:
                new_dir = os.path.join(source_dir, 'mix_%s' % ('_'.join(set_list)))
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                if not os.path.exists(new_dir+'\\'+file_name):
                    shutil.copyfile(source_dir+'\\' + file_name, new_dir+'\\'+file_name)
                    shutil.copyfile(source_dir+'\\' + img_name, new_dir+'\\'+img_name)
                    shutil.copyfile(source_dir+'\\' + png_name, new_dir+'\\'+png_name)
