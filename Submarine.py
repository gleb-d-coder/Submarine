
##Submarine Game
## Created by Gleb Denisov on 18-Apr-2020

# GUI of the Game
from tkinter import *
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title("Buble blaster")
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='DARKBLUE')
c.pack()
ship_id = c.create_polygon(5, 5, 5, 25, 30, 15,fill='red')
ship_id2 = c.create_oval(0, 0, 30, 30, outline='red')
SHIP_R = 10
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)
SHIP_SPD = 5
def move_ship(event):
    # Up
    if event.keysym == 'w':         
         c.move(ship_id, 0, -SHIP_SPD)
         c.move(ship_id2, 0, -SHIP_SPD)
    # Down
    elif event.keysym == 's':       
        c.move(ship_id, 0, SHIP_SPD)
        c.move(ship_id2, 0, SHIP_SPD)
    # Left
    elif event.keysym == 'a':       
        c.move(ship_id, -SHIP_SPD, 0)
        c.move(ship_id2, -SHIP_SPD, 0)
    # Right
    elif event.keysym == 'd':       
        c.move(ship_id, SHIP_SPD, 0)
        c.move(ship_id2, SHIP_SPD, 0)
c.bind_all('<Key>', move_ship)
from random import randint
bub_id = list()
bub_r = list()
bub_speed = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100
def create_buble():
    x = WIDHT + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval
    
