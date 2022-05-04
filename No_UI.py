from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import os
import time

#####################################################
# 기본설정 크롬드라이버 자동다운
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"ChromeDriver is installed: {driver_path}")
else:
    print(f"install the ChromeDriver(ver: {chrome_ver})")
    chromedriver_autoinstaller.install(True)
####################################################
driver = webdriver.Chrome(driver_path)
url = "https://www.learnus.org/"
driver.implicitly_wait(5)
driver.get(url)
time.sleep(1)

# 로그인창 들어가기
driver.find_element(By.CSS_SELECTOR,
                    "#page-header > div.main-header.page-util > div > div.usermenu > ul > li > a.btn.btn-sm.btn-loginout").click()
time.sleep(1)

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#ssoLoginForm > div > div:nth-child(1) > input:nth-child(3)")
id.click()
id.send_keys("2021189045")

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#ssoLoginForm > div > div:nth-child(1) > input:nth-child(4)")
pw.click()
pw.send_keys("비번")

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, '#ssoLoginForm > div > div.form-group.form-group-submit > input')
login_btn.click()

while(True):
    pass



