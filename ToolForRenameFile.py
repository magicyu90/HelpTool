# coding=utf-8
import codecs
import os
import shutil

srcDir = "G:\\英文卢顿图库200新版\\11\\1199"
#srcDir = "G:\\hao\\06-lixi"
dirs = os.listdir(srcDir)
helixName = "Helix"
helixSEName = "HelixSE"

dirCount = 1
for currentDir in dirs:
    dirNewName = "FalseAlarm%04d" % dirCount
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
            if not os.path.isdir(os.path.join(filePath, fileName)):  # 文件
                fileExtensionIndex = fileName.rfind('.')
                fileExtension = fileName[fileExtensionIndex:]
                # 对于以pi、db、raw结尾的文件不进行处理
            # print(fileName)

                if fileExtension == '.jpg' and 'OB' in fileName[:2]:
                    continue
                if fileExtension != '.pi' and fileExtension != '.db' and fileExtension != '.raw':
                    if fileName.find('_') != -1:
                        indexToChange = fileName.find('_')
                        print("change name contains '_':", fileName)
                        newName = dirNewName + fileName[indexToChange:]
                        os.rename(filePath + "\\" + fileName,
                                  filePath + "\\" + newName)
                    else:
                        print('change name directly:', fileName)
                        newName = dirNewName + fileExtension
                        os.rename(filePath + "\\" + fileName,
                                  filePath + "\\" + newName)

            else:
                # 只处理Helix和HelixSE文件夹
                if fileName == helixName or fileName == helixSEName:
                    filePath = filePath + "\\" + fileName
                    helixFiles = os.listdir(filePath)
                    for helixFileName in helixFiles:
                        helixIndexToChange = helixFileName.find('_')
                        print('change helix file name:', helixFileName)
                        helixNewName = dirNewName + \
                            helixFileName[helixIndexToChange:]
                        os.rename(filePath + "\\" + helixFileName,
                                  filePath + "\\" + helixNewName)
    except Exception as ex:
        print('Error happend:%s' % str(ex))
        # continue

    os.rename(srcDir + "\\" + currentDir, srcDir + "\\" + dirNewName)
    dirCount += 1
