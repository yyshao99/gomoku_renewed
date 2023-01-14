
import pygame
import random
import numpy as np
import time
from strategies import judge_random, judge_cyy, judge_basic
from win import win






def main():
     
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
    pan = np.zeros((15,15))
    log = []
    # black:1
    # empty:0
    # white:-1



    color = 1
    playing = 1
    music = 0
    sound_active = 1
    localtime = time.asctime( time.localtime(time.time()) )
    start = 1
    while running:
        for event in pygame.event.get():
            if color == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[1] <= 700:
                        if playing:
                            x,y = judge_cyy(pan,1)
                            if start:
                                start = 0
                                x,y = 7,7
                            log.append((x,y))
                            if pan[x][y] == 0:
                                print("black"+"(%s,%s)"%(x,y))
                                pan[x][y] = 1
                                toput = (x*46.42,y*46.42)
                                screen.blit(im_black,toput)
                                
                                if sound_active == 1:
                                    pygame.mixer.Channel(2).play(sound)

                                color = -color
                                if win(pan):
                                    print("black wins")
                                    playing = 0
                                    color = 1
                                    screen.blit(im_finishblack,(300,0))
                                    pygame.display.flip()
                                    log.append(('win',1))
                                    f = open('./logs/logs:'+localtime+'.txt','w')
                                    f.write(str(log))
                                    f.close()
                                    print('output logs:'+'logs:'+localtime+'.txt')
                                    
                                pygame.display.flip()
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
                            
            elif color == -1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[1] <= 700:
                        if playing:
                            x,y = judge_cyy(pan,-1)
                            log.append((x,y))
                            if pan[x][y] == 0:
                                print("black"+"(%s,%s)"%(x,y))
                                pan[x][y] = -1
                                toput = (x*46.42,y*46.42)
                                screen.blit(im_white,toput)
                                
                                if sound_active == 1:
                                    pygame.mixer.Channel(2).play(sound)

                                color = -color
                                if win(pan):
                                    print("white wins")
                                    playing = 0
                                    color = 1
                                    screen.blit(im_finishwhite,(300,0))
                                    pygame.display.flip()
                                    log.append(('win',-1))
                                    f = open('./logs/logs:'+localtime+'.txt','w')
                                    f.write(str(log))
                                    f.close()
                                    print('output logs:'+'logs:'+localtime+'.txt')
                                    
                                pygame.display.flip()
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

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
     

if __name__=="__main__":
    main()
