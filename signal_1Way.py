import turtle
from time import sleep
import cv2
from vehicle_detector import VehicleDetector
import random
import numpy  as np

vd = VehicleDetector()

# Camera Function

# def camera():
#     cam = cv2.VideoCapture(0).lmu7
#     img_counter = 0

#     while True:
#         ret, image = cam.read()
#         if (ret == False):
#             print("failed to grab frame")
#             break

#         cv2.imshow('Imagetest',image)
#         k = cv2.waitKey(1)
#         print(k)
#         if (k%256 == 32):
#             img_name = "frame.png".format(img_counter)
#             cv2.imwrite(img_name,image)
#             print("screenshot")
#             break

#     cam.release()
#     cv2.destroyAllWindows()
lane1 = "./lane1.jpg"
lane2 = "./lane2.jpg"
lane3 = "./lane3.jpg"
lane4 = "./lane4.jpg"

def process_lane(lane_number, img_path, counter):
    img = cv2.imread(img_path)
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)
    counter += vehicle_count

    for box in vehicle_boxes:
        left, top, right, bottom = np.array(box, dtype=int).squeeze()
        width = right - left
        height = bottom - top
        center = (left + int((right-left)/2), top + int((bottom-top)/2))
        cv2.rectangle(img, (left, top),(right, bottom), (255, 0, 0), 2)
        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (0, 0, 0), 3)

    cv2.imshow("Lane {}".format(lane_number), img)
    print("Vehicle Count: ", vehicle_count)
    print("Total current count", counter)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    return counter


# Lane Functions
def Lane1(img_path):
    global cnt1
    cnt1=process_lane(1, lane1, cnt1)
    
def Lane2(img_path):
    global cnt2
    cnt2=process_lane(2, lane2, cnt2)

def Lane3(img_path):
    global cnt3
    cnt3=process_lane(3, lane3, cnt3)
    
def Lane4(img_path):
    global cnt4
    cnt4=process_lane(4, lane4, cnt4)

# Set up the screen
wn = turtle.Screen()
wn.setup(width=750, height=750)
wn.title("Traffic Lights")
wn.bgcolor("black")
# turtle.speed(speed=20)
turtle.speed(0)
pen = turtle.Turtle()

# Writing Texts Lane1
pen.penup()
pen.goto(0, 170)
pen.color("white")
pen.write('Lane1', align="center", font=("Serif", 18))

# Draw box around the stoplight Lane1
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 320)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

# Red light
red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0, 300)

# Yellow light
yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0, 260)

# Green light
green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0, 220)

# Writing Texts Lane2
pen.penup()
pen.goto(-220, -10)
pen.color("white")
pen.write('Lane2', align="center", font=("Serif", 18))

# Draw box around the stoplight Lane2
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-320, -60)
pen.pendown()
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)

# Red light
red_light1 = turtle.Turtle()
red_light1.shape("circle")
red_light1.color("grey")
red_light1.penup()
red_light1.goto(-290, 40)

# Yellow light
yellow_light1 = turtle.Turtle()
yellow_light1.shape("circle")
yellow_light1.color("grey")
yellow_light1.penup()
yellow_light1.goto(-290, 0)

# Green light
green_light1 = turtle.Turtle()
green_light1.shape("circle")
green_light1.color("grey")
green_light1.penup()
green_light1.goto(-290, -40)

# Writing Texts Lane3
pen.penup()
pen.goto(220, -10)
pen.color("white")
pen.write('Lane3', align="center", font=("Serif", 18))

# Draw box around the stoplight Lane3
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(320, -60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

# Red light
red_light2 = turtle.Turtle()
red_light2.shape("circle")
red_light2.color("grey")
red_light2.penup()
red_light2.goto(290, 40)

# Yellow light
yellow_light2 = turtle.Turtle()
yellow_light2.shape("circle")
yellow_light2.color("grey")
yellow_light2.penup()
yellow_light2.goto(290, 0)

# Green light
green_light2 = turtle.Turtle()
green_light2.shape("circle")
green_light2.color("grey")
green_light2.penup()
green_light2.goto(290, -40)

# Writing Texts Lane4
pen.penup()
pen.goto(0, -180)
pen.color("white")
pen.write('Lane4', align="center", font=("Serif", 18))

# Draw box around the stoplight Lane4
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(30, -310)
pen.pendown()
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

# Red light
red_light3 = turtle.Turtle()
red_light3.shape("circle")
red_light3.color("grey")
red_light3.penup()
red_light3.goto(0, -210)

# Yellow light
yellow_light3 = turtle.Turtle()
yellow_light3.shape("circle")
yellow_light3.color("grey")
yellow_light3.penup()
yellow_light3.goto(0, -250)

# Green light
green_light3 = turtle.Turtle()
green_light3.shape("circle")
green_light3.color("grey")
green_light3.penup()
green_light3.goto(0, -290)


while True:

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0


# Lane1
    Lane1(lane1)
    green_light.color("green")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("grey")
    red_light1.color("red")
    red_light2.color("red")
    red_light3.color("red")

    yellow_light.color("grey")
    yellow_light1.color("grey")
    yellow_light2.color("grey")
    yellow_light3.color("grey")
    sleep(cnt1)

# Delay 1
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("grey")
    red_light1.color("grey")
    red_light2.color("red")
    red_light3.color("red")

    yellow_light.color("yellow")
    yellow_light1.color("yellow")
    yellow_light2.color("grey")
    yellow_light3.color("grey")
    sleep(1)

# Lane2
    Lane2(lane2)
    green_light.color("grey")
    green_light1.color("green")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("red")
    red_light1.color("grey")
    red_light2.color("red")
    red_light3.color("red")

    yellow_light.color("grey")
    yellow_light1.color("grey")
    yellow_light2.color("grey")
    yellow_light3.color("grey")
    sleep(cnt2)

# Delay 2
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("red")
    red_light1.color("grey")
    red_light2.color("grey")
    red_light3.color("red")

    yellow_light.color("grey")
    yellow_light1.color("yellow")
    yellow_light2.color("yellow")
    yellow_light3.color("grey")
    sleep(1)

# Lane3
    Lane3(lane3)
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("green")
    green_light3.color("grey")

    red_light.color("red")
    red_light1.color("red")
    red_light2.color("grey")
    red_light3.color("red")

    yellow_light.color("grey")
    yellow_light1.color("grey")
    yellow_light2.color("grey")
    yellow_light3.color("grey")
    sleep(cnt3)

# Delay 3
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("red")
    red_light1.color("red")
    red_light2.color("grey")
    red_light3.color("grey")

    yellow_light.color("grey")
    yellow_light1.color("grey")
    yellow_light2.color("yellow")
    yellow_light3.color("yellow")
    sleep(1)

# Lane4
    Lane4(lane4)
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("green")

    red_light.color("red")
    red_light1.color("red")
    red_light2.color("red")
    red_light3.color("grey")

    yellow_light.color("grey")
    yellow_light1.color("grey")
    yellow_light2.color("grey")
    yellow_light3.color("grey")
    sleep(cnt4)

# Delay 4
    green_light.color("grey")
    green_light1.color("grey")
    green_light2.color("grey")
    green_light3.color("grey")

    red_light.color("grey")
    red_light1.color("red")
    red_light2.color("red")
    red_light3.color("grey")

    yellow_light.color("yellow")
    yellow_light1.color("grey")
    yellow_light2.color("grey")
    yellow_light3.color("yellow")
    sleep(1)

wn.mainloop()
