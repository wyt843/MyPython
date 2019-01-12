#! /usr/bin/env python
# coding:utf-8

import tkinter

def baseLabel(event):
    global tk
    print(event)
    lb = tkinter.Label(tk, text="事件显示")
    lb.pack()

def submit():
    global tk,i
    print("登录成功，密码:{}".format(i.get()))
    tk.destroy() # 关闭窗口

tk = tkinter.Tk()
tk.wm_title("事件 案例")

lb = tkinter.Label(tk, text="label 模拟 button")
lb.bind("<Button-1>", baseLabel)
lb.pack()

i = tkinter.Entry(tk)
i["show"] = "*" # 设置掩码
i.pack()

btn = tkinter.Button(tk, text="submit")
btn.bind("<Button-1>", submit)
btn.pack()

tk.mainloop()
