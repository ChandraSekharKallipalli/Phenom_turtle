import turtle as jarvis
import time

jarvis.shape("turtle")
# Function to draw the first section
jarvis.width(3)
def draw_first_section():
    jarvis.color("#42cbd5")
    jarvis.fillcolor("white")

    # Move the turtle to the center
    jarvis.penup()
    jarvis.goto(-90, -100)
    jarvis.pendown()

    # Draw the first section
    jarvis.begin_fill()
    jarvis.left(90)
    jarvis.forward(200)
    jarvis.circle(-100, 290)
    jarvis.left(110)
    jarvis.forward(106.03)
    jarvis.circle(-32.9, 180)
    jarvis.end_fill()

# Function to draw the second section
def draw_second_section():
    jarvis.fillcolor("#42cbd5")
    jarvis.begin_fill()
    jarvis.circle(50, 360)
    jarvis.end_fill()

# Function to draw the third section
def draw_third_section():
    jarvis.fillcolor("white")
    jarvis.pencolor("#42cbd5")
    jarvis.begin_fill()
    jarvis.seth(230)
    jarvis.circle(-130, 105)
    jarvis.circle(22, 180)
    jarvis.circle(174, 105)
    jarvis.circle(22, 180)
    jarvis.end_fill()

    time.sleep(0.5)
    jarvis.bgcolor("#42cbd5")
    time.sleep(1)

# Function to animate text
def animate_text(text, font=("Arial", 30, "normal")):
    jarvis.speed(3)
    jarvis.pencolor("white")
    jarvis.write(text, font=font, align="center")

# Main drawing functions
draw_first_section()

jarvis.color("#42cbd5")
jarvis.penup()
jarvis.right(90)
jarvis.forward(150)
jarvis.left(90)
jarvis.forward(200)
jarvis.pendown()

draw_second_section()

jarvis.penup()
jarvis.left(90)
jarvis.forward(0)
jarvis.left(90)
jarvis.forward(230)
jarvis.pendown()

draw_third_section()

jarvis.up()
jarvis.seth(90)
jarvis.forward(50)
jarvis.right(90)
jarvis.forward(-50)

# Text animation
text_to_display = "Phenom PhamiLy"
for char in text_to_display:
    animate_text(char)
    jarvis.forward(24)

# Align

jarvis.forward(-150)
jarvis.seth(270)
jarvis.forward(10)
time.sleep(4)
jarvis.forward(160)

# Function to display developer information
def display_developer_info():
    developer = "Developed by #Chandra Sekhar"
    jarvis.write(developer, align="center")

# Display developer information

display_developer_info()

jarvis.forward(15)

jarvis.done()
