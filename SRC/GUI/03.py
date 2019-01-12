#! /usr/bin/env python
# coding:utf-8

import tkinter

tk = tkinter.Tk()

def btn_response():
    global input1, input2
    print("用户：{}  密码：{}".format(input1.get(), input2.get()))

tk.wm_title("Tkinter grid 布局案例")
tk.maxsize(1000, 300) # 设置窗口最大 大小
tk.minsize(700, 250) # 设置窗口最大 大小

label1 = tkinter.Label(tk, text="用户名")
label2 = tkinter.Label(tk, text="密码")
input1 = tkinter.Entry(tk)
input2 = tkinter.Entry(tk)
btn = tkinter.Button(tk,text="commit", command=btn_response)

label1.grid(column=0, row=0)
label2.grid(column=0, row=1)
input1.grid(column=1, row=0)
input2.grid(column=1, row=1)
btn.grid(column=1, row=2)

tk.mainloop()