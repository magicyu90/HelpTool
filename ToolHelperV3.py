# coding=utf-8
import codecs
import xml.etree.ElementTree as ET
import os
import shutil

srcDir = "E:\\zx"
destDir = "E:\\zxcopy"
dirs = os.listdir(srcDir)

# 对于符合规范的xml文件直接，进行反序列化操作
# tree = ET.parse('ManualLabel.xml')
# root = tree.getroot()
# susCount = 0
# for sus in root.findall('sus'):
#     susCount += 1

def copytree(src, dst, symlinks=False, ignore=None):
    '''Copy src directory to dest directory'''
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

for currentDir in dirs:
    dirToEnter = srcDir + "\\" + currentDir + "\\" + "ManualLabel"
    manualLabelFiles = os.listdir(dirToEnter)
    for file in manualLabelFiles:
        if file.endswith('.xml'):
            susCount = 0
            xmlFile = open(dirToEnter + "\\" + file, 'r', encoding="utf8")
            xmlFileLines = xmlFile.readlines()[2:]
            xmlFileStr = ''.join(xmlFileLines)
            root = ET.fromstring(xmlFileStr)
            for sus in root.findall('sus'):
                susCount += 1
            if susCount == 1:
                print('copy dir:', srcDir + "\\" + currentDir)
                copytree(srcDir + "\\" + currentDir, destDir + "\\" + currentDir)