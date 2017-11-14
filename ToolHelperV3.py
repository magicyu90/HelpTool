#coding=utf-8
import codecs
import xml.etree.ElementTree as ET

#对于符合规范的xml文件直接，进行反序列化操作
tree = ET.parse('ManualLabel.xml')
root = tree.getroot()
susCount = 0
for sus in root.findall('sus'):
    susCount += 1


#对于不符合规范的xml文件，读取xml文件中的字符串
xmlFile = open('ManualLabel2.xml', 'r', encoding="utf8")
xmlFileLines = xmlFile.readlines()[2:]
xmlFileStr = ''.join(xmlFileLines)
root2 = ET.fromstring(xmlFileStr)

susCount2 = 0
for sus in root2.findall('sus'):
    susCount2 += 1
print('susCount for ManualLabel2.xml:', susCount2)
