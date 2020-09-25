"""
main.py

Grapher ver 1.0

This program developed linear function as turtle module (built-in)
일차함수 그래프 뷰어를 터틀 모듈로 구현했습니다.
이 프로그램은 macOS 14.0에서 개발되었습니다. Windows에서는 작동하지 않을 수 있습니다.
문제가 생겼을 때는 go2ysj@gmail.com으로 메일보내주시면 감사하겠습니다.
"""

import turtle as t
from tkinter import *

print("(LOG) started all task")

# metadata
meta = {
    "basis size": 50
}
screen = t.Screen()
screen.setup(500, 500)
print("(LOG) setted metadata")

# gui
window = Tk()
window.title("Grapher")
title = Label(master=window, text="y = ax + b")
title.pack()
label_1 = Label(master=window, text="기울기(a)")
label_1.pack()
entry_1 = Entry(window)
entry_1.pack()
label_2 = Label(master=window, text="편향(b)")
label_2.pack()
entry_2 = Entry(window)
entry_2.pack()


def make():
    """
    graph make
    """
    # function
    a = int(Entry.get(entry_1))
    b = int(Entry.get(entry_2))
    y = lambda x: a * x + b
    print("(LOG) setted function system")

    # graphFrameDrawer
    print("(LOG) started draw graph frame")
    graphFrameDrawer = t.Turtle()
    graphFrameDrawer.speed(10)
    graphFrameDrawer.penup()
    graphFrameDrawer.goto(-400, 0)
    graphFrameDrawer.pendown()
    graphFrameDrawer.goto(400, 0)
    graphFrameDrawer.penup()
    graphFrameDrawer.goto(0, -400)
    graphFrameDrawer.pendown()
    graphFrameDrawer.goto(0, 400)
    print("(LOG) ended draw graph frame")

    # graphLineDrawer
    print("(LOG) started draw graph line")
    graphLineDrawer = t.Turtle()
    graphLineDrawer.pensize(2)
    graphLineDrawer.pencolor("blue")
    graphLineDrawer.speed(10)
    graphLineDrawer.penup()
    graphLineDrawer.goto(-400, 0)
    graphLineDrawer.pendown()

    for x_ in range(-300, 300):
        graphLineDrawer.goto(x_, y(x_))
    print("(LOG) ended draw graph line")
    print("(LOG) ended all task. You can close now.")
    t.mainloop()


button = Button(master=window, text="실행", command=make)
button.pack()
window.mainloop()
