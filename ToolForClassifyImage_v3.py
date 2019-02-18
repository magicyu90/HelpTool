"""
对图像标注工具生成的图像进行归类和移动,需要指明原路径、生成路径和分类文件
运行之后，会在生成路径产生info.txt
"""

# coding=utf-8
import codecs
import os
import shutil
import itertools

source_dir = r'G:\图像标注\重庆江北机场jpg分发--郑鹏\范小晶\已标注\TFNCH-VII-160037'
category_file = r'C:\Users\shenyu1.NUCTECH\Desktop\category.txt'
dest_dir = r'C:\Users\shenyu1.NUCTECH\Desktop\dest\TFNCH-VII-160037'

info_text = open(dest_dir+'\\'+'info.txt', 'w')
# 检测分类文件
if not os.path.exists(category_file):
    raise Exception('分类文件不存在')

info_text.write('原路径:%s,生成路径:%s \n' % (source_dir, dest_dir))
info_text.write('生成信息:\n')

category_file = open(category_file)
lines = category_file.readlines()
category_dict = dict()
for line in lines:
    line = line.strip('\n')
    if line != '':
        if '##' in line:
            current_category = line.replace('#', '')
            category_dict[current_category] = []
        else:
            category_dict[current_category].append(line)

categories = list(itertools.chain.from_iterable(category_dict.values()))
print(categories)

for root, dirs, files in os.walk(source_dir):
    for name in files:
        # print(name)
        ext = os.path.splitext(name)[-1]
        basename = os.path.splitext(name)[0]
        if ext == '.txt':
            origin_name = basename.replace('_label', '')
            jpg_name = origin_name+'.jpg'
            png_name = origin_name+'_label'+'.png'
            current_categories = []
            text_file = open(root + '\\' + name, "r", encoding='utf-8')
            lines = text_file.readlines()
            for line in lines:
                line = line.strip('\n')
                line = line.replace(u'\ufeff', '')
                category = line.split(' ')[0]
                # print(category)
                if not category in categories:
                    #category = line.split(' ')[0]+' '+line.split(' ')[1]
                    print('not in category:', category)
                current_categories.append(category)

            #----------------------生成类对应文件夹----------------------#
            if len(current_categories) <= 1:  # 单一类
                new_dir = os.path.join(dest_dir, category)
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
            else:
                set_list = list(set(current_categories))
                set_list.sort()
                if len(set_list) == 1:
                    new_dir = os.path.join(dest_dir, 'single_%s' % (set_list[0]))
                    if not os.path.exists(new_dir):
                        os.makedirs(new_dir)
                else:
                    new_dir = os.path.join(dest_dir, 'mix_%s' % ('_'.join(set_list)))
                    if not os.path.exists(new_dir):
                        os.makedirs(new_dir)

            #----------------------拷贝文件----------------------#
            if os.path.exists(root+'\\'+name):
                # 拷贝txt
                shutil.copyfile(root+'\\' + name, new_dir+'\\'+name)
            if os.path.exists(root+'\\'+jpg_name):
                # 拷贝jpg
                shutil.copyfile(root+'\\' + jpg_name, new_dir+'\\'+jpg_name)
            else:
                info_text.write('jpg文件不存在:%s' % root+'\\'+jpg_name)
            if os.path.exists(root+'\\'+png_name):
                # 拷贝png
                shutil.copyfile(root+'\\' + png_name, new_dir+'\\'+png_name)
            else:
                info_text.write('png文件不存在:%s' % root+'\\'+png_name)
                    