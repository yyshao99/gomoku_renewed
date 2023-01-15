
import pygame
import random
import numpy as np
import time
from collections import deque
import game_logic as gl


class UI:
    def __init__(self,repo="resources",width=700,height=800):
        self.resource_repo = repo
        self.event_queue = deque()
        self.running = False
        self.width = width
        self.height = height
        self.spacing = 46.42
        self.screen = None
        self.playing = False
        self.gl = gl.GameLogic()

    def gamestart(self):
        pygame.init()
        pygame.mixer.init(frequency = 8000, channels=1,buffer = 512)
        bgm = pygame.mixer.Sound("resources/music.wav")
        sound = pygame.mixer.Sound("resources/sound.wav")
        im_finishblack = pygame.image.load("resources/finishblack.png")
        im_finishwhite = pygame.image.load("resources/finishwhite.png")
        im_pan = pygame.image.load("resources/pan.png")
        self.im_white = pygame.image.load("resources/white.png")
        self.im_black= pygame.image.load("resources/black.png")
        im_again = pygame.image.load("resources/again.png")
        im_musicon = pygame.image.load("resources/music on.png")
        im_musicoff = pygame.image.load("resources/music off.png")
        logo = pygame.image.load("resources/gomoku.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("minimal program")
        
        screen = pygame.display.set_mode((self.width,self.height))
        self.screen = screen
        screen.blit(im_pan,(0,0))
        screen.blit(im_again,(0,self.width))
        screen.blit(im_musicon,(self.width/2,self.width))
        pygame.display.flip()

        self.running = True
        self.playing = True
        self.event_handler()

    def event_handler(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_click()

    def mouse_click(self):
        screen_pos = pygame.mouse.get_pos()
        if screen_pos[1] <= self.width:
            if playing:
                x_axis = int((screen_pos[0])//46.42)
                y_axis = int((screen_pos[1])//46.42)
                pos = (x_axis,y_axis)
                gl.play_chess(pos)
                
        if pos[1] > 700:
            if pos[0] <= 350:
                print("play again")
                pan = np.zeros((15,15))
                color = 1
                playing = 1
                screen.blit(im_pan,(0,0))
                pygame.display.flip()
                localtime = time.asctime( time.localtime(time.time()) )
                log = []
            else:
                if music == 0:
                    print("music on")
                    pygame.mixer.pre_init(frequency=4000)
                    pygame.mixer.Channel(1).play(bgm)
                    screen.blit(im_musicoff,(350,700))
                    pygame.display.flip()
                    music = 1
                else:
                    music = 0
                    print("music off")
                    pygame.mixer.Channel(1).stop()
                    screen.blit(im_musicon,(350,700))
                    pygame.display.flip()

    def play_chess(self,color,pos):
        screen_pos = (pos[0] * self.spacing, pos[1] * self.spacing)
        if color == 1:
            self.screen.blit(self.im_black,screen_pos)
        if color == -1:
            self.screen.blit(self.im_white,screen_pos)
        pygame.display.flip()
