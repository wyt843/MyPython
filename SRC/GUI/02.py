#! /usr/bin/env python
# coding:utf-8

import tkinter

tk = tkinter.Tk()
tk.wm_title("Tkinter place 布局案例  输出九九 乘法表")
tk.maxsize(1000, 700) # 设置窗口最大 大小
tk.minsize(800, 450) # 设置窗口最大 大小

for y in range(1, 10):
    for x in range(1, 10):
        if x > y:
            break
        text = "{:2d} *{:2d} = {:2d}".format(x, y,x*y)
        label = tkinter.Label(tk, text=text)
        label.place(x=x*70, y=y*40, width=65, height=20, bordermode="outside")  # 指定位置切设置组件大小

tk.mainloop()