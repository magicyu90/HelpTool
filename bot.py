import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox(executable_path = 'D:\\Firefox\\geckodriver.exe')
driver.get("http://mobile.anjianba.cn")

name_box = driver.find_element_by_name("username")
name_box.clear()
name_box.send_keys(u"李栋")
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
    time.sleep(7)
    i = 0
    for i in range(10):
        found = False
        while (not found):
            try:
                img_elem = driver.find_element_by_class_name("dr-image")
                found = True
            except NoSuchElementException:
                time.sleep(1)
        img_src_url = img_elem.get_attribute("src")
        # image recognition algorithm could be added here, maybe next time :)
        if "safe" in img_src_url:
            safe_btn = driver.find_element_by_class_name("a_btn_safe")
            safe_btn.click()
        else:
            danger_btn = driver.find_element_by_class_name("a_btn_danger")
            danger_btn.click()
        time.sleep(1)
        i += 1
    match_result_out = False
    while (not match_result_out):
        try:
            again_btn = driver.find_element_by_xpath("//*[@id='btn-again']")
            again_btn.click()
            match_result_out = True
        except NoSuchElementException:
            time.sleep(1)
    match += 1

driver.close()