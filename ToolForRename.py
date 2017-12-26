# coding=utf-8
import codecs
import os
import shutil

srcDir = "F:\\移动端图片汇总\\safe"
files = os.listdir(srcDir)
dirname = os.path.basename(srcDir)


index = 1
for file in files:
    appendixName = file.split('.')[1]
    newName = dirname + str(index).zfill(4) + "." + appendixName
    print(newName)
    os.rename(os.path.join(srcDir, file),
              os.path.join(srcDir, newName))
    index += 1
