import os
from shutil import copyfile, rmtree

source_dir = r'C:\Users\shenyu1.NUCTECH\Desktop\pg'

dest_dir = r'C:\Users\shenyu1.NUCTECH\Desktop\dest'

files = os.listdir(source_dir)
folders_tocheck = []

for file_name in files:
    folder_to_move = file_name.split('.')[0][-6:]
    folders_tocheck.append(folder_to_move)
    if os.path.exists(dest_dir+'\\'+folder_to_move):
        print('%s will be copied...' % (source_dir+'\\' + file_name))
        copyfile(source_dir+'\\' + file_name, dest_dir+'\\'+folder_to_move+'\\'+file_name)


dest_folders = os.listdir(dest_dir)
for folder in dest_folders:
    if folder not in folders_tocheck:
        print('%s not exist,will be deleted' % folder)
        # rmtree(dest_dir+'\\'+folder)
