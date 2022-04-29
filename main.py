from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
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
url = "https://www.learnus.org/login.php?errorcode=4"
browser = webdriver.Chrome("c:\chromedriver.exe")
browser.implicitly_wait(10)
browser.get(url)
time.sleep(1)

# 아이디 입력창
id = browser.find_element(By.CSS_SELECTOR, "#ssoLoginForm > div > div:nth-child(1) > input:nth-child(3)")
id.click()
id.send_keys("2021189045")
time.sleep(1)

# 비밀번호 입력창
pw = browser.find_element(By.CSS_SELECTOR, "#ssoLoginForm > div > div:nth-child(1) > input:nth-child(4)")
pw.click()
pw.send_keys("rkdckstn1!")
time.sleep(1)

#로그인 버튼
login_btn = browser.find_element(By.CSS_SELECTOR,"#ssoLoginForm > div > div.form-group.form-group-submit > input")
login_btn.click()

