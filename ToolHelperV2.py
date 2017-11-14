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


srcDir = "E:\\zx"
destDir = "E:\\zxcopy"
dirs = os.listdir(srcDir)

for dir in dirs:
    dirToEnter = srcDir + "\\" + dir + "\\" + "ManualLabel"
    manualLabelFiles = os.listdir(dirToEnter)
    for file in manualLabelFiles:
        if file.endswith('.xml'):
            labelCount = 0
            xmlFile = open(dirToEnter + "\\" + file, 'r', encoding="utf8")
            xmlFileLines = xmlFile.readlines()[2:]
            for line in xmlFileLines:
                line = line.strip()
                if line.startswith('<sus label='):
                    labelCount += 1
            if labelCount == 1:
                print('copy dir:', srcDir + "\\" + dir)
                copytree(srcDir + "\\" + dir, destDir + "\\" + dir)
