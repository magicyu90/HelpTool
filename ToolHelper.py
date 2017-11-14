# coding=utf-8
import codecs
import os.path
import xml.etree.ElementTree as ET
import shutil

localDir = "E:\\zx\\"
destDir = "E:\\zxcopy\\"
dirs = os.listdir(localDir)

def copytree(src, dst, symlinks=False, ignore=None):
    '''Copy src directory to dest directory'''
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

# 通过行数来判断是否有多个Label，需要优化
for currentDir in dirs:
    dirToEnter = localDir + currentDir + "\\" + "ManualLabel"
    manualLabelFiles = os.listdir(dirToEnter)
    for file in manualLabelFiles:
        if file.endswith('.xml'):
            xmlFileLines = sum(1 for line in open(
                dirToEnter + "\\" + file, 'r', encoding="utf8"))
            if xmlFileLines <= 13:
                # copy 文件夹
                print('copy dir:', localDir + currentDir)
                copytree(localDir + currentDir, destDir + currentDir)
