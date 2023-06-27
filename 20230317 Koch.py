from tkinter import *
from tkinter import messagebox
import time
import random

def show():
    if order.get() >= 0:
        t1 = time.perf_counter_ns()
        canvas.delete('all')
        p1 = (x, y - round(length/2/H), 1)
        p2 = (x + round(length/2), y + round(length/2*D/H), 3)
        p3 = (x - round(length/2), y + round(length/2*D/H), 5)
        points = (p1, p2, p3, p1)
        generate(order.get(), points, length)
        t2 = time.perf_counter_ns()
        label3.config(text=f'生成時間：{(t2 - t1) / 1_000_000} ms')
    else:
        messagebox.showerror('階數錯誤', '階層數必須大於等於 0 。')
        return

def generate(order, points, length):
    order -= 1
    total = len(points)
    if order >= 0:
        for i in range(0, total-1):
            p1 = points[i]
            p5 = points[i+1]
            direction_index = p1[2]
            new_direction_index_1 = new_direction(direction_index, -1)
            new_direction_index_2 = new_direction(direction_index, 1)
            new_length = round(length / 3)
            p2 = (p1[0] + round((p5[0]-p1[0])/3),
                  p1[1] + round((p5[1]-p1[1])/3), 
                  new_direction_index_1)
            p4 = (p1[0] + round(2*(p5[0]-p1[0]) / 3),
                  p1[1] + round(2*(p5[1]-p1[1]) / 3), 
                  direction_index)
            p3 = (p2[0] + new_length * DIRECTION[new_direction_index_1][0],
                  p2[1] + new_length * DIRECTION[new_direction_index_1][1],
                  new_direction_index_2)
            new_points = (p1, p2, p3, p4, p5)
            generate(order, new_points, new_length)
            
    else:
        for i in range(0, total-1):
            p1 = points[i][:2]
            p2 = points[i+1][:2]
            draw_line(p1, p2)

def draw_line(p1, p2):
    r = hex(random.randint(50, 255)).ljust(4,'0')[2:]
    g = hex(random.randint(50, 255)).ljust(4,'0')[2:]
    b = hex(random.randint(50, 255)).ljust(4,'0')[2:]
    color = f'#{r}{g}{b}'
    canvas.create_line(p1, p2, width=1, fill=color)

def new_direction(direction, a):
    direction += a
    direction %= 6
    return direction


H = 3**0.5 / 2
D = 1 / 2
DIRECTION = ((1, 0), (D, H), (-D, H), (-1, 0), (-D, -H), (D, -H))
WIDTH = 801
HEIGHT = 801
length = WIDTH - 120
x, y = (WIDTH+1) // 2, (HEIGHT+1) // 2

root = Tk()
root.title('Koch Snow Flake')
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