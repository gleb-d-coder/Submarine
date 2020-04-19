#.______    __    __  .______   .______    __       _______      _______.    __    __   __    __  .__   __. .___________. _______ .______      
#|   _  \  |  |  |  | |   _  \  |   _  \  |  |     |   ____|    /       |   |  |  |  | |  |  |  | |  \ |  | |           ||   ____||   _  \     
#|  |_)  | |  |  |  | |  |_)  | |  |_)  | |  |     |  |__      |   (----`   |  |__|  | |  |  |  | |   \|  | `---|  |----`|  |__   |  |_)  |    
#|   _  <  |  |  |  | |   _  <  |   _  <  |  |     |   __|      \   \       |   __   | |  |  |  | |  . `  |     |  |     |   __|  |      /     
#|  |_)  | |  `--'  | |  |_)  | |  |_)  | |  `----.|  |____ .----)   |      |  |  |  | |  `--'  | |  |\   |     |  |     |  |____ |  |\  \----.
#|______/   \______/  |______/  |______/  |_______||_______||_______/       |__|  |__|  \______/  |__| \__|     |__|     |_______|| _| `._____|
## Created by Gleb Denisov on 18-Apr-2020

### GUI of the Game

# Import section
from tkinter import *
from random import randint
from math import sqrt
from time import sleep, time



### 001 The game main window
HEIGHT = 500
WIDTH = 800
window = Tk()
window.title("Buble blaster")
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='DARKBLUE')
c.pack()

### 002 Draw submarine
ship_id = c.create_polygon(5, 5, 5, 25, 30, 15,fill='red')
ship_id2 = c.create_oval(0, 0, 30, 30, outline='red')
SHIP_R = 10
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)

### 003 Submarine manage
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


### It's the bubble time!!!

### 004 Bubbles moving
bub_id = list()
bub_r = list()
bub_speed = list()
MIN_BUB_R = 10
MAX_BUB_R = 30
MAX_BUB_SPD = 10
GAP = 100

def create_buble():
    x = WIDTH + GAP
    y = randint(0, HEIGHT)
    r = randint(MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))

### 005 Move bubbles
def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[1], 0)
        

### 007
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2

### 008
def del_bubbles(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]

### 009
def clean_up_bubs():
    for i in range(len(bub_id)-1, -1, -1):
        x, y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubble(i)

### 011
def distance(id1, id2):
    x1, y1 = get_cords(id1)
    x2, y2 = get_cords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

### 012
def collision():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1,):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points
###14
c.create_text(50, 30, text='TIME', fill='white' )
c.create_text(150, 30, text='SCORE', fill='white')
time_text = c.create-text(50, 50, fill='white' )
score_text = c.create_text(150, 50, fill='white' )
def show_score(score):
    c.itemcomfing(score_text, text=str(score))
def show_time(time_left):
    c.itomcomfig(time_text, text, text=str(score))


### 006/010/013 MAIN GAME LOOP
BUB_CHANCE = 10
score = 0
while True:
    if randint(1, BUB_CHANCE) == 1:
        create_buble()
    clean_up_bubs()
    score += collision()
    print(score)
    window.update()
    sleep(0.01)

### 015   
BUB_CHANCE = 10
TIME_LEMIT = 40
BONUS_SCORE = 1000
score = 0
bonus = 0
end = time() + TIME_LEMIT

###16
#MAIN GAME LOOP
while time() < end:
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    clen_up_bubs()
    if(int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LEMIT
    show_score(score)
    show_time(int(end - time()))
    window.update()
    sleep(0.01)
    ###17
   c.create_text(MID_X, MID_Y, \
        text='GAME OVER', fill='white', font=('Helvetica',30))
   c.create_text(MID_X, MID_Y + 30, \
        text+'Score: '+ str(score), fill='white')
   c.create_text(MID_X, MID_Y + 45, \
                 text+'Bonus time: '+ str(bonus*TIME_LIMIT), fill+'white') 
