# coding=utf-8
"""
第二步：指定的目录里的  
"""

import os
import shutil
import argparse
from shutil import copyfile

# parser = argparse.ArgumentParser()
# parser.add_argument('-s', '--src', help='包含xml和txt的源文件夹')
# parser.add_argument('-d', '--dest', help='目的文件夹')

filePath = r'E:\testdest'
destPath = r'E:\testmerge'

# args = parser.parse_args()
# if args.src:
#     if not os.path.exists(args.src):
#         raise Exception('请验证源文件夹')
#     filePath = args.src
#     print('src:', args.src)
# else:
#     raise Exception('没有指定源文件夹')

# if args.dest:
#     if not os.path.exists(args.dest):
#         raise Exception('请验证目的文件夹')
#     destPath = args.dest
#     print('dest:', args.dest)
# else:
#     raise Exception('没有指定目的文件夹')

#alldirs = []

# for root, dirs, files in os.walk(destPath):
#     alldirs.extend(dirs)

for root, dirs, files in os.walk(filePath):
    for name in files:
        ext = os.path.splitext(name)[-1]
        basename = os.path.splitext(name)[0]
        if ext == '.txt' or ext == '.png':
            #last_14_digits = basename[-14:]
            year= basename[-20:-16]
            date= basename[-16:-12]
            package= basename[-12:-6]
            test_path=os.path.join(destPath, year,date,package)
            is_exist = os.path.exists(test_path)
            if is_exist:
                copyfile(os.path.join(root, name), os.path.join(test_path, name))