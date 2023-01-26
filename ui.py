
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
        self.music_on = 0
        self.win_cond = 0
        self.sound_active = 0
        self.width = width
        self.height = height
        self.spacing = 46.42
        self.screen = None
        self.playing = False
        self.gl = gl.GameLogic()
        self.log = []

    def gamestart(self):
        pygame.init()
        pygame.mixer.init(frequency = 8000, channels=1,buffer = 512)
        self.bgm = pygame.mixer.Sound("resources/music.wav")
        self.play_sound = pygame.mixer.Sound("resources/sound.wav")
        self.im_finishblack = pygame.image.load("resources/finishblack.png")
        self.im_finishwhite = pygame.image.load("resources/finishwhite.png")
        self.im_pan = pygame.image.load("resources/pan.png")
        self.im_white = pygame.image.load("resources/white.png")
        self.im_black= pygame.image.load("resources/black.png")
        self.im_again = pygame.image.load("resources/again.png")
        self.im_musicon = pygame.image.load("resources/music on.png")
        self.im_musicoff = pygame.image.load("resources/music off.png")
        logo = pygame.image.load("resources/gomoku.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("minimal program")
        
        screen = pygame.display.set_mode((self.width,self.height))
        self.screen = screen
        screen.blit(self.im_pan,(0,0))
        screen.blit(self.im_again,(0,self.width))
        screen.blit(self.im_musicon,(self.width/2,self.width))
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
            if self.playing:
                x_axis = int((screen_pos[0])//46.42)
                y_axis = int((screen_pos[1])//46.42)
                pos = (x_axis,y_axis)
                color = self.gl.play_chess(pos)
                if color:
                    self.play_chess(color,pos)
        if screen_pos[1] > self.width:
            if screen_pos[0] <= 350:
                print("play again")
                self.gl.replay()
                pan = np.zeros((15,15))
                color = 1
                self.playing = 1
                self.screen.blit(self.im_pan,(0,0))
                pygame.display.flip()
                localtime = time.asctime( time.localtime(time.time()) )
                log = []
            else:
                if self.music_on == 0:
                    print("music on")
                    pygame.mixer.pre_init(frequency=4000)
                    pygame.mixer.Channel(1).play(self.bgm)
                    self.screen.blit(self.im_musicoff,(350,700))
                    pygame.display.flip()
                    self.music_on = 1
                else:
                    self.music_on = 0
                    print("music off")
                    pygame.mixer.Channel(1).stop()
                    self.screen.blit(self.im_musicon,(350,700))
                    pygame.display.flip()

    def play_chess(self,color,pos):
        screen_pos = (pos[0] * self.spacing, pos[1] * self.spacing)
        if color == 1:
            self.screen.blit(self.im_black,screen_pos)
        if color == -1:
            self.screen.blit(self.im_white,screen_pos)
        pygame.display.flip()
        if self.sound_active == 1:
            pygame.mixer.Channel(2).play(self.sound)
        self.win_cond = self.gl.win()
        if self.win_cond == 1:
            self.win(1)
        if self.win_cond == -1:
            self.win(-1)

    def win(self,color):
        if color == 1: 
            print("black wins")
            self.playing = False
            self.screen.blit(self.im_finishblack,(300,0))
        if color == -1: 
            print("white wins")
            self.playing = False
            self.screen.blit(self.im_finishwhite,(300,0))
        pygame.display.flip()
        