import pygame 
from pygame import *
from pygame.locals import *
import random
import sys
import pickle
import time
import os
from Tkinter import *
from tkFileDialog import*

#colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
blue2 = (44, 157, 201)
blue3 = (8, 140, 196)
blue4 = (40, 181, 166)
aqua = (0, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
green2 = (0, 153, 0)
green3 = (0,100,0)
gray = (158, 156, 166)
gray2 = (69, 67, 68)

#var
rendermode = 1
play = 0
song_path = ''
song_path_old = ''

#images
upload_img = pygame.image.load("upload.png")
close_img = pygame.image.load("close.png")
pause_img = pygame.image.load("pause.png")
play_img = pygame.image.load("play.png")

from win32api import GetSystemMetrics
print "Width =", GetSystemMetrics(0)
print "Height =", GetSystemMetrics(1)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ( GetSystemMetrics(0) / 4, 1)
pygame.init()
screen_x = 700
screen_y = 100
screen = pygame.display.set_mode([screen_x,screen_y], NOFRAME)
middlex = screen_x/2
middley = screen_y/2
print middlex
print middley

#fonts
menu_font = pygame.font.SysFont('Calibri', 40)
hud_font = pygame.font.SysFont('Calibri', 40)
hud_font2 = pygame.font.SysFont('Calibri', 20)
big_font = pygame.font.SysFont('Calibri', 80)

def erroR(type):
    if type == 1:

        app = Tk()
        app.title('error')
        app.geometry('500x250')

        labelText = StringVar()
        labelText.set('''Error:
                        
         file system seems to have been deleted
        -program may be unstable
        -reinstall may fix''')

        label1 = Label(app, textvariable = labelText, height = 10)
        label1.pack()

        app.mainloop()

#pickle_out = open('size.csf', 'w')
#pickle.dump('0', pickle_out)
#pickle_out.close()

try:
    pickle_in = open('size.csf', 'r')
    size = pickle.load(pickle_in)
except:
    erroR(1)

if not size == '0':
    erroR(1)

#window settings
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    mx, my = pygame.mouse.get_pos()
    if rendermode == 1:
        screen.fill(aqua)

        if play == 1:
            playing_text = menu_font.render('playing ', True, white)
            screen.blit(playing_text,(90, 5))
            playing2_text = menu_font.render(song_path_old, True, white)
            screen.blit(playing2_text,(90, 50))

        #load
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 5 and my < 95:
                    if mx > 5 and mx < 85:
                        f = askopenfilename()
                        song_path = f
                        print song_path
                        pygame.time.delay(100)

        #play/pause
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 5 and my < 95:
                    if mx > 500 and mx < 580:
                        if play == 0:
                            play = 1
                            pygame.mixer.music.unpause()
                            pygame.time.delay(100)                           
                        elif play == 1:
                            play = 0
                            pygame.mixer.music.pause()
                            pygame.time.delay(100)
                            
  
        #close
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if my > 5 and my < 95:
                    if mx > 600 and mx < 680:
                        pygame.quit()
                        sys.exit()   

        if not song_path == '':
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play(-1, 0.0)
            play = 1
            song_path_old = song_path
            song_path = ''

        pygame.draw.rect(screen, aqua, [480, 0, 700, 100]) 

        screen.blit(upload_img, (5, 10))
        screen.blit(close_img, (600, 10))
        if play == 1:
            screen.blit(pause_img, (500, 10))
        else:
            screen.blit(play_img, (500, 10))
    pygame.display.update()