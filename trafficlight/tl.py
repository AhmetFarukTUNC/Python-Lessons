import time

lights = ["red","yellow","green"]


for i in lights:
    if i == "red":
        print("stop!")
    time.sleep(1)
    if i == "yellow":
        print("ready!")
    time.sleep(1)
    if i == "green":
        print("go!")
