__author__ = 'Hugo'
# coding:utf-8
from urllib import request
from bs4 import BeautifulSoup
import re


class BDTB:
    def __init__(self, baseUrl, see_lz):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(see_lz)
        self.content = ''

    def getPage(self, pageNum):
        url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
        response = request.urlopen(url)
        content = response.read().decode('utf-8')
        # print(content)
        self.content = content

    def getTitle(self):
        content = self.content
        pattern = re.compile(r'<h3 class="core_title_txt.*?>(.*?)</h3>')
        result = re.search(pattern, content).group(1)
        print('title:%s' % result)
        return result if result else None

    def getPageNum(self):
        content = self.content
        pattern = re.compile(
            r'<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>.*?</li>')
        result = re.search(pattern, content).group(1)
        print('page num:%s' % result)
        return result if result else None

    def getPostContent(self):
        content = self.content
        # pattern = re.compile(r'<div id="post_content_.*?>(.*?)</div>')
        # items = re.findall(pattern, content)
        # for item in items:
        #     print(item)
        #------find post by beautifulSoup-----
        soup = BeautifulSoup(self.content, 'html.parser')
        for item in soup.find_all('div', class_='d_post_content j_d_post_content '):
            print(item)


baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl, 1)
bdtb.getPage(1)
bdtb.getTitle()
bdtb.getPageNum()
bdtb.getPostContent()
