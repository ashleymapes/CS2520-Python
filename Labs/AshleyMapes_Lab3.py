'''
Ashley Mapes
Lab 3

This is my original design and implementation inspired by the show Phineas and Ferb


INSPIRATION
I recently got a dog from the pound and he was named Ferb. His brother was named Phineas,
however, someone had already adopted him. Their names reminded me of my childhood watching
Phineas and Ferb with my sister when we were kids. I felt an instant connection with Ferb
and decided to adopt him and have him live with me at my apartment. We renamed him Finny
to pay respect to his past (phineas + ferb) and he's been living a very happy puppy life!!

This program will draw an abstract, simple drawing of the very geometric shaped cast of
Phineas and Ferb using python turtle

'''

import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

finny = turtle.Turtle()
finny.speed(10)

# Function to draw a filled rectangle
def draw_rectangle(width, height, color):
    finny.pencolor(color)
    finny.fillcolor(color)
    finny.begin_fill()
    for _ in range(2):
        finny.forward(width)
        finny.left(90)
        finny.forward(height)
        finny.left(90)
    finny.end_fill()
    finny.penup()

def draw_triangle(side, angle, color):
    finny.pencolor(color)
    finny.pendown()
    finny.fillcolor(color)
    finny.begin_fill()
    
    finny.left(angle)
    for _ in range(3):
        finny.forward(side)
        finny.left(120)
    finny.end_fill()
    finny.penup

# Function to draw perry
def draw_perry():
    
    #main body
    finny.goto(-100,-100)
    draw_rectangle(150,60,"#24a7a1")
    
    # front legs
    finny.goto(-90,-120)
    draw_rectangle(10,20,"#24a7a1")
    
    finny.goto(-90,-130)
    draw_rectangle(20,10,"#ff9810")
    
    #back legs
    finny.goto(10,-120)
    draw_rectangle(10,20,"#24a7a1")
    
    finny.goto(10,-130)
    draw_rectangle(20,10,"#24a7a1")
    
    # beak
    finny.goto(30,-100)
    draw_rectangle(20,20,"#ff9810")
    
    finny.goto(50,-95)
    draw_rectangle(40,10,"#ff9810")
    
    # tail
    finny.goto(-160,-100)
    draw_rectangle(60,30,"#fd975c")
    
    #fedora
    finny.goto(0,-40)
    draw_rectangle(60,10,"#562b35")
    
    finny.goto(10,-30)
    draw_rectangle(40,10,"#000000")
    
    finny.goto(10,-20)
    draw_rectangle(40,15,"#562b35")
    
    
    
# Function to draw phineas
def draw_phineas():
    finny.goto(200,0)
    draw_triangle(150,80,"#f8c088")
    # shirt
    
    finny.left(10)
    x = 210
    y = 0
    for _ in range (3):
        finny.goto(x,y)
        draw_rectangle(10,50,"orange")
        y -= 10
        finny.goto(x,y)
        draw_rectangle(10,50,"white")
        y -= 10
    
    #pants
    finny.goto(x, y - 70)
    draw_rectangle(80,50, "blue")
    
    #hair twaft
    finny.left(45)
    finny.goto(240,150)
    draw_rectangle(15,20, "red")
    

# Function to draw Ferb
def draw_ferb():
    # head
    finny.penup()
    finny.goto(-300, 0)
    draw_rectangle(60,150,"#f8c088")
    
    # nose
    finny.goto(-240,50)
    draw_rectangle(30,60,"#f8c088")
        
    # hair
    finny.penup()
    finny.goto(-300, 150)
    finny.pendown()
    draw_rectangle(60, 30, "green")

    # shirt
    finny.penup()
    finny.goto(-300, -40)
    finny.pendown()
    draw_rectangle(60, 40, "white")

    # pants
    finny.penup()
    finny.goto(-300, -130)
    finny.pendown()
    draw_rectangle(60, 90, "purple")

def main():
    # draw the cast
    draw_ferb()
    draw_perry()
    draw_phineas()
    
    
    # hide the turtle
    finny.hideturtle()

    # finish
    screen.mainloop()

main()