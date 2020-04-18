
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
    if event.keysym == 'w':         # Up
         c.move(ship_id, 0, -SHIP_SPD)
         c.move(ship_id2, 0, -SHIP_SPD)
    elif event.keysym == 's':       # Down
        c.move(ship_id, 0, SHIP_SPD)
        c.move(ship_id2, 0, SHIP_SPD)
    elif event.keysym == 'a':       # Left
        c.move(ship_id, -SHIP_SPD, 0)
        c.move(ship_id2, -SHIP_SPD, 0)
    elif event.keysym == 'd':       # Right
        c.move(ship_id, SHIP_SPD, 0)
        c.move(ship_id2, SHIP_SPD, 0)
c.bind_all('<Key>', move_ship)

