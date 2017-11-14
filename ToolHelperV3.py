#coding=utf-8
import codecs
import xml.etree.ElementTree as ET

tree = ET.parse('ManualLabel.xml')
root = tree.getroot()

print('root:', root)
susCount = 0
for sus in root.findall('sus'):
    susCount += 1

print('susCount for ManualLabel.xml:', susCount)

xmlFile = open('ManualLabel2.xml', 'r', encoding="utf8")
xmlFileLines = xmlFile.readlines()[2:]
xmlFileStr = ''.join(xmlFileLines)
root2 = ET.fromstring(xmlFileStr)

susCount2 = 0
for sus in root2.findall('sus'):
    susCount2 += 1

print('susCount for ManualLabel2.xml:', susCount2)
