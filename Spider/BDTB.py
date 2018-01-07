__author__ = 'Hugo'
# coding:utf-8
from urllib import request
from bs4 import BeautifulSoup
import re
import os

# 处理页面标签类


class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


class BDTB:
    def __init__(self, baseUrl, see_lz):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(see_lz)
        self.content = ''
        self.page = None
        self.file = None
        self.tool = Tool()

    def getPage(self, pageNum):
        url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
        response = request.urlopen(url)
        page = response.read().decode('utf-8')
        # print(content)
        return page

    def getTitle(self, page):
        pattern = re.compile(r'<h3 class="core_title_txt.*?>(.*?)</h3>')
        result = re.search(pattern, page).group(1)
        return result if result else None

    def getPageNum(self, page):
        content = self.content
        pattern = re.compile(
            r'<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>.*?</li>')
        result = re.search(pattern, page).group(1)
        return result if result else None

    def getPostContent(self, page):
        pattern = re.compile(r'<div id="post_content_.*?>(.*?)</div>')
        items = re.findall(pattern, page)
        startPattern = re.compile(r'^\d{1,2} (.*)')
        contents = []
        for item in items:
            item = self.tool.replace(item)
            if re.match(startPattern, item):
                contents.append(item)
        return contents
        #------find post by beautifulSoup-----
        # soup = BeautifulSoup(self.content, 'html.parser')
        # for item in soup.find_all('div', class_='d_post_content j_d_post_content '):
        #     print(item)

    def writeData(self, contents):
        for item in contents:
            self.file.write(item + '\n')

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        try:
            print('该帖子共有:%s页' % str(pageNum))
            self.file = open(title + '.txt', 'w+')
            for i in range(1, int(pageNum) + 1):
                print('正在写入第' + str(i) + '页')
                page = self.getPage(i)
                contents = self.getPostContent(page)
                self.writeData(contents)

        except IOError as e:
            print('写入异常,原因:' + e.message)
        finally:
            self.file.close()
            print('写入完毕')


baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl, 1)
bdtb.start()
