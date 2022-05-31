from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import os
from bs4 import BeautifulSoup
import requests
from tkinter import messagebox
import tkinter as tk
import threading
import time
import keyboard

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

# headless Chrome
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36')
driver = webdriver.Chrome(driver_path)

#수강과목 리스트
course_list = []

#런어스 로그인 함수
class LearnUs:

    def __init__(self, string):
        self.coursename = string

    def learnuslogin(self):
        # 런어스 홈페이지 접속
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
        id.send_keys(ent1.get())
        time.sleep(1)

        # 비밀번호 입력창
        pw = driver.find_element(By.CSS_SELECTOR, "#ssoLoginForm > div > div:nth-child(1) > input:nth-child(4)")
        pw.click()
        pw.send_keys(ent2.get())
        time.sleep(1)

        # 로그인 버튼
        login_btn = driver.find_element(By.CSS_SELECTOR,
                                        '#ssoLoginForm > div > div.form-group.form-group-submit > input')
        login_btn.click()
        time.sleep(2)
        driver.refresh()

        if driver.current_url == 'https://www.learnus.org/login.php':
            messagebox.showinfo("오류", "아이디나 비밀번호가 잘못되었습니다.")  # 메시지 박스를 띄운다.
            driver.quit()
            win.quit()
            win.mainloop()
        elif driver.current_url == 'https://www.learnus.org/?lang=':
            pass



    def course_list_selenium(self):
        # 수강 과목들 가져오기
        driver.get("https://www.learnus.org/?lang=")
        learnus_page_source = driver.page_source
        soup = BeautifulSoup(learnus_page_source, 'html.parser')

        course_title_list = soup.select(
            'div.front-box-body.course_lists > ul > li > div > a > div > div.course-title > h3 ')
        print("\n수강 과목:")
        for title in course_title_list:
            title_in_text = title.text.replace('(1학기)', '')
            title_in_text_class = LearnUs(title_in_text)
            print(title_in_text)
            a = []
            a.append(title_in_text)
            course_list.append



    def notification_pull(self):
        driver.get("https://www.learnus.org/local/ubnotification/")
        notification_page_source = driver.page_source
        soup = BeautifulSoup(notification_page_source, 'html.parser')

        notification_list = soup.select('#page-content > div > div > div.well.wellnopadding > a > div > div')
        print("\n공지사항 업데이트:")
        for list in notification_list:
            print(list.text)

    def course_list_requests(self):
        # 수강 과목들 가져오기


        """
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
        """
    # 알림 내용들 가져오기





    driver.close()
    print("드라이버 종료")


#런어스 로그인 함수 쓰레드를 만들기
def login(event):
    threading.Thread(target=learnus_login).start()

#####################################################
#tkinter 라이브러리를 이용하여 GUI 만들기#

class UI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_logo()
        self.create_id()
        self.create_pw()
        self.login()

    def create_logo(self):
        lab_d = tk.Label(self.master)
        img = tk.PhotoImage(file="learnus_logo.png")
        lab_d.config(image=img)
        lab_d.pack()

    def create_id(self):
        lab1 = tk.Label(self.master)
        lab1.config(text="학번")
        lab1.pack()
        ent1 = tk.Entry(self.master)
        ent1.pack()

    def create_pw(self):
        lab2 = tk.Label(self.master)
        lab2.config(text="비밀번호")
        lab2.pack()
        ent2 = tk.Entry(self.master)
        ent2.config(show="*")
        ent2.bind("<Return>", login)
        ent2.pack()


    def login(self):
        btn = tk.Button(self.master)
        btn.config(width=10, height=1)
        btn.config(text="로그인")
        btn.bind("<Button-1>", login)
        btn.pack()

root = tk.Tk()
root.geometry("900x600")
root.title("런어스 보조앱 (LearnMe)")
root.iconbitmap(default='learnus_logo.ico')
root.option_add("*Font", "맑은고딕 20")
LearnUs_app = UI(master=root)
LearnUs_app.mainloop()


#로그인 버튼 넣기

#Enter 누르면 로그인


#로그인 버튼 왼쪽 클릭하면 로그인




