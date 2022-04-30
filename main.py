from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
from bs4 import BeautifulSoup
import requests

#####################################################
# 기본설정
def chromeWebdriver():
    chrome_service = ChromService(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('exculdeSwithces', ['enable-logging'])
    driver = webdriver.Chrome(service=chrome_service, options=options)
    return driver

#####################################################

# 런어스 홈페이지 접속
url = "https://www.learnus.org/"
driver = webdriver.Chrome("c:\chromedriver.exe")
driver.implicitly_wait(10)
driver.get(url)
time.sleep(1)

#로그인창 들어가기
driver.find_element(By.CSS_SELECTOR, "#page-header > div.main-header.page-util > div > div.usermenu > ul > li > a.btn.btn-sm.btn-loginout").click()
time.sleep(1)

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#ssoLoginForm > div > div:nth-child(1) > input:nth-child(3)")
id.click()
id.send_keys("2021189045")
time.sleep(1)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#ssoLoginForm > div > div:nth-child(1) > input:nth-child(4)")
pw.click()
pw.send_keys("rkdckstn1!")
time.sleep(1)

#로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR,'#ssoLoginForm > div > div.form-group.form-group-submit > input')
login_btn.click()

###########################################

#수강 과목들 가져오기

driver.get("https://www.learnus.org/?lang=")
learnus_page_source = driver.page_source
soup = BeautifulSoup(learnus_page_source, 'html.parser')

course_title_list = soup.select('div.front-box-body.course_lists > ul > li > div > a > div > div.course-title > h3 ')
print("\n수강 과목:")
for title in course_title_list:
    print(title.text)


# 전체 알림 먼저 들어가기
time.sleep(1)
notification_btn1 = driver.find_element(By.CSS_SELECTOR, '#page-header > div.page-util > div.usermenu > ul > li.nav-item.nav-item-userinfo > button')
notification_btn1.click()
time.sleep(1)

notification_btn2 = driver.find_element(By.CSS_SELECTOR, '#page-userinfo > div > div.col-3.col-tab > div > a.nav-link.nav-link-noti')
notification_btn2.click()
time.sleep(1)

notification_btn3 = driver.find_element(By.CSS_SELECTOR, '#mCSB_3_container > div > div.userinfo-title > div > div:nth-child(2) > a')
notification_btn3.click()

# 알림 내용들 가져오기

driver.get("https://www.learnus.org/local/ubnotification/")
notification_page_source = driver.page_source
soup = BeautifulSoup(notification_page_source, 'html.parser')

notification_list = soup.select('#page-content > div > div > div.well.wellnopadding > a > div > div')
print("\n공지사항 업데이트:")
for list in notification_list:
    print(list.text)