# coding=utf-8
import codecs
import os
import shutil

srcDir = "C:\\Users\\shenyu1.NUCTECH\\Desktop\\dangerbaggage"
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
