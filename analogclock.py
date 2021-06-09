import turtle
import time

screen = turtle.Screen() #turtle screen
screen.bgcolor("white") #background of the screen
screen.setup(width=600, height=600) #geometry of the GUI
screen.title("clock") #title of the GUI
screen.tracer(0) #tracer for the GUI

rajdeep = turtle.Turtle() #the turtle
rajdeep.hideturtle() #make the turtle invisible
rajdeep.speed(0) #setting the speed to 0
rajdeep.pensize(3) #setting the pensize to 3


def ghadi_bana(ghantaa, minutee, secondd, rajdeep): #function with 4 parameters

    rajdeep.up() #not ready to draw
    rajdeep.goto(0, 210) #positioning the turtle
    rajdeep.setheading(180) #setting the heading to 180
    rajdeep.color("red") #setting the color of the pen to red
    rajdeep.pendown() #starting to draw
    rajdeep.circle(210) #a circle with the radius 210

    rajdeep.up() #not ready to draw
    rajdeep.goto(0, 0) #positioning the turtle
    rajdeep.setheading(90) #same as seth(90) in newer version

    for z in range(12): #loop 
        rajdeep.fd(190) #moving forward at 190 units
        rajdeep.pendown() #starting to draw
        rajdeep.fd(20) #forward at 20
        rajdeep.penup() #not ready to draw
        rajdeep.goto(0, 0) #positioning the turtle
        rajdeep.rt(30) #right at an angle of 30 degrees

    hands = [("black", 80, 12), ("black", 150, 60), ("black", 110, 60)] #the color and the hands set
    time_set = (ghantaa, minutee, secondd) #setting the time

    for hand in hands: #loop
        time_part = time_set[hands.index(hand)] #time part in the hand index in hands of time_Set
        angle = (time_part/hand[2])*360 #setting the angle for the clock
        rajdeep.penup() #not ready to draw
        rajdeep.goto(0, 0) #positioning the turtle
        rajdeep.color(hand[0]) #setting the color of the hand
        rajdeep.setheading(90) #same as seth(90)
        rajdeep.rt(angle) #right at an angle of "right"
        rajdeep.pendown() #ready to draw
        rajdeep.fd(hand[1]) #forward at a unit of 1st index of the hand var


while True:
    ghantaa = int(time.strftime("%I")) #setting the hour from the time module
    minutee = int(time.strftime("%M")) #setting the minute from the time module
    secondd = int(time.strftime("%S")) #setting the second as above

    ghadi_bana(ghantaa, minutee, secondd, rajdeep) #calling the ghanta_bana() function with the given parameters
    screen.update() #updating the scren
    time.sleep(1) #making the code sleep for a second with the time module
    rajdeep.clear() #clearing the pen
