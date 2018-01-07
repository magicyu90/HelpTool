# coding:utf-8
import time
import datetime
import json
import random
from urllib import parse, error
from selenium import webdriver
from urllib.request import Request, urlopen


class AnjianbaBa:
    '''
    安检培训系统爬虫工具
    '''

    def __init__(self, url):
        self.driver = webdriver.Firefox(
            executable_path="/Users/hugo/dev/geckodriver")
        self.driver.get(url)
        username = self.driver.find_element_by_id('username')
        password = self.driver.find_element_by_id('password')
        username.clear()
        password.clear()
        username.send_keys('000')
        password.send_keys('123456')
        loginBtn = self.driver.find_element_by_id('btn_Submit')
        loginBtn.click()
        time.sleep(2)
        ticket = self.driver.get_cookie('ticket')
        data = json.loads(parse.unquote(ticket['value']))
        self.token = data['access_token']
        self.orgIds = []

    def clickOrg(self, item, level):
        '''
        递归展开组织机构节点并记录相应节点ID
        '''
        # 展开节点
        item.find_elements_by_xpath("*")[0].click()
        time.sleep(1)
        lis = item.find_elements_by_xpath(
            "//ul[@class='level%d ']//li[@class='level%d']" % (level, level + 1))
        if lis:
            for li in lis:
                if li.get_attribute('id') not in self.orgIds:
                    self.orgIds.append(li.get_attribute('id'))
                currentLevel = int(li.get_attribute('class')[5:])
                self.clickOrg(li, currentLevel)

    def getUsers(self):
        '''
        获取用户信息
        '''
        try:
            进入用户管理页面
            self.driver.find_element_by_link_text(u'用户管理').click()
            time.sleep(1)
            req = Request('http://api.anjianba.cn//api/User/Query')
            req.add_header('Authorization', 'Bearer %s' % self.token)
            result = json.loads(urlopen(req).read().decode('utf-8'))
            if result['success']:
                print(u'共%d用户:' % result['total'])
                for user in result['data']:
                    print('姓名:%s,工号:%s,ID:%d' %
                          (user['name'], user['accountNo'], user['id']))
            else:
                print('获取用户出错，错误信息:%s' % result['error'])
        except error.URLError as e:
            print('URLError:', e.reason)

    def addUser(self):
        '''
        新增用户
        '''
        try:
            # 进入用户创建页面
            self.driver.find_element_by_link_text(u'用户管理').click()
            time.sleep(1)
            self.driver.find_element_by_id('add_userinfo').click()
            appendix = time.strftime('%H:%M')
            # 姓名
            self.driver.find_element_by_id(
                'input_userName').send_keys('spider %s' % appendix)
            time.sleep(1)
            # 工号
            self.driver.find_element_by_id('input_jobNo').send_keys('ssadsa12')
            time.sleep(1)
            # 身份类型
            self.driver.find_element_by_id('input_userType').click()
            time.sleep(1)
            userType = self.driver.find_element_by_xpath(
                "//ul[@id = 'input_userType-select']//li[@data-select-id='%s']" % str(random.randint(1, 3)))
            userType.click()
            time.sleep(1)
            # 机构
            self.driver.find_element_by_id('input_userOrg').click()
            time.sleep(1)
            orgs = self.driver.find_elements_by_xpath(
                "//ul[@id = 'ul_ztree_input_userOrg']//li[@class='level0']")
            for org in orgs:
                self.clickOrg(org, 0)
            orgCount = len(self.orgIds)
            self.driver.find_element_by_id(
                self.orgIds[random.randint(0, orgCount - 1)]).find_elements_by_xpath('*')[1].click()
            time.sleep(1)
            # 技能
            self.driver.find_element_by_id('input_grade').click()
            time.sleep(1)
            grade = self.driver.find_element_by_xpath(
                "//ul[@id = 'input_grade-select']//li[@data-select-id='%s']" % str(random.randint(1, 4)))
            grade.click()
            time.sleep(1)
            # 岗位
            self.driver.find_element_by_id('input_post').click()
            time.sleep(1)
            position = self.driver.find_element_by_xpath(
                "//ul[@id = 'input_post-select']//li[@data-select-id='%s']" % str(random.randint(1, 4)))
            position.click()
            time.sleep(1)

            # 提交
            self.driver.find_element_by_id('btn_submit').click()

        except expression as identifier:
            pass
        finally:
            pass


aj_spider = AnjianbaBa('http:www.anjianba.cn')
# aj_spider.getUsers()
aj_spider.addUser()
