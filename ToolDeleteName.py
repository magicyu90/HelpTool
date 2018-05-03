# coding=utf-8
import codecs
import os
import shutil

srcDir = "G:\\英国卢顿图库\\TIP图库\\12\\229-307"
# srcDir = "G:\\hao\\06-lixi"
dirs = os.listdir(srcDir)
helixName = "Helix"
helixSEName = "HelixSE"

dirCount = 1
for currentDir in dirs:
    dirNewName = "F_Gun_%04d_1" % dirCount
    try:
        # if os.path.exists(srcDir + "\\" + "bomb%s" % dirNewName):
        #     dirCount += 1
        #     continue
        # print(dirNewName)
        # files = os.listdir(srcDir + "\\" + currentDir)
        files = os.listdir(os.path.join(srcDir, currentDir))
        for fileName in files:
            # filePath = srcDir + "\\" + currentDir
            filePath = os.path.join(srcDir, currentDir)
            if fileName == helixName or fileName == helixSEName:
                filePath = filePath + "\\" + fileName
                helixFiles = os.listdir(filePath)
                for helixFileName in helixFiles:
                    newName = helixFileName.split('.')[0] + "." +helixFileName.split('.')[2]
                    #print(newName)
                    os.rename(filePath + "\\" + helixFileName,
                                filePath + "\\" + newName)
            # print(fileName)
    except Exception as ex:
        print('Error happend:%s' % str(ex))
        # continue

    # os.rename(srcDir + "\\" + currentDir, srcDir + "\\" + dirNewName)
    dirCount += 1
