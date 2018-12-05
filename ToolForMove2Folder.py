'''
图库挪到同名文件夹
'''

import os
from shutil import copyfile, rmtree

source_dir = r'G:\非洲项目图库\knife'

dest_dir = r'C:\Users\shenyu1.NUCTECH\Desktop\dest'

files = os.listdir(source_dir)
folders_tocheck = []

for file_name in files:
    print(file_name)
    folder_to_move = file_name.split('.')[0][0:9]
    new_folder = os.path.join(source_dir, folder_to_move)

    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    copyfile(source_dir+'\\' + file_name, new_folder+'\\'+file_name)
