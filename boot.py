#!/usr/bin/env python2
# coding=utf-8

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random

driver = webdriver.Firefox(executable_path='D:\\Firefox\\geckodriver.exe')
wait = WebDriverWait(driver, 10)
driver.maximize_window()
print(driver.get_window_size())
# driver.set_window_size(1024,768)
driver.get("http://pk.anjianba.cn")

name_box = driver.find_element_by_name("username")
name_box.clear()
name_box.send_keys(u'GoHHHHH')
start_btn = driver.find_element_by_class_name("mint-button")
start_btn.click()
time.sleep(3)
mask_btn = driver.find_element_by_class_name("a_page_btn_fix")
mask_btn.click()
time.sleep(3)
start_pk_btn = driver.find_element_by_class_name("pk-btn")
start_pk_btn.click()

match = 0
while (match < 10000):
    time.sleep(3)
    has_start = False

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'count-down')))
    i = 0
    clickable = False
    while (not clickable):
        if EC.visibility_of_element_located((By.CLASS_NAME, "count-down")):
            clickable = True
            print('可以点击啦？')
        else:
            print('*' * 20)
            time.sleep(0.2)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dr-image")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a_btn_safe")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a_btn_danger")))
    safe_btn = driver.find_element_by_class_name("a_btn_safe")
    danger_btn = driver.find_element_by_class_name("a_btn_danger")
    time.sleep(5)
    for i in range(10):
        found = False
        while (not found):
            try:
                img_elem = driver.find_element_by_class_name("dr-image")
                found = True
            except NoSuchElementException:
                time.sleep(1)
        img_src_url = img_elem.get_attribute("src")
        safe_btn.click()
        print('点击安全按钮')

        time.sleep(1)
        lichildren = driver.find_elements_by_xpath("//ul[@class='topic-result']//li[string-length(@class)>0]")
        print('当前结果:' + lichildren[len(lichildren) - 1].get_attribute('class'))

        i += 1
    match_result_out = False
    while (not match_result_out):
        try:
            again_btn = driver.find_element_by_xpath("//*[@id='btn-again']")
            again_btn.click()
            match_result_out = True
        except NoSuchElementException:
            time.sleep(5)
    match += 1

driver.close()
