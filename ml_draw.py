from tkinter import *
import PIL
from PIL import Image, ImageDraw
import numpy as np 
import pandas as pd


def clear_canvas():
    cv.delete("all")
    cv["bg"] = "black"
    draw.rectangle((0, 0, 560, 560), width=0, fill="black")

def activate_paint(event):
    x1, y1 = (event.x - 10), (event.y - 10)
    x2, y2 = (event.x + 10), (event.y + 10)
    cv.create_oval((x1, y1, x2, y2), fill='white', outline="white", width=25)
    draw.ellipse((x1, y1, x2, y2), width=25)

    image_gray = np.array(image1.convert('L'))
    window_size = 20
    result = np.zeros((28, 28))
    for i in range(0, 560, window_size):
        for j in range(0, 560, window_size):
            result[i // window_size, j // window_size] = np.max(image_gray[i:i + window_size, j:j + window_size])
    
    result = (result / 255) * 0.99 + 0.01
    result = result.reshape(784)
    outputs = forward_prop(result)
    outputs = outputs / np.sum(outputs) * 100
    outputs = ['{:0.2f}'.format(x) for x in outputs]
    for i in range(10):
        labels[i]["text"] = f"{i} -> {outputs[i]}%".ljust(11)
    


w1 = pd.read_csv("w1_test.csv")
w2 = pd.read_csv("w2_test.csv")

def forward_prop(input_values):
    x = input_values
    weights = [w1, w2]
    for w in weights:
        x = 1 / (1 + np.exp(-np.dot(w, x)))
    return x

root = Tk()
root.config(bg="black")
root.title("Определитель числа")
root.resizable(width=False, height=False)

cv = Canvas(root, width=560, height=560, bg='black')

image1 = PIL.Image.new('RGB', (560, 560), 'black', )
draw = ImageDraw.Draw(image1)

control_frame = Frame(root, width=440, bg="black")
control_frame.pack(side=RIGHT)

l0 = Label(control_frame, text="0 -> 0.00%", font=("Arial", 20), bg="black", fg="white")
l0.grid(row=0, column=0)
l1 = Label(control_frame, text="1 -> 0.00%", font=("Arial", 20), bg="black", fg="white")
l1.grid(row=1, column=0)
l2 = Label(control_frame, text="2 -> 0.00%", font=("Arial", 20), bg="black", fg="white")
l2.grid(row=2, column=0)
l3 = Label(control_frame, text="3 -> 0.00%", font=("Arial", 20), bg="black", fg="white")
l3.grid(row=3, column=0)
l4 = Label(control_frame, text="4 -> 0.00%", font=("Arial", 20), bg="black", fg="white")
l4.grid(row=4, column=0)
l5 = Label(control_frame, text="5 -> 0.00%", font=("Arial", 20), bg="black", fg="white")
l5.grid(row=5, column=0)
l6 = Label(control_frame, text="6 -> 0.00%", font=("Arial", 20), bg="black", fg="white")
l6.grid(row=6, column=0)
l7 = Label(control_frame, text="7 -> 0.00%", font=("Arial", 20), bg="black", fg="white")
l7.grid(row=7, column=0)
l8 = Label(control_frame, text="8 -> 0.00%", font=("Arial", 20), bg="black", fg="white")
l8.grid(row=8, column=0)
l9 = Label(control_frame, text="9 -> 0.00%", font=("Arial", 20), bg="black", fg="white")
l9.grid(row=9, column=0)
button = Button(control_frame, text="CLEAR", font=("Arial", 20), command=clear_canvas, bg="lightpink", fg="black", bd=0, activebackground="lightgrey")
button.grid(row=10, column=0, pady=50)

labels = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9]

cv.bind('<B1-Motion>', activate_paint)
cv.pack(expand=1, fill=BOTH, side=LEFT)

root.mainloop()

