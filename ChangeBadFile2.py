# coding=utf-8
import codecs
import os
import shutil

srcDir = r"G:\TIP图库\12\ba"
#srcDir = "G:\\hao\\06-lixi"
dirs = os.listdir(srcDir)
helixName = "helix"
helixSEName = "helixse"

dirCount = 1400
index_to_change = 1
for currentDir in dirs:
    dirNewName = "Gun%04d" % dirCount
    try:
        files = os.listdir(os.path.join(srcDir, currentDir))
        for fileName in files:
            # filePath = srcDir + "\\" + currentDir
            filePath = os.path.join(srcDir, currentDir)
            if not os.path.isdir(os.path.join(filePath, fileName)):  # 文件
                fileExtensionIndex = fileName.rfind('.')
                fileExtension = fileName[fileExtensionIndex:]

                if fileExtension == '.jpg' and 'OB' in fileName[:2]:
                    continue
                # 对于以pi、db、raw结尾的文件不进行处理
                if fileExtension != '.pi' and fileExtension != '.db' and fileExtension != '.raw':
                    if fileName.find('_') != -1:  # 名字中带有'_'
                        indexToChange = fileName.find('_Gun_%04d_1' % index_to_change)
                        #print('filename:%s,count.:%d' % (fileName, fileName.count('.')))

                        # os.rename(filePath + "\\" + fileName,
                        #           filePath + "\\" + newName)

            else:
                # 只处理Helix和HelixSE文件夹
                if fileName.lower() == helixName or fileName.lower() == helixSEName:
                    filePath = filePath + "\\" + fileName
                    helixFiles = os.listdir(filePath)
                    for helixFileName in helixFiles:
                        if helixFileName.count('.') == 2:
                            print('change helix bad file with name:%s' % helixFileName)
                            firstIndex = helixFileName.find('.')
                            lastIndex = helixFileName.rfind('.')
                            helixNewName = helixFileName[:firstIndex] + helixFileName[lastIndex:]
                            print(helixNewName)
                            os.rename(filePath + "\\" + helixFileName,
                                      filePath + "\\" + helixNewName)
    except Exception as ex:
        print('Error happend:%s' % str(ex))
        # continue

    #os.rename(srcDir + "\\" + currentDir, srcDir + "\\" + dirNewName)
    dirCount += 1
    index_to_change += 1
