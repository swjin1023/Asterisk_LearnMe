from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk


ex_dict = {'공학수학(3) (MAT2016.01-01) (1학기)': ['완료하지 못함: 6.1 Laplace Transform. Inverse Transform. Linearity. s-Shifting', '완료하지 못함: 6.2 Transforms of Derivatives and Integrals. ODEs ', '완료하지 못함: 13주 TA ', '완료하지 못함: vector space(optional)', '완료하지 못함: 12주 TA', '완료하지 못함: 6.1 Laplace Transform. Inverse Transform. Linearity. s-Shifting', '완료하지 못함: 6.2 Transforms of Derivatives and Integrals. ODEs ', '완료하지 못함: 13주 TA ', '완료하지 못함: 6.3 Unit Step Function. t-Shifting', '완료하지 못함: 6.4 Short Impulse. Diracs Delta Function. Partial Fractions', '완료하지 못함: 6.5 Convolution. Integral Equations', '완료하지 못함: 6.6 Differentiation and Integration of Transforms. ODEs with variable coefficients '], '회로이론 (SYS2101.01-00) (1학기)': ['Not completed: Homework 10', 'Not completed: Homework 1', 'Not completed: Homework 2', 'Not completed: Homework 3', 'Not completed: Homework 4', 'Not completed: Homework 5', 'Not completed: Homework 6', 'Not completed: Homework 7', 'Not completed: Homework 8', 'Not completed: Homework 9', 'Not completed: Homework 10'], '기초디지털논리회로 (SYS2103.01-00) (1학기)NEW': ['Not completed: On-line lecture on Mar 29', 'Not completed: WW5_1', 'Not completed: TEST 1 Result', 'Not completed: Lecture12_2'], '재료과학의기초 (SYS2104.01-00) (1학기)': [], '데이터구조및알고리즘 (SYS2105.01-00) (1학기)': ['Not completed: On-line lecture 2 on Mar 29', 'Not completed: LAB2 TA', 'Not completed: Test 1 Result', 'Not completed: WW11_2_1', 'Not completed: WW11_2_2', 'Not completed: WW11_2_3', 'Not completed: WW11_2_4', 'Not completed: WW12_2_1', 'Not completed: WW12_2_2', 'Not completed: WW12_2_3', 'Not completed: WW12_2_4', 'Not completed: WW12_2_5'], '시스템반도체개론 (SYS2106.01-00) (1학기)NEW': [], '탁구 (UCL1112.02-00) (1학기)': ['완료하지 못함: 토너먼트 공지'], '채플(C) (YCA1007.01-00) (1학기)': ['완료하지 못함: 3주차 영상', '완료하지 못함: 12주차 소감문', '완료하지 못함: 12주차 영상']}

ex_dict_list= list(ex_dict.keys())
window = Tk()
window.geometry("1300x600")
window.title("런어스 보조앱 (LearnMe)")
window.option_add("*Font", "맑은고딕 20")
window.configure(bg='light blue')

style = ttk.Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background="gray45")
style.map("TNotebook.Tab", background= [("selected", "gray80")])

notebook = ttk.Notebook(window, width=600, height=600)
notebook.pack(expand=True)
#

for key in ex_dict_list:
    frame1 = Frame(window,relief="solid", bd=2, background="white")
    notebook.add(frame1, text=key)
    text1 = Text(frame1)
    text1.pack()
    for list in ex_dict[key]:
        text1.insert(END ,list+'\n')

# frame2 = Frame(window,relief="solid",bd=2)
# notebook.add(frame2, text="회로이론")
# label2 = Label(frame2, text="페이지2의 내용")
# label2.pack(pady=20)
#
# frame3 = Frame(window,relief="solid",bd=2)
# notebook.add(frame3, text="기초디지털논리회로")
# label3 = Label(frame3, text="페이지3의 내용")
# label3.pack(pady=20)
#
# frame4 = Frame(window,relief="solid",bd=2)
# notebook.add(frame4, text="재료과학의기초")
# label4 = Label(frame4, text="페이지4의 내용")
# label4.pack(pady=20)
#
# frame5 = Frame(window,relief="solid",bd=2)
# notebook.add(frame5, text="데이터구조및알고리즘")
# label5 = Label(frame5, text="페이지5의 내용")
# label5.pack(pady=20)
#
# frame6 = Frame(window,relief="solid",bd=2)
# notebook.add(frame6, text="시스템반도체개론")
# label6 = Label(frame6, text="페이지6의 내용")
# label6.pack(pady=20)
#
# frame7 = Frame(window,relief="solid",bd=2)
# notebook.add(frame7, text="탁구")
# label7 = Label(frame7, text="페이지7의 내용")
# label7.pack(pady=20)
#
# frame8 = Frame(window,relief="solid",bd=2)
# notebook.add(frame8, text="페이지8")
# label8 = Label(frame8, text="페이지8의 내용")
# label8.pack(pady=20)
#
# frame9 = Frame(window,relief="solid",bd=2)
# notebook.add(frame9, text="페이지9")
# label9 = Label(frame9, text="페이지9의 내용")
# label9.pack(pady=20)


window.mainloop()