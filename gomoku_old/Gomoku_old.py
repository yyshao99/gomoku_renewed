
import pygame
import random

def to_defend3(pan):
    allans = []
    for i in tog(pan,3,1):
        if i[0] == 1:
            if i[3] == 1:
                if pan[i[2][0]-1][i[2][1]] == 0 and pan[i[2][0]+3][i[2][1]] == 0:
                    if is_sur(pan,pan[i[2][0]+3][i[2][1]],2,1)>is_sur(pan,pan[i[2][0]-1][i[2][1]],2,1):
                        allans.append((i[2][0]+3,i[2][1]))
                    else:
                        allans.append((i[2][0]-1,i[2][1]))
            if i[3] == 2:
                if pan[i[2][0]][i[2][1]-1] == 0 and pan[i[2][0]][i[2][1]+3] == 0:
                    if is_sur(pan,pan[i[2][0]][i[2][1]+3],2,1)>is_sur(pan,pan[i[2][0]][i[2][1]-1],2,1):
                        allans.append((i[2][0],i[2][1]+3))
                    else:
                        allans.append((i[2][0],i[2][1]-1))
            if i[3] == 3:
                if pan[i[2][0]-1][i[2][1]-1] == 0 and pan[i[2][0]+3][i[2][1]+3] == 0:
                    if is_sur(pan,pan[i[2][0]+3][i[2][1]+3],2,1)>is_sur(pan,pan[i[2][0]-1][i[2][1]-1],2,1):
                        allans.append((i[2][0]+3,i[2][1]+3))
                    else:
                        allans.append((i[2][0]-1,i[2][1]-1))
            if i[3] == 4:
                if pan[i[2][0]+1][i[2][1]-1] == 0 and pan[i[2][0]-3][i[2][1]+3] == 0:
                    if is_sur(pan,pan[i[2][0]-3][i[2][1]+3],2,1)>is_sur(pan,pan[i[2][0]+1][i[2][1]-1],2,1):
                        allans.append((i[2][0]-3,i[2][1]+3))
                    else:
                        allans.append((i[2][0]+1,i[2][1]-1))
    return allans
def to_get3(pan):
    allans = []
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = 2
                for i in tog(pan,3,2):
                    if i[0] == 2:
                        if i[3] == 1:
                            if pan[i[2][0]-1][i[2][1]] == 0 and pan[i[2][0]+3][i[2][1]] == 0:
                                allans.append((p,q))
                        if i[3] == 2:
                            if pan[i[2][0]][i[2][1]-1] == 0 and pan[i[2][0]][i[2][1]+3] == 0:
                                allans.append((p,q))
                        if i[3] == 3:
                            if pan[i[2][0]-1][i[2][1]-1] == 0 and pan[i[2][0]+3][i[2][1]+3] == 0:
                                allans.append((p,q))
                        if i[3] == 4:
                            if pan[i[2][0]+1][i[2][1]-1] == 0 and pan[i[2][0]-3][i[2][1]+3] == 0:
                                allans.append((p,q))
                pan[p][q] = 0
    return allans

def to_get4 (pan):
    allans = []
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = 2
                for i in tog(pan,4,2):
                    if i[0] == 2:
                        if i[3] == 1:
                            if pan[i[2][0]-1][i[2][1]] == 0 or pan[i[2][0]+4][i[2][1]] == 0:
                                allans.append((p,q))
                        if i[3] == 2:
                            if pan[i[2][0]][i[2][1]-1] == 0 or pan[i[2][0]][i[2][1]+4] == 0:
                                allans.append((p,q))
                        if i[3] == 3:
                            if pan[i[2][0]-1][i[2][1]-1] == 0 or pan[i[2][0]+4][i[2][1]+4] == 0:
                                allans.append((p,q))
                        if i[3] == 4:
                            if pan[i[2][0]+1][i[2][1]-1] == 0 or pan[i[2][0]-4][i[2][1]+4] == 0:
                                allans.append((p,q))
                pan[p][q] = 0
    return allans




def to_defend_clean4(pan):
    allans = []
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = 1
                if is_clean4(pan):
                    allans.append((p,q))
                    pan[p][q] = 0
                pan[p][q] = 0
    return allans

def to_defend4(pan):
    allans = []
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = 1
                if is_4(pan):
                    allans.append((p,q))
                pan[p][q] = 0
    return allans
    

def to_defend34(pan):
    for i in to_defend4(pan):
        if to_defend3(pan) == []:
            pan[i[0]][i[1]] = 1
            if to_defend3(pan) != []:
                pan[i[0]][i[1]] = 0
                return i
            pan[i[0]][i[1]] = 0
        


def is_clean4(pan):
    ans = []
    for i in tog(pan,4,1):
        if i[3] == 1:
            if pan[i[2][0]-1][i[2][1]] == 0 and pan[i[2][0]+4][i[2][1]] == 0:
                return True
        if i[3] == 2:
            if pan[i[2][0]][i[2][1]-1] == 0 and pan[i[2][0]][i[2][1]+4] == 0:
                return True
        if i[3] == 3:
            if pan[i[2][0]-1][i[2][1]-1] == 0 and pan[i[2][0]+4][i[2][1]+4] == 0:
                return True
        if i[3] == 4:
            if pan[i[2][0]+1][i[2][1]-1] == 0 and pan[i[2][0]-4][i[2][1]+4] == 0:
                return True
    return False
def is_4(pan):
    ans = 0
    for i in tog(pan,4,1):
        if i[3] == 1:
            if pan[i[2][0]-1][i[2][1]] == 0 or pan[i[2][0]+4][i[2][1]] == 0:
                ans += 1
        if i[3] == 2:
            if pan[i[2][0]][i[2][1]-1] == 0 or pan[i[2][0]][i[2][1]+4] == 0:
                ans += 1
        if i[3] == 3:
            if pan[i[2][0]-1][i[2][1]-1] == 0 or pan[i[2][0]+4][i[2][1]+4] == 0:
                ans += 1
        if i[3] == 4:
            if pan[i[2][0]+1][i[2][1]-1] == 0 or pan[i[2][0]-4][i[2][1]+4] == 0:
                ans += 1
    return ans
                



    
def is_sur(pan,pos,ran,color):
    sur = 0
    for p in range(-ran,ran+1):
        for q in range(-ran,ran+1):
            if pan[p][q] == color:
                sur += 1
    return sur
def to_win(pan):
    for i in range(15):
        for p in range(15):
            if pan[i][p] == 0:
                pan[i][p] = 2
                if win(pan,5,1) == 1:
                    pan[i][p] = 0
                    return (i,p)
                pan[i][p] = 0

def to_defend(pan):
    for i in range(15):
        for p in range(15):
            if pan[i][p] == 0:
                pan[i][p] = 1
                if win(pan,5,1) == 1:
                    pan[i][p] = 0
                    return (i,p)
                pan[i][p] = 0
def to_defend_double4(pan):
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = 1
                if is_4 == 2:
                    pan[p][q] = 0
                    return (p,q)
                pan[p][q] = 0

def to_defend_double3(pan):
    for i in range(15):
        for p in range(15):
            if pan[i][p] == 0:
                pan[i][p] = 1
                if len(to_defend3(pan)) > 1:
                    pan[i][p] = 0
                    return (i,p)
                pan[i][p] = 0

def finish(color):
    print("finish")
    if color == 1:
        print("Conguatulations! black wins")
    if color == 2:
        print("Conguatulations! white wins")
def tog(pan,n,color):
    allans = []
    for color in [color]:
        for i in range(15):
            for p in range(15):
                if pan[i][p] == color:
                    wincon = 0
                    for con in range(n):
                        if i+con <= 14:
                            if pan[i+con][p] == color:
                                wincon += 1
                            else:
                                pass
                    if wincon == n:
                        allans.append([color,n,[i,p],1])
                    wincon = 0
                    for con in range(n):
                        if p+con <= 14:
                            if pan[i][p+con] == color:
                                wincon += 1
                            else:
                                pass
                    if wincon == n:
                        allans.append([color,n,[i,p],2])
                    wincon = 0
                    for con in range(n):
                        if i+con<=14 and p+con <=14:
                            if pan[i+con][p+con] == color:
                                wincon += 1
                            else:
                                pass
                    if wincon == n:
                        allans.append([color,n,[i,p],3])
                    wincon = 0
                    for con in range(n):
                        if i-con >= 0 and p+con <= 14:
                            if pan[i-con][p+con] == color:
                                wincon += 1
                            else:
                                pass
                    if wincon == n:
                        allans.append([color,n,[i,p],4])
    return allans
 

def win(pan,n,test):
    for color in [1,2]:
        for i in range(15):
            for p in range(15):
                if pan[i][p] == color:
                    wincon = 0
                    for con in range(n):
                        if i+con <= 14:
                            if pan[i+con][p] == color:
                                wincon += 1
                            else:
                                pass
                    if wincon == n:
                        if test == 0:
                            finish(color)
                        return 1
                    wincon = 0
                    for con in range(n):
                        if p+con <= 14:
                            if pan[i][p+con] == color:
                                wincon += 1
                            else:
                                pass
                    if wincon == n:
                        if test == 0:
                            finish(color)
                        return 1
                    wincon = 0
                    for con in range(n):
                        if i+con<=14 and p+con <=14:
                            if pan[i+con][p+con] == color:
                                wincon += 1
                            else:
                                pass
                    if wincon == n:
                        if test == 0:
                            finish(color)
                        return 1
                    wincon = 0
                    for con in range(n):
                        if i-con >= 0 and p+con <= 14:
                            if pan[i-con][p+con] == color:
                                wincon += 1
                            else:
                                pass
                    if wincon == n:
                        if test == 0:
                            finish(color)
                        return 1

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
    pan = []
    for i in range(15):
        pan.append([])
    for i in range(15):
        for p in range(15):
            pan[p].append(0)
    color = 1
    playing = 1
    music = 0
    while running:
        for event in pygame.event.get():
            if color == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[1] <= 700:
                        if playing == 1:
                            x_axis = int((pos[0])//46.42)
                            y_axis = int((pos[1])//46.42)
                            if pan[x_axis][y_axis] == 0:
                                print("black"+"(%s,%s)"%(x_axis,y_axis))
                                pan[x_axis][y_axis] = 1
                                screen.blit(im_pan,(0,0))
                                for i in range(15):
                                    for p in range(15):
                                        if pan[i][p]==1:
                                            toput = ( i*46.42,p*46.42)
                                            screen.blit(im_black,toput)
                                        if pan[i][p]==2:
                                            toput = ( i*46.42,p*46.42)
                                            screen.blit(im_white,toput)
                                if music == 1:
                                    pygame.mixer.Channel(2).play(sound)
                                pygame.display.flip()
                                color = -(color-1.5)+1.5
                                if win(pan,5,0) == 1:
                                    playing = 0
                                    screen.blit(im_finishblack,(300,0))
                                    pygame.display.flip()
                    if pos[1] > 700:
                        if pos[0] <= 350:
                            print("again")
                            pan = []
                            for i in range(15):
                                pan.append([])
                            for i in range(15):
                                for p in range(15):
                                    pan[p].append(0)
                            color = 1
                            playing = 1
                            screen.blit(im_pan,(0,0))
                            for i in range(15):
                                for p in range(15):
                                    if pan[i][p]==1:
                                        toput = ( i*46.42,p*46.42)
                                        screen.blit(im_black,toput)
                                    if pan[i][p]==2:
                                        toput = ( i*46.42,p*46.42)  
                                        screen.blit(im_white,toput)
                            pygame.display.flip()
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
                            
            if color == 2:
                x = random.randint(x_axis-1,x_axis+1)
                y = random.randint(y_axis-1,y_axis+1)
                
                
                if pan[x][y] == 0:
                    toput = ( x*46.42,y*46.42)
                    if color == 2:
                        pan[x][y] = 2
                        print("white"+"(%s,%s)"%(x,y))
                        screen.blit(im_pan,(0,0))
                        for i in range(15):
                            for p in range(15):
                                if pan[i][p]==1:
                                    toput = ( i*46.42,p*46.42)
                                    screen.blit(im_black,toput)
                                if pan[i][p]==2:
                                    toput = ( i*46.42,p*46.42)  
                                    screen.blit(im_white,toput)
                        pygame.display.flip()
                    color = -(color-1.5)+1.5
                    if win(pan,5,0) == 1:
                        playing = 0
                        screen.blit(im_finishwhite,(300,0))
                        pygame.display.flip()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
     

if __name__=="__main__":
    main()
