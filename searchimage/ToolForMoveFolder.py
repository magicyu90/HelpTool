# coding=utf-8
"""
第三步：移动包含txt的文件夹到目文件夹
"""

import os
import shutil
import argparse
from shutil import copyfile, copytree


filePath = r'E:\testmovefolder\eqp1'
destPath = r'E:\tttt\ttt\eqp1'

eqp = os.path.basename(filePath)

for root, dirs, files in os.walk(os.path.join(filePath)):
    for name in files:
        ext = os.path.splitext(name)[-1]
        basename = os.path.splitext(name)[0]
        if ext == '.txt':
            new_root = root.replace(filePath, destPath)
            if not os.path.exists(new_root):
                os.makedirs(new_root)
            for file in os.listdir(root):
                srcFile = os.path.join(root, file)
                targetFile = os.path.join(new_root, file)
                if os.path.isfile(srcFile):
                    print('复制文件%s到%s' % (srcFile, targetFile))
                    shutil.copyfile(srcFile, targetFile)
                else:
                    if not os.path.exists(targetFile):
                        print('复制目录%s到%s' % (srcFile, targetFile))
                        shutil.copytree(srcFile, targetFile)
