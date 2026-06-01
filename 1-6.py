import math
import time
from turtle import *

s = Screen()
s.setup(width=600, height=800) 
s.bgcolor("black")

t = Turtle()
t.speed(0)
t.color("red")
t.hideturtle() 

def hearta(k): return 15 * math.sin(k)**3
def heartb(k): return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

# trai tim
for i in range(100):
    t.goto(hearta(i) * 15, heartb(i) * 15) 
    t.goto(0, 0)
writer = Turtle()
writer.hideturtle()
writer.color("#FF96C8")
writer.penup()
name = "Lê Ngọc Nguyên Thy"
writer.goto(0, -400) 

current_text = ""
for char in name:
    current_text += char
    writer.clear()
    writer.write(current_text, align="center", font=("Arial", 18, "bold"))
    time.sleep(0.2) 
time.sleep(1.5)

# chuyen canh

s.clearscreen()
s.bgcolor("black") 

# phan 7 mau
rainbow = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"]

lines = [
    "Chúc công chúa",
    "Ngày 1/6",
    "Vui vẻ"
]

pens = []
y_positions = [150, 0, -150] 

for y in y_positions:
    p = Turtle()
    p.hideturtle()
    p.penup()
    p.goto(0, y)
    pens.append(p)

color_idx = 0 

for i in range(3):
    current_text = ""
    for char in lines[i]:
        current_text += char
        pens[i].clear()
        
        pens[i].color(rainbow[color_idx % 7])
       
        pens[i].write(current_text, align="center", font=("Arial", 25, "bold"))
        
        color_idx += 1
        time.sleep(0.15) 
        
time.sleep(3)
done()
