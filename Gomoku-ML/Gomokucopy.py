
import pygame
import original as ori

def main():
    pygame.init()
    pygame.mixer.init(frequency = 8000, channels=1,buffer = 512)
    im_pan = pygame.image.load("resources/pan.png")
    im_white = pygame.image.load("resources/white.png")
    im_black= pygame.image.load("resources/black.png")
    im_again = pygame.image.load("resources/again.png")
    im_musicon = pygame.image.load("resources/music on.png")
    logo = pygame.image.load("resources/gomoku.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    
    screen = pygame.display.set_mode((700,800))
    screen.blit(im_pan,(0,0))
    screen.blit(im_again,(0,700))
    screen.blit(im_musicon,(350,700))
    pygame.display.flip()
    running = True
    pan = []
    for i in range(15):
        pan.append([])
    for i in range(15):
        for p in range(15):
            pan[p].append(0)
    color = 1
    x,y = 0,0
    playing = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("again")
                playing = 1
                pan = []
                for i in range(15):
                    pan.append([])
                for i in range(15):
                    for p in range(15):
                        pan[p].append(0)
                color = 1
                screen.blit(im_pan,(0,0))
                for i in range(15):
                    for p in range(15):
                        if pan[i][p]==1:
                            toput = ( i*46.42,p*46.42)
                            screen.blit(im_black,toput)
                        if pan[i][p]==-1:
                            toput = ( i*46.42,p*46.42)  
                            screen.blit(im_white,toput)
                pygame.display.flip()              
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] != 0:
                    if playing == 1:  
                        if color == 1:
                            a = True
                            while a:
                                (x,y) = ori.decide2(pan,color)
                                if pan[x][y] == 0:
                                    a = False
                            print('black'+str((x,y)))
                            pan[x][y]=1
                            print(ori.win(pan))
                            if ori.win(pan) == 1:
                                ori.finish(1)
                                playing = 0
                            toput = ( x*46.42,y*46.42)
                            screen.blit(im_black,toput)
                            pygame.display.flip()
                            
                        if color == -1:
                            a = True
                            while a:
                                (x,y) = ori.decide2(pan,color)
                                if pan[x][y] == 0:
                                    a = False
                            toput = ( x*46.42,y*46.42)
                            pan[x][y] = -1
                            print("white"+"(%s,%s)"%(x,y))
                            screen.blit(im_white,toput)
                            pygame.display.flip()
                            print(ori.win(pan))
                            if ori.win(pan) == -1:
                                ori.finish(-1)
                                playing = 0
                        color = -color
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                     

if __name__=="__main__":
    main()
