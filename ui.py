
import pygame
import random
import numpy as np
import time



class UI:
    def __init__(self,repo="resources",width=700,height=800):
        self.resource_repo = repo

    def gamestart(self):
        pygame.init()
        pygame.mixer.init(frequency = 8000, channels=1,buffer = 512)
        bgm = pygame.mixer.Sound("resources/music.wav")
        sound = pygame.mixer.Sound("resources/sound.wav")
        im_finishblack = pygame.image.load("resources/finishblack.png")
        im_finishwhite = pygame.image.load("resources/finishwhite.png")
        im_pan = pygame.image.load("resources/pan.png")
        im_white = pygame.image.load("resources/white.png")
        im_black= pygame.image.load("resources/black.png")
        im_again = pygame.image.load("resources/again.png")
        im_musicon = pygame.image.load("resources/music on.png")
        im_musicoff = pygame.image.load("resources/music off.png")
        logo = pygame.image.load("resources/gomoku.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("minimal program")
        
        screen = pygame.display.set_mode((700,800))
        screen.blit(im_pan,(0,0))
        screen.blit(im_again,(0,700))
        screen.blit(im_musicon,(350,700))
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
