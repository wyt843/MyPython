#! /usr/bin/env python
# coding:utf-8

import tkinter
import math

'''
获取五角星，五个顶点坐标
'''
def wjx(x,y,r):

    a = math.sin(math.radians(18)) * r
    b = math.cos(math.radians(18)) * r

    a2 = math.sin(math.radians(54)) * r
    b2 = math.cos(math.radians(54)) * r

    points = [
        (x, y - r),
        (x + b, y - a),
        (x - b, y - a),
        (x - b2, y + a2),
        (x + b2, y + a2)
    ]
    return points

window = tkinter.Tk()

cvs = tkinter.Canvas(window, width=400, height=300)
cvs.pack()

cvs.create_line(0, 150, 400, 150)
cvs.create_text(100, 150, text="五角星")

# 画一个五角星
points = wjx(200, 150, 100)
line = math.sin(math.radians(36)) * 100 * 2
for p1 in points:
    for p2 in points:
        dis2 = abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2
        dis = math.sqrt( dis2 )
        if dis <= line: # 两点之间的距离为正五角星边长
            continue
        cvs.create_line(p1[0], p1[1], p2[0], p2[1])

window.mainloop()


