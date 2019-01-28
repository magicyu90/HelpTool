# coding=utf-8
"""
对指定的目录的图像移动
"""

import os
import shutil
import argparse
from shutil import copyfile

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--src', help='包含img的源文件夹')
parser.add_argument('-d', '--dest', help='目的文件夹')

filePath = ''
destPath = ''

args = parser.parse_args()
if args.src:
    if not os.path.exists(args.src):
        raise Exception('请验证源文件夹')
    filePath = args.src
    print('src:', args.src)
else:
    raise Exception('没有指定源文件夹')

if args.dest:
    if not os.path.exists(args.dest):
        raise Exception('请验证目的文件夹')
    destPath = args.dest
    print('dest:', args.dest)
else:
    raise Exception('没有指定目的文件夹')

for root, dirs, files in os.walk(filePath):
    for name in files:
        ext = os.path.splitext(name)[-1]
        basename = os.path.splitext(name)[0]
        if ext == '.xml' and 'Helix' in dirs:
            searchname = os.path.join(root, basename+'.img')
            if os.path.exists(searchname):
                destname = os.path.join(destPath, basename+'.img')
                shutil.copyfile(searchname, destname)
