from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def learn_us_email():
    # 창 띄우기
    window = Tk()
    window.geometry('450x400')
    window.title('이메일 보내기')
    window.resizable(width=False, height=False)

    # 수신인
    label = Label(window, text="수신인 : ", width=9, font=("맑은 고딕", 10))
    label.pack()
    string1 = StringVar(None)
    mail1 = Entry(window, textvariable=string1, width=25)
    mail1.pack(padx=5, pady=10)

    # 제목
    label = Label(window, text="제목 : ", width=9, font=("맑은 고딕", 10))
    label.pack()
    string2 = StringVar(None)
    mail2 = Entry(window, textvariable=string2, width=25)
    mail2.pack(padx=5, pady=10)

    # 내용
    label = Label(window, text="내용 : ", width=8, font=("맑은 고딕", 10))
    label.pack()
    mail3 = Text(window, width=55, height=15)
    mail3.pack()

    def sendmail():
        html = False
        receiver = string1.get()
        subject = string2.get()
        body = mail3.get("1.0", "end-1c")
        server = smtplib.SMTP('smtp.naver.com', 587)

        # 메일 설정
        msg = MIMEMultipart()
        username = '########'  # 사용자의 네이버 이메일 대입
        password = '########'  # 사용자의 네이버 비밀번호 대입(2단계 인증 사용시 어플리케이션 비밀번호 발급 후 대입)
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
        server.quit()

    # 보내기 버튼
    button = Button(window, height=1, width=7, text="보내기", font=("맑은 고딕", 10), command=sendmail)
    button.pack()

    window.mainloop()

#############################################
learn_us_email()