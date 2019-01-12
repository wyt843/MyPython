#! /usr/bin/env python
# coding:utf-8

import tkinter

# 创建窗口对象
base = tkinter.Tk()

def initScreen():
    base.wm_title("Tkinter 窗口")

    li = ['C', 'Python', 'PHP', 'SQL', 'Java']

    label = tkinter.Label(base, text="Label")
    label.pack()  # 指定布局

    label2 = tkinter.Label(base, text="绿色 label", background="green")
    label2.pack(padx=4, pady=4)  # 指定布局

    button = tkinter.Button(base, text="Button", command=showLabel)
    button.pack(side=tkinter.RIGHT, expand=tkinter.NO, fill=tkinter.X)
    # 窗口上创建列表组件
    listb = tkinter.Listbox(base)
    # 列表组件 添加数据
    for item in li:
        listb.insert(0, item)
    listb.pack()
    # 进入消息循环
    base.mainloop()

def showLabel():
    global base
    lb = tkinter.Label(base, text="显示Label")
    lb.pack(side=tkinter.RIGHT)

if __name__ == '__main__':
    initScreen()


