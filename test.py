## main에 합치기 전에 코드 연습용 ##

from tkinter import *

win = Tk()
win.geometry("900x600")
win.title("런어스 보조앱 (LearnMe)")
#옆에 제목 그림은 런어스로 넣자

win.option_add("*Font", "맑은고딕 20")

#######################################
#런어스 로고
lab_d = Label(win)
img=PhotoImage(file="learnus_logo.png")
lab_d.config(image=img)
lab_d.pack()
#id 라벨과 입력창
lab1=Label(win)
lab1.config(text="학번")
lab1.pack()
ent1=Entry(win)
ent1.pack()
#pw 라벨과 입력창
lab2=Label(win)
lab2.config(text="비밀번호")
lab2.pack()
ent2=Entry(win)
ent2.config(show="*")
ent2.pack()
######################################
btn = Button(win)
btn.config(width=10, height=1)
btn.config(text="로그인")
def login():
    my_id = ent1.get()
    my_pw = ent2.get()
    print(my_pw,my_id)

btn.config(command=login)
btn.pack()
######################################
win.mainloop()