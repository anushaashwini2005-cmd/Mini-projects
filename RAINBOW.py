# RAINBOW 
import turtle

# Setup the screen
screen = turtle.Screen()
screen.setup(width=800, height=500)
screen.bgcolor("skyblue")  # A nice sky background

# Create the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.width(20) # Thickness of each color band
t.hideturtle()

# Traditional Rainbow Colors (ROYGBIV)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

def draw_rainbow():
    # Starting radius for the outermost color (Red)
    radius = 200 
    
    # Starting position (adjusting based on radius to center it)
    t.penup()
    t.goto(radius, -50)
    t.setheading(90) # Point upwards
    t.pendown()

    for color in colors:
        t.color(color)
        
        # Draw a semi-circle (180 degrees)
        t.circle(radius, 180)
        
        # Move to the starting position for the next inner circle
        t.penup()
        radius -= 20 # Decrease radius for the next band
        t.right(180) # Flip direction to move back across
        t.goto(radius, -50)
        t.setheading(90)
        t.pendown()

draw_rainbow()

# Keep the window open
turtle.done()
