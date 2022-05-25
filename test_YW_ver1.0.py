from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 이메일 보내기 기능 (네이버 이메일)
class my_mail(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.parent = parent
            self.initUI()

        # GUI 구성 요소 구현
        def initUI(self):
            self.parent.title("이메일 보내기")
            self.pack(fill=BOTH, expand=True)

            frame1 = Frame(self)
            frame1.pack(fill=X)
            frame2 = Frame(self)
            frame2.pack(fill=X)
            frame3 = Frame(self)
            frame3.place(x=5, y=100)
            frame4 = Frame(self)
            frame4.place(x=220, y=400)

            # frame1 (수신인)
            label = Label(frame1, text="수신인 :", width=8, font=("함초롱바탕", 10))
            label.pack(side=LEFT)
            string1 = StringVar(None)
            mail1 = Entry(frame1, textvariable=string1, width=55)
            mail1.pack(side="left", fill=X, padx=5, pady=10)

            # frame2 (제목)
            label = Label(frame2, text="제목 :", width=8, font=("함초롱바탕", 10))
            label.pack(side=LEFT)
            string2 = StringVar(None)
            mail2 = Entry(frame2, textvariable=string2, width=55)
            mail2.pack(side="left", fill=X, padx=5, pady=10)

            # frame3 (내용)
            label = Label(frame3, text="내용 :", width=8, font=("함초롱바탕", 10))
            label.pack(side=LEFT)

            def sendmail():
                html = False
                receiver = string1.get()
                subject = string2.get()
                body = mail3.get("1.0", "end-1c")
                server = smtplib.SMTP('smtp.naver.com', 587)

                # 메일 설정
                msg = MIMEMultipart()
                username = '#########@naver.com'   # 사용자의 네이버 이메일 대입
                password = '#############'         # 사용자의 네이버 어플리케이션 비밀번호 대입
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

            mail3 = Text(frame3, width=45, height=20)
            mail3.pack(side="left", fill=X)

            # frame4 (보내기 버튼)
            button = Button(frame4, height=1, width=10, text="보내기", command=sendmail)
            button.pack()

def emailmain():
    root = Tk()
    root.geometry("500x450")
    root.resizable(width=False, height=False)
    application = my_mail(root)
    root.mainloop()

emailmain()