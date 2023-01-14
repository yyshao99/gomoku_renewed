
import random


def full(pan):
    a = True
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                a = False
    return a

def tog(pan,n,color):
    allans = []
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
 
def is_sur(pan,pos,ran,color):
    sur = 0
    for p in range(-ran,ran+1):
        for q in range(-ran,ran+1):
            if pan[p][q] == color:
                sur += 1
    return sur

def to_defend3(pan,color):
    allans = []
    for i in tog(pan,3,-color):
        if i[0] == -color:
            if i[3] == 1:
                if i[2][0]-1>-1 and i[2][0]+3<15:
                    if pan[i[2][0]-1][i[2][1]] == 0 and pan[i[2][0]+3][i[2][1]] == 0:
                        if is_sur(pan,pan[i[2][0]+3][i[2][1]],2,1)>is_sur(pan,pan[i[2][0]-1][i[2][1]],2,1):
                            allans.append((i[2][0]+3,i[2][1]))
                        else:
                            allans.append((i[2][0]-1,i[2][1]))
            if i[3] == 2:
                if i[2][1]-1>-1 and i[2][1]+3<15:
                    if pan[i[2][0]][i[2][1]-1] == 0 and pan[i[2][0]][i[2][1]+3] == 0:
                        if is_sur(pan,pan[i[2][0]][i[2][1]+3],2,1)>is_sur(pan,pan[i[2][0]][i[2][1]-1],2,1):
                            allans.append((i[2][0],i[2][1]+3))
                        else:
                            allans.append((i[2][0],i[2][1]-1))
            if i[3] == 3:
                if i[2][0]-1>-1 and i[2][0]+3<15 and i[2][1]-1>-1 and i[2][1]+3<15:
                    if pan[i[2][0]-1][i[2][1]-1] == 0 and pan[i[2][0]+3][i[2][1]+3] == 0:
                        if is_sur(pan,pan[i[2][0]+3][i[2][1]+3],2,1)>is_sur(pan,pan[i[2][0]-1][i[2][1]-1],2,1):
                            allans.append((i[2][0]+3,i[2][1]+3))
                        else:
                            allans.append((i[2][0]-1,i[2][1]-1))
            if i[3] == 4:
                if i[2][0]+1 <15 and i[2][0]-3 > -1 and i[2][1]-1>-1 and i[2][1]+3<15:
                    if pan[i[2][0]+1][i[2][1]-1] == 0 and pan[i[2][0]-3][i[2][1]+3] == 0:
                        if is_sur(pan,pan[i[2][0]-3][i[2][1]+3],2,1)>is_sur(pan,pan[i[2][0]+1][i[2][1]-1],2,1):
                            allans.append((i[2][0]-3,i[2][1]+3))
                        else:
                            allans.append((i[2][0]+1,i[2][1]-1))
    return allans
def to_get3(pan,color):
    allans = []
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = color
                for i in tog(pan,3,color):
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

def to_get4 (pan,color):
    allans = []
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = color
                for i in tog(pan,4,color):
                    if i[0] == color:
                        if i[3] == 1:
                            if i[2][0]-1>-1 and i[2][0]+4<15:
                                if pan[i[2][0]-1][i[2][1]] == 0 or pan[i[2][0]+4][i[2][1]] == 0:
                                    allans.append((p,q))
                        if i[3] == 2:
                            if i[2][1]-1>-1 and i[2][1]+4<15:
                                if pan[i[2][0]][i[2][1]-1] == 0 or pan[i[2][0]][i[2][1]+4] == 0:
                                    allans.append((p,q))
                        if i[3] == 3:
                            if i[2][0]-1>-1 and i[2][0]+4<15 and i[2][1]-1>-1 and i[2][1]+4<15:
                                if pan[i[2][0]-1][i[2][1]-1] == 0 or pan[i[2][0]+4][i[2][1]+4] == 0:
                                    allans.append((p,q))
                        if i[3] == 4:
                            if i[2][0]-4>-1 and i[2][0]+1<15 and  i[2][1]-1>-1 and i[2][1]+4<15:
                                if pan[i[2][0]+1][i[2][1]-1] == 0 or pan[i[2][0]-4][i[2][1]+4] == 0:
                                    allans.append((p,q))
                pan[p][q] = 0
    if len(allans)<5:
        return allans
    else:
        return []




def to_defend_clean4(pan,color):
    allans = []
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = -color
                if is_clean4(pan,color):
                    allans.append((p,q))
                    pan[p][q] = 0
                pan[p][q] = 0
    return allans

def to_defend4(pan,color):
    allans = []
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = -color
                if is_4(pan,color):
                    allans.append((p,q))
                pan[p][q] = 0
    return allans
    

def to_defend34(pan,color):
    for i in to_defend4(pan,color):
        if to_defend3(pan,color) == []:
            pan[i[0]][i[1]] = -color
            if to_defend3(pan,color) != []:
                pan[i[0]][i[1]] = 0
                return i
            pan[i[0]][i[1]] = 0
        


def is_clean4(pan,color):
    for i in tog(pan,4,-color):
        if i[3] == 1:
            if i[2][0]-1 > -1 and i[2][0]+4< 15:
                if pan[i[2][0]-1][i[2][1]] == 0 and pan[i[2][0]+4][i[2][1]] == 0:
                    return True
        if i[3] == 2:
            if i[2][1]-1 > -1 and i[2][1]+4< 15:
                if pan[i[2][0]][i[2][1]-1] == 0 and pan[i[2][0]][i[2][1]+4] == 0:
                    return True
        if i[3] == 3:
            if i[2][0]-1 > -1 and i[2][0]+4< 15 and i[2][1]-1 > -1 and i[2][1]+4< 15:
                if pan[i[2][0]-1][i[2][1]-1] == 0 and pan[i[2][0]+4][i[2][1]+4] == 0:
                    return True
        if i[3] == 4:
            if i[2][0]+1 <15 and i[2][0]-4>-1 and i[2][0]-1 > -1 and i[2][0]+4< 15:
                if pan[i[2][0]+1][i[2][1]-1] == 0 and pan[i[2][0]-4][i[2][1]+4] == 0:
                    return True
    return False

def is_4(pan,color):
    ans = 0
    for i in tog(pan,4,-color):
        if i[3] == 1:
            if i[2][0]-1 >= 0 and i[2][0]+4<15:
                if pan[i[2][0]-1][i[2][1]] == 0 or pan[i[2][0]+4][i[2][1]] == 0:
                    ans += 1
        if i[3] == 2:
            if i[2][1]-1 >= 0 and i[2][1]+4<15:
                if pan[i[2][0]][i[2][1]-1] == 0 or pan[i[2][0]][i[2][1]+4] == 0:
                    ans += 1
        if i[3] == 3:
            if i[2][0]-1 >= 0 and i[2][0]+4<15 and i[2][1]-1 >= 0 and i[2][1]+4<15:
                if pan[i[2][0]-1][i[2][1]-1] == 0 or pan[i[2][0]+4][i[2][1]+4] == 0:
                    ans += 1
        if i[3] == 4:
            if i[2][0]+1 < 15 and i[2][0]-4 > -1 and i[2][1]-1 >= 0 and i[2][1]+4<15:
                if pan[i[2][0]+1][i[2][1]-1] == 0 or pan[i[2][0]-4][i[2][1]+4] == 0:
                    ans += 1
    return ans
                



    

def to_win(pan,color):
    for i in range(15):
        for p in range(15):
            if pan[i][p] == 0:
                pan[i][p] = color
                if tog(pan,5,color)!=[]:
                    pan[i][p] = 0
                    return (i,p)
                pan[i][p] = 0

def to_defend(pan,color):
    for i in range(15):
        for p in range(15):
            if pan[i][p] == 0:
                pan[i][p] = -color
                if tog(pan,5,-color)!=[]:
                    pan[i][p] = 0
                    return (i,p)
                pan[i][p] = 0
                
def to_defend_double4(pan,color):
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = -color
                if is_4 == 2:
                    pan[p][q] = 0
                    return (p,q)
                pan[p][q] = 0

def to_defend_double3(pan,color):
    for i in range(15):
        for p in range(15):
            if pan[i][p] == 0:
                pan[i][p] = -color
                if len(to_defend3(pan,color)) > 1:
                    pan[i][p] = 0
                    return (i,p)
                pan[i][p] = 0

def finish(color):
    print("finish")
    if color == 1:
        print("Conguatulations! black wins")
    if color == 2:
        print("Conguatulations! white wins")

def win(pan):
    for p in range(11):
        for q in range(11):
            a = True
            for i in range(4):
                if pan[p+i+1][q]!=pan[p][q]:
                    a = False
            if  a:
                return pan[p][q]
            a = True
            for i in range(4):
                if pan[p][q+i+1]!=pan[p][q]:
                    a = False
            if a:
                return pan[p][q]
            a = True
            for i in range(4):
                if pan[p+i+1][q+i+1]!=pan[p][q]:
                    a = False
            if a:
                return pan[p][q]
            a = True
            for i in range(4):
                if pan[p+i+1][q-i+3]!=pan[p][q+4]:
                    a = False
            if a:
                return pan[p][q+4]
            
    return 0
def initialize():
    pan = []
    for i in range(15):
        pan.append([])
    for i in range(15):
        for p in range(15):
            pan[p].append(0)
    return pan



def decide(pan,color):
    x,y = -1,-1
    if to_defend_double3(pan,color) != None:
        (x,y) = to_defend_double3(pan,color)
        a = 'double3'
    if to_get3(pan,color) != []:
        (x,y) = to_get3(pan,color)[0]
        a = 'get3'
    if to_get4(pan,color) != []:
        (x,y) = to_get4(pan,color)[0]
        a = 'get4'
    if to_defend_clean4(pan,color) !=[]:
        (x,y) = to_defend_clean4(pan,color)[0]
        a = 'def clean 4'
    if to_defend3(pan,color) != []:
        a = 'def3'
        (x,y) = to_defend3(pan,color)[0]
    if to_defend34(pan,color) != None:
        a = 'def34'
        (x,y) = to_defend34(pan,color)
    if to_defend_double4(pan,color) != None:
        (x,y) = to_defend_double4(pan,color)
        a = 'def double4'
    if to_defend(pan,color) != None:
        (x,y) = to_defend(pan,color)
        a = 'def5'
    if to_win(pan,color) != None:
        (x,y) = to_win(pan,color)
        a = 'get5'
    pan1 = initialize()
    if pan == pan1:
        (x,y)=(7,7)
        a = 'first'
    if x == -1 and y == -1:
        (x,y) = decide2(pan,color)
        a = 'scan'
    print(a)
    pan[x][y] = color
    return (x,y)

def value(a,color):
    a *= color
    if a == 0:
        return 0 
    if a == 1:
        return 3
    if a == 2:
        return 10
    if a == 3:
        return 30
    if a == 4: 
        return 100
    if a == -1:
        return 4
    if a == -2:
        return 12
    if a == -3:
        return 25
    if a == -4:
        return 80
    else:
        print('false')
        print(a)

def scan(pan,color):
    pan1 = initialize()
    for i in range(15):
        for p in range(15):
            if pan[i][p]==0:
                s = 0
                for t in range(5):
                    if i-t >= 0 and i-t+4 < 15:
                        a = 0
                        for q in range(5):
                            a += pan[i-t+q][p]
                        s += value(a,color)
                for t in range(5):
                    if p-t>=0 and p-t+4 <15:
                        a = 0
                        for q in range(5):
                            a += pan [i][p-t+q]
                        s  += value(a,color)
                for t in range(5):
                    if p-t>=0 and p-t+4 <15 and i-t >= 0 and i-t+4 < 15:
                        a = 0
                        for q in range(5):
                            a += pan [i-t+q][p-t+q]
                        s  += value(a,color)
                for t in range(5):
                    if p+t < 15 and p+t-4 >= 0 and i-t >= 0 and i-t+4 < 15:
                        a = 0
                        for q in range(5):
                            a += pan [i-t+q][p+t-q]
                        s  += value(a,color)
                pan1[i][p]=s
            else:
                pan1[i][p] = 0
    return pan1

def decide2(pan,color):
    pan1 = initialize()
    if pan == pan1:
        return (7,7)
    pan1 = scan(pan,color)
    a = 0
    t = []
    for i in range(15):
        for q in range(15):
            if pan1[i][q]>a:
                a = pan1[i][q]
    for i in range(15):
        for q in range(15):
            if pan1[i][q] == a:
                t.append((i,q))
    c = random.randint(0,len(t)-1)
    return t[c]
                
            


