'''
By - Sahil Guglani
Task - A simple GUI to toggle 3 LED's using Raspberry Pi
'''
from gpiozero import LED
import RPi.GPIO
from tkinter import *
win.geometry("300 x 390")

green = LED(17)
red = LED(18)
blue = LED(27)

green.off()
red.off()
blue.off()
    
def Red():
    green.off()
    red.on()
    blue.off()
    print("Turn on red LED")

def Green():
    green.on()
    red.off()
    blue.off()
    print("Turn on green LED")

def Blue():
    green.off()
    red.off()
    blue.on()
    print("Turn on blue LED")
    
def close():
    green.off()
    red.off()
    blue.off()
    print("All LED's turned off")
    
def exit():
    RPi.GPIO.cleanup()
    win.destroy()
    print("Exit successfully!")
    
win = Tk()
win.title("LED Toggler")

Red = Radiobutton(win, text = "Turn Red",value = 1, command = Red, bg = "red", height = 4, width = 20)
Green = Radiobutton(win, text = "Turn Green",value = 0, command = Green, bg = "green", height = 4, width = 20)
Blue = Radiobutton(win, text = "Turn Blue",value = 2, command = Blue, bg = "blue", height = 4, width = 20)
Close = Radiobutton(win, text = "Turn all off",vorder = 3, command = close, bg = "white", height = 4, width = 20)
Exit = Button(win, text = "Exit",border = 3, command = exit, bg = "gray", height = 4, width = 18)

Red.grid(row = 0,column = 1)
Green.grid(row = 1,column = 1)
Blue.grid(row = 2,column = 1)
Close.grid(row = 3, column = 1)
Exit.grid(row = 4,column = 1)

win.mainloop()

