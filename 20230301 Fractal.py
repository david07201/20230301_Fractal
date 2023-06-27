from tkinter import *
from tkinter import messagebox
import time
import random

def show():
    """顯示 H tree"""
    global color
    if order.get() >= 0:
        t1 = time.perf_counter_ns()
        canvas.delete('all')
        h_tree(order.get(), center, length)
        t2 = time.perf_counter_ns()
        label3.config(text=f'生成時間：{(t2 - t1) / 1_000_000} ms')
    else:
        messagebox.showerror('階數錯誤', '階層數必須大於等於 0 。')
        return        
    
def h_tree(order, center, length):
    """依指定階級樹繪製 H 樹碎形"""
    length /= 2
    p1 = (center[0] - length, center[1] - length) # 左上點
    p2 = (center[0] - length, center[1] + length) # 左下點
    p3 = (center[0] + length, center[1] - length) # 右上點
    p4 = (center[0] + length, center[1] + length) # 右下點
    
    r = hex(random.randint(50, 255)).ljust(4,'0')[2:]
    g = hex(random.randint(50, 255)).ljust(4,'0')[2:]
    b = hex(random.randint(50, 255)).ljust(4,'0')[2:]
    color = f'#{r}{g}{b}'

    draw_line(
        (center[0] - length, center[1]),
        (center[0] + length, center[1]), color) # 繪製 H 水平線
    draw_line(p1, p2, color) # 繪製 H 左垂直線
    draw_line(p3, p4, color) # 繪製 H 右垂直線

    order -= 1
    if order >= 0:
        h_tree(order, p1, length) # 遞迴左上點為中間點
        h_tree(order, p2, length) # 遞迴左下點為中間點
        h_tree(order, p3, length) # 遞迴右上點為中間點
        h_tree(order, p4, length) # 遞迴右下點為中間點

def draw_line(p1, p2, color):
    """繪製 p1 和 p2 之間的線條"""
    canvas.create_rectangle(
        p1[0], p1[1], p2[0], p2[1], width=0, fill=color)

WIDTH = 801
HEIGHT = 801
length = WIDTH // 2
center = (WIDTH//2 + 1, HEIGHT//2 + 1)
    
root = Tk()
root.title('H Tree')
root.config(bg='#B0B0B0')

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='#000000')
frame = Frame(root, bg='#B0B0B0')

canvas.pack()
frame.pack(padx=5, pady=5)

label = Label(frame, text='輸入階數：', bg='#B0B0B0')
order = IntVar()
order.set(0)
entry = Entry(frame, textvariable=order, width=3, justify='right')
button = Button(frame, text='顯示 H tree', command=show, bg='#B0B0B0')
label3 = Label(frame, text='生成時間：', bg='#B0B0B0')

label.pack(side='left')
entry.pack(side='left', padx=3)
button.pack(side='left')
label3.pack(side='left')

root.mainloop()