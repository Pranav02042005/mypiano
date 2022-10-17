#importing modules
import pygame as py
from notes import *
import time as t
from pygame import mixer
# initializing the module
py.init()
# screen description
screen = py.display.set_mode((1375,700))
# screen setting
py.display.set_caption('mypiano')
icon=py.image.load('logo.png')
py.display.set_icon(icon)
#loading keys


c_temp = py.image.load('C.png')
cpressed = py.image.load('C_pressed.png')
d_temp = py.image.load('D.png')
dpressed = py.image.load('D_pressed.png')
e_temp = py.image.load('E.png')
epressed = py.image.load('E_pressed.png')
f_temp = py.image.load('F.png')
fpressed = py.image.load('F_pressed.png')
g_temp = py.image.load('G.png')
gpressed = py.image.load('G_pressed.png')
a_temp = py.image.load('A.png')
apressed = py.image.load('A_pressed.png')
b_temp = py.image.load('B.png')
bpressed = py.image.load('B_pressed.png')


size=(110,300)

a=py.transform.scale(a_temp ,size)
b = py.transform.scale(b_temp , size)
c = py.transform.scale(c_temp, size)
d = py.transform.scale(d_temp, size)
e = py.transform.scale(e_temp, size)
f = py.transform.scale(f_temp, size)
g = py.transform.scale(g_temp, size)
a_pressed=py.transform.scale(apressed,size)
b_pressed = py.transform.scale(bpressed, size)
c_pressed = py.transform.scale(cpressed, size)
d_pressed = py.transform.scale(dpressed, size)
e_pressed = py.transform.scale(epressed, size)
f_pressed = py.transform.scale(fpressed, size)
g_pressed = py.transform.scale(gpressed, size)



#sequencing images
dic={'C':c_pressed,'D':d_pressed,'E':e_pressed,'F':f_pressed,'G':g_pressed,'A':a_pressed,'B':b_pressed}
image_list=[c,d,e,f,g,a,b]
pos_lis=[(0,400),(400,800)]
pos_dic={'C4':(0,400)}
image_pressed=dic.values()


def rate(image,pos):
    screen.blit(image,pos)
    t.sleep(0.5)
def plot(image,pos):
    screen.blit(image,pos)

start=0
running =1
while running:
    # plotting images
    screen.blit(c, (0, 400))
    screen.blit(d, (100, 400))
    screen.blit(e, (200, 400))
    screen.blit(f, (300, 400))
    screen.blit(g, (400, 400))
    screen.blit(a, (500, 400))
    screen.blit(b, (600, 400))
    screen.blit(c, (700, 400))
    screen.blit(d, (800, 400))
    screen.blit(e, (900, 400))
    screen.blit(f, (1000, 400))
    screen.blit(g, (1100, 400))
    screen.blit(a, (1200, 400))
    screen.blit(b, (1300, 400))

    for event in py.event.get():
        if event.type == py.QUIT:
            running=0
        if event.type ==py.KEYUP:
            input_event=chr(event.key).upper()
            if input_event in white_input:
                y = search(input_event, start)
                if y == 'C4':
                    screen.blit(c_pressed, (0, 400))
                    t.sleep(0.5)
                elif y == 'D4':
                    screen.blit(d_pressed, (100, 400))
                    t.sleep(0.5)
                elif y == 'E4':
                    screen.blit(e_pressed, (200, 400))
                    t.sleep(0.5)
                elif y == 'F4':
                    screen.blit(f_pressed, (300, 400))
                    t.sleep(0.5)
                elif y == 'G4':
                    screen.blit(g_pressed, (400, 400))
                    t.sleep(0.5)
                elif y == 'A4':
                    screen.blit(a_pressed, (500, 400))
                    t.sleep(0.5)
                elif y == 'B4':
                    screen.blit(b_pressed, (600, 400))
                    t.sleep(0.5)
                elif y == 'C5':
                    screen.blit(c_pressed, (700, 400))
                    t.sleep(0.5)
                elif y == 'D5':
                    screen.blit(d_pressed, (800, 400))
                    t.sleep(0.5)
                elif y == 'E5':
                    screen.blit(e_pressed, (900, 400))
                    t.sleep(0.5)
                elif y == 'F5':
                    screen.blit(f_pressed, (1000, 400))
                    t.sleep(0.5)
                elif y == 'G5':
                    screen.blit(g_pressed, (1100, 400))
                    t.sleep(0.5)
                elif y == 'A5':
                    screen.blit(a_pressed, (1200, 400))
                    t.sleep(0.5)
                elif y == 'B5':
                    screen.blit(b_pressed, (1300, 400))
                    t.sleep(0.5)

                print(y)


        if event.type==py.KEYDOWN:
            input_event = chr(event.key).upper()
            if input_event in white_input:
                y = search(input_event, start)
                if y == 'C4':
                    screen.blit(c, (0, 400))

                elif y == 'D4':
                    screen.blit(d, (100, 400))
                elif y == 'E4':
                    screen.blit(e, (200, 400))
                elif y == 'F4':
                    screen.blit(f, (300, 400))
                elif y == 'G4':
                    screen.blit(g, (400, 400))
                elif y == 'A4':
                    screen.blit(a, (500, 400))
                elif y == 'B4':
                    screen.blit(b, (600, 400))
                elif y == 'C5':
                    screen.blit(c, (700, 400))
                elif y == 'D5':
                    screen.blit(d, (800, 400))
                elif y == 'E5':
                    screen.blit(e, (900, 400))
                elif y == 'F5':
                    screen.blit(f, (1000, 400))
                elif y == 'G5':
                    screen.blit(g, (1100, 400))
                elif y == 'A5':
                    screen.blit(a, (1200, 400))
                elif y == 'B5':
                    screen.blit(b, (1300, 400))








    py.display.update()
