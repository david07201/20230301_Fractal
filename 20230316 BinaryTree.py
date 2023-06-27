from tkinter import *
from tkinter import messagebox
import time
import random

def show():
    if order.get() >= 0:
        t1 = time.perf_counter_ns()
        canvas.delete('all')
        center = (x, y)
        generate(order.get(), center, direction_current, length)
        t2 = time.perf_counter_ns()
        label3.config(text=f'生成時間：{(t2 - t1) / 1_000_000} ms')
    else:
        messagebox.showerror('階數錯誤', '階層數必須大於等於 0 。')
        return

def generate(order, center, direction_current, length):
    end = (round(center[0]+DIRECTION[direction_current][0]*length),
           round(center[1]+DIRECTION[direction_current][1]*length))
    r = hex(random.randint(50, 255)).ljust(4,'0')[2:]
    g = hex(random.randint(50, 255)).ljust(4,'0')[2:]
    b = hex(random.randint(50, 255)).ljust(4,'0')[2:]
    color = f'#{r}{g}{b}'
    draw_line(center, end, color)

    order -= 1
    if order >= 0:
        length *= RATIO
        direction_p1 = direction_current + 1
        direction_p1 %= 8
        direction_p2 = direction_current - 1
        direction_p2 %= 8
        generate(order, end, direction_p1, length)
        generate(order, end, direction_p2, length)

def draw_line(p1, p2, color):
    canvas.create_line(p1, p2, width=1, fill=color)


S = 1 / 2**0.5
RATIO = 0.58
DIRECTION = (
    (1, 0), (S, S), (0, 1), (-S, S),
    (-1, 0), (-S, -S), (0, -1), (S, -S)
)
direction_current = -2
WIDTH = 801
HEIGHT = 801
length = 300
x, y = 401, 801

root = Tk()
root.title('Binary Tree')
root.configure(bg='#B0B0B0')

canvas = Canvas(root, bg='#000000', width=WIDTH, height=HEIGHT)
frame = Frame(root, bg='#B0B0B0')
canvas.pack()
frame.pack()

label1 = Label(frame, text='階層：', bg='#B0B0B0')
order = IntVar()
order.set(0)
entry1 = Entry(frame, textvariable=order, justify='right', width=3)
button = Button(frame, text='生成',command=show, bg='#B0B0B0')
label3 = Label(frame, text='生成時間：', bg='#B0B0B0')
label1.pack(side='left')
entry1.pack(side='left')
button.pack(side='left', padx=5)
label3.pack(side='left')


root.mainloop()