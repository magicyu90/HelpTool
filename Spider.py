from urllib import request
from bs4 import BeautifulSoup
import re

# 进入主函数
if __name__ == '__main__':
    response = request.urlopen("http://blog.magicyu.com/")
    content = response.read().decode('utf-8')

    # print('info信息:', response.info())
    # print('info Server信息:', response.info()['Server'])
    # print('header:', response.headers)
    soup = BeautifulSoup(content, 'html.parser')
    print('页面标题:', soup.title.text)
    index = 1
    for postTitle in soup.find_all('a', class_='post-title-link'):
        print('number:%d,title:%s' % (index, postTitle.text))
        index += 1

    for h1 in soup.find_all('h1', attrs={"itemprop": re.compile('^name h')}):
        print(h1)
