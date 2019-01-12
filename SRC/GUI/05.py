#! /usr/bin/env python
# coding:utf-8

import tkinter

def pop(event):
    popMenu = tkinter.Menu(window)
    for item in ["弹出菜单", "查看", "下载", "上传"]:
        popMenu.add_command(label=item)
    popMenu.post(event.x_root, event.y_root) #菜单弹出

window = tkinter.Tk()

window.bind("<Button-3>", pop)

menubar = tkinter.Menu(window)

edit = tkinter.Menu(menubar)
for item in ["Copy", "Paste", "Cut"]:
    edit.add_command(label=item)
    edit.add_separator() # 添加分割符

for item in ["File", "Edit", "View"]:
    if item == "Edit":
        menubar.add_cascade(label=item, menu=edit)
    else:
        menubar.add_command(label=item)

window["menu"] = menubar

window.mainloop()