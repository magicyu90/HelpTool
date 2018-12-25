"""
对图像标注工具生成的图像进行归类和移动,有分类文件
"""

# coding=utf-8
import codecs
import os
import shutil
import itertools

source_dir = r'C:\Users\shenyu1.NUCTECH\Desktop\问题箱包1'
files = os.listdir(source_dir)


# 检测分类文件
if not os.path.exists(source_dir+'\\'+'category.txt'):
    raise Exception('分类文件不存在')

category_file = open(source_dir+'\\'+'category.txt')
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

for file_name in files:
    name, ext = os.path.splitext(file_name)
    if ext == '.txt' and name != 'category':
        text_file = open(source_dir + '\\' + file_name, "r", encoding='utf-8')
        lines = text_file.readlines()
        i = 1
        origin_name = name[0:name.rfind('_')]
        jpg_name = origin_name+'.jpg'
        png_name = origin_name+'_label'+'.png'
        current_categories = []
        for line in lines:
            line = line.strip('\n')
            line = line.replace(u'\ufeff', '')
            category = line.split(' ')[0]
            # print(category)
            if not category in categories:
                #category = line.split(' ')[0]+' '+line.split(' ')[1]
                print('not in category:', category)
            current_categories.append(category)

        if len(current_categories) <= 1:  # 单一类
            new_dir = os.path.join(source_dir, category)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            if not os.path.exists(new_dir+'\\'+file_name):
                shutil.copyfile(source_dir+'\\' + file_name, new_dir+'\\'+file_name)
                shutil.copyfile(source_dir+'\\' + jpg_name, new_dir+'\\'+jpg_name)
                shutil.copyfile(source_dir+'\\' + png_name, new_dir+'\\'+png_name)
        else:
            set_list = list(set(current_categories))
            if len(set_list) == 1:
                new_dir = os.path.join(source_dir, 'single_%s' % (set_list[0]))
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                if not os.path.exists(new_dir+'\\'+file_name):
                    shutil.copyfile(source_dir+'\\' + file_name, new_dir+'\\'+file_name)
                    shutil.copyfile(source_dir+'\\' + jpg_name, new_dir+'\\'+jpg_name)
                    shutil.copyfile(source_dir+'\\' + png_name, new_dir+'\\'+png_name)
            else:
                new_dir = os.path.join(source_dir, 'mix_%s' % ('_'.join(set_list)))
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                if not os.path.exists(new_dir+'\\'+file_name):
                    shutil.copyfile(source_dir+'\\' + file_name, new_dir+'\\'+file_name)
                    shutil.copyfile(source_dir+'\\' + jpg_name, new_dir+'\\'+jpg_name)
                    shutil.copyfile(source_dir+'\\' + png_name, new_dir+'\\'+png_name)
