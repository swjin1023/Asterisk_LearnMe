from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import os
from bs4 import BeautifulSoup
import requests
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import threading
import time
import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

def LearnMe():
    # 런어스 로그인 함수
    def learnus_login(event):
        course_titles = []
        data_dict = {}

        # 로딩 보여주기
        p_var = DoubleVar()
        progressbar = ttk.Progressbar(root, maximum=100, length=350, variable=p_var)
        progressbar.pack()
        lab4 = Label(root)
        lab4.config(text="로딩중 0%")
        lab4.pack()

        # 런어스 홈페이지 접속
        driver = webdriver.Chrome(driver_path)
        url = "https://www.learnus.org/"
        driver.implicitly_wait(15)
        driver.get(url)
        time.sleep(1)

        # 로그인창 들어가기
        driver.find_element(By.CSS_SELECTOR,
                            "#page-header > div.main-header.page-util > div > div.usermenu > ul > li > a.btn.btn-sm.btn-loginout").click()
        time.sleep(1)

        lab4.config(text="로딩중 20%")
        p_var.set(20)
        progressbar.update()
        lab4.update()

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

        lab4.config(text="로딩중 30%")
        p_var.set(30)
        progressbar.update()
        lab4.update()

        try:
            # 로그인 버튼
            login_btn = driver.find_element(By.CSS_SELECTOR,
                                            '#ssoLoginForm > div > div.form-group.form-group-submit > input')
            login_btn.click()

            s = requests.Session()
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"}
            s.headers.update(headers)

            for cookie in driver.get_cookies():
                c = {cookie['name']: cookie['value']}
                s.cookies.update(c)

        except:
            print("아이디 비번 오류")
            lab4.config(text="아이디 또는 비번이 틀립니다. 다시 입력해주세요")
            lab4.update()
            progressbar.destroy()
            driver.close()
            return

        req = s.get("https://www.learnus.org/?lang=ko")
        soup = BeautifulSoup(req.content, 'html.parser')

        lab4.config(text="로딩중 40%")
        p_var.set(40)
        progressbar.update()
        lab4.update()

        course_title_list = soup.findAll("h3")
        course_title_url = soup.findAll("a", attrs={"class": "course-link"})
        keywords = ["완료하지 못함", "Not completed"]
        num = 40

        for title, url in zip(course_title_list, course_title_url):
            print("\n" + title.text)
            req1 = s.get(url["href"])
            soup = BeautifulSoup(req1.content, 'html.parser')
            uncompleted_list = soup.findAll("img", attrs={"class": "icon"})

            num += 60 // len(course_title_list)
            loading_num = "로딩중 " + str(num) + "%"
            lab4.config(text=loading_num)
            p_var.set(num)
            progressbar.update()
            lab4.update()
            list1 = []

            for lists in uncompleted_list:
                uncompleted_VOD = lists.parent.parent.previous_sibling
                if "완료하지 못함" in lists["alt"] or "Not completed" in lists["alt"]:
                    if "Zoom meeting" not in uncompleted_VOD.contents[0].find("img")["alt"] and "file" not in \
                            uncompleted_VOD.contents[0].find("img")["alt"] \
                            and "URL링크" not in uncompleted_VOD.contents[0].find("img")["alt"]:
                        print(lists["alt"] + " <" + uncompleted_VOD.contents[0].find("img")["alt"] + ">")
                        course_titles.append(title.text)
                        list1.append(lists["alt"])
                data_dict[title.text] = list1

        lab4.config(text="로딩 완료")
        p_var.set(100)
        progressbar.update()
        data_dict_list = list(data_dict.keys())
        print(data_dict)
        print(data_dict_list)
        lab4.update()
        driver.close()

        # 함수 정의
        def new_window():
            root.destroy()

            window = Tk()
            window.geometry("1300x600")
            window.title("런어스 보조앱 (LearnMe)")
            window.option_add("*Font", "맑은고딕 20")
            window.configure(bg='light blue')

            style = ttk.Style()
            style.theme_use('default')
            style.configure('TNotebook.Tab', background="gray45")
            style.map("TNotebook.Tab", background=[("selected", "gray80")])

            notebook = ttk.Notebook(window, width=600, height=600)
            notebook.pack(expand=True)

            for key in data_dict_list:
                frame1 = Frame(window, relief="solid", bd=2, background="white")
                notebook.add(frame1, text=key)
                text1 = Text(frame1)
                text1.pack()
                for list1 in data_dict[key]:
                    text1.insert(END, list1 + '\n')

            window.mainloop()

        new_window()

    # 런어스 로그인 함수 쓰레드를 만들기
    def login(event):
        threading.Thread(target=learnus_login).start()

    def loading_progress(window, setnum):
        # 로딩 보여주기
        p_var = DoubleVar()
        progressbar = ttk.Progressbar(root, maximum=100, length=350, variable=p_var)
        progressbar.pack()
        lab4 = Label(window)
        lab4.config(text="로딩중 " + setnum + "%")
        lab4.pack()
        p_var.set(setnum)
        progressbar.update()
        lab4.update()

    ###########################################################

    # tkinter 라이브러리를 이용하여 GUI 만들기#
    # 단순히 이메일 보내기 버튼 추가해서 함수 연결시 올바른 수신자 주소 입력했음에도 SMRPRecipientsRefused 에러 발생...
    # sol -> '이메일 보내기' 버튼 클릭 시 Toplevel이 추가 팝업창 표시
    # 부모 위젯을 생성된 최상위 창으로 변경해주기 위한 작업 필요

    def createnew():
        newWindow = tk.Toplevel(root)
        newWindow.geometry("550x500")
        newWindow.title('이메일 보내기')
        newWindow.resizable(width=False, height=False)

        label = Label(newWindow, text="수신인 : ", width=9, font=("맑은 고딕", 10))
        label.pack()
        string1 = StringVar(None)
        mail1 = Entry(newWindow, textvariable=string1, width=15)
        mail1.pack(padx=5, pady=10)

        label = Label(newWindow, text="제목 : ", width=9, font=("맑은 고딕", 10))
        label.pack()
        string2 = StringVar(None)
        mail2 = Entry(newWindow, textvariable=string2, width=15)
        mail2.pack(padx=5, pady=10)

        label = Label(newWindow, text="내용 : ", width=8, font=("맑은 고딕", 10))
        label.pack()
        mail3 = Text(newWindow, width=30, height=10)
        mail3.pack()

        def sendmail():
            html = False
            receiver = string1.get()
            subject = string2.get()
            body = mail3.get("1.0", "end-1c")
            server = smtplib.SMTP('smtp.naver.com', 587)

            # 메일 설정
            msg = MIMEMultipart()
            username = '#######'  # 사용자의 네이버 이메일 대입
            password = '#######'  # 사용자의 네이버 비밀번호 대입(2단계 인증 사용시 어플리케이션 비밀번호 발급 후 대입)
            msg['From'] = username
            msg['To'] = receiver
            msg['Subject'] = subject

            if html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))

            # 서버에 로그인
            server.starttls()
            server.login(username, password)
            # 메일 보내기
            mail = msg.as_string()
            server.sendmail(username, receiver, mail)

            # frame4 (보내기 버튼)
        button = Button(newWindow, height=1, width=7, text="보내기", font=("맑은 고딕", 10), command=sendmail)
        button.pack()

        newWindow.mainloop()

    class UI(tk.Frame): # tkinter UI class
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            master.geometry("900x600") # 아래 4줄 : 제목 표시줄
            master.title("런어스 보조앱 (LearnMe)")
            master.iconbitmap(default='learnus_logo.ico')
            master.option_add("*Font", "맑은고딕 20")
            self.pack()
            self.create_logo()
            self.create_id()
            self.create_pw()
            self.login()

        def create_logo(self): # learnus 로고 넣기
            lab_d = tk.Label(self.master)
            img = tk.PhotoImage(file="learnus_logo.png")
            lab_d.config(image=img)
            lab_d.image = img
            lab_d.pack()

        def create_id(self): # id 라벨과 입력창
            lab1 = tk.Label(self.master)
            lab1.config(text="학번")
            lab1.pack()
            global ent1
            ent1 = tk.Entry(self.master)
            ent1.pack()


        def create_pw(self): # pw 라벨과 입력창
            lab2 = tk.Label(self.master)
            lab2.config(text="비밀번호")
            lab2.pack()
            global ent2
            ent2 = tk.Entry(self.master)
            ent2.config(show="*")
            ent2.bind("<Return>", learnus_login) # Enter 누르면 로그인
            ent2.pack()


        def login(self): # 로그인 버튼
            btn = tk.Button(self.master)
            btn.config(width=10, height=1)
            btn.config(text="로그인")
            btn.bind("<Button-1>", learnus_login) # 로그인 버튼 왼쪽 클릭하면 로그인
            btn.pack()

    root = tk.Tk()
    LearnUs_app = UI(master=root)
    LearnUs_app.mainloop()


########################################################
LearnMe()
