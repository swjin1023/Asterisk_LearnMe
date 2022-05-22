from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import os
from bs4 import BeautifulSoup
import requests
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
driver.implicitly_wait(15)
driver.get(url)
time.sleep(1)

# 로그인창 들어가기
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
pw.send_keys("비번")
time.sleep(1)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, '#ssoLoginForm > div > div.form-group.form-group-submit > input')
login_btn.click()

s= requests.Session()
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"}
s.headers.update(headers)

for cookie in driver.get_cookies():
    c= {cookie['name']:cookie['value']}
    s.cookies.update(c)

req = s.get("https://www.learnus.org/?lang=ko")
soup = BeautifulSoup(req.content, 'html.parser')
course_title_list = soup.findAll("h3")
course_title_url = soup.findAll("a", attrs={"class":"course-link"})

for title,url in zip(course_title_list,course_title_url):
    print(title.text)
    req1 = s.get(url["href"])
    soup = BeautifulSoup(req1.content, 'html.parser')
    uncompleted_list = soup.findAll("img", attrs={"class": "icon"})
    for list in uncompleted_list:
        print(list)
#for url in course_title_url:
    #print(url["href"])


