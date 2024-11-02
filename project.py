import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
t.speed(0)
n=70
h=0
for i in range (360):
    c=colorsys.hsv_to_rgb(h,1,1)

    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range (2):
        t.left(2)
        t.circle(100)
    h+=1/n
    if h >= 1:  # Reset hue to loop through colors
        h = 0
