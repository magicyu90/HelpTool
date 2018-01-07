# coding:utf-8
import time
from urllib import parse, error
from urllib.request import Request, urlopen
import json
from selenium import webdriver

driver = webdriver.Firefox(executable_path="/Users/hugo/dev/geckodriver")
driver.get('http:www.anjianba.cn')

username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
username.clear()
username.send_keys('000')
password.clear()
password.send_keys('123456')
loginBtn = driver.find_element_by_id('btn_Submit')
loginBtn.click()

ticket = driver.get_cookie('ticket')
data = json.loads(parse.unquote(ticket['value']))
token = data['access_token']
time.sleep(2)
# 用户管理
driver.find_element_by_link_text(u'用户管理').click()

try:
    req = Request('http://api.anjianba.cn//api/User/Query')
    req.add_header('Authorization', 'Bearer %s' % token)
    result = urlopen(req).read().decode('utf-8')
    result = json.loads(result)
    if result['success']:
        print(u'共%d用户:' % result['total'])
        for u in result['data']:
            print('姓名:%s,工号:%s,Id:%d' % (u['name'], u['accountNo'], u['id']))
    else:
        print('Api error:%s' % result['error'])
except error.URLError as e:
    print('Error:', e.reason)
finally:
    print('Done!')


time.sleep(1)
driver.close()
