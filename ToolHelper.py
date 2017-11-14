#coding=utf-8
import codecs
import os.path
import xml.etree.ElementTree as ET
import shutil


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


#通过行数来判断是否有多个Label，需要优化
localDir = "E:\\zx\\"
destDir = "E:\\zxcopy\\"
dirs = os.listdir(localDir)
for dir in dirs:
    dirToEnter = localDir + dir + "\\" + "ManualLabel"
    manualLabelFiles = os.listdir(dirToEnter)
    for file in manualLabelFiles:
        if file.endswith('.xml'):
            xmlFileLines = sum(1 for line in open(
                dirToEnter + "\\" + file, 'r', encoding="utf8"))
            if xmlFileLines <= 13:
                # copy 文件夹
                print('copy dir:', localDir + dir)
                copytree(localDir + dir, destDir + dir)
