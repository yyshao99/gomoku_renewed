
import random
import numpy as np
from win import win


def judge_random(pan):
    while True:
        x = random.randint(0,14)
        y = random.randint(0,14)
        if pan[x][y] == 0:
            return (x,y)

def judge_basic(pan,color):
    """
    if to_defend_double3(pan,color) != None:
        print("according to defend double3")
        (x,y) = to_defend_double3(pan,color)
    """
    x,y = judge_cyy(pan,color)
    print('0')
    if to_get3(pan,color) != None:
        print("according to get3")
        (x,y) = to_get3(pan,color)
    print('1')
    if to_get4(pan,color) != None:
        print("according to get4")
        (x,y) = to_get4(pan,color)
    """
    if to_get_double3(pan,color) != None:
        print("according to get double3")
        (x,y) = to_defend_double3(pan,color)
    """
    if to_defend_clean4(pan,color) !=None:
        print("according to clean4")
        (x,y) = to_defend_clean4(pan,color)
    print('2')
    if to_defend3(pan,color) != None:
        print("according to 3")
        (x,y) = to_defend3(pan,color)
    print('3')
    """
    if to_defend34(pan,color) != None:
        print("according to defend 34")
        (x,y) = to_defend34(pan,color)
    if to_get34(pan,color) != None:
        print("according to get 34")
        (x,y) = to_defend34(pan,color)
    """
    if to_defend_double4(pan,color) != None:
        print("according to defend Double4")
        (x,y) = to_defend_double4(pan,color)
    print('4')
    if to_get_double4(pan,color) != None:
        print("according to get Double4")
        (x,y) = to_get_double4(pan,color)
    print('5')
    if to_defend4(pan,color) != None:
        print("according to defend4")
        (x,y) = to_defend4(pan,color)
    print('6')
    if to_win(pan,color) != None:
        print("according to win")
        (x,y) = to_win(pan,color)
    print('7')
    return x,y


def to_win(pan,color):
    for i in range(15):
        for p in range(15):
            if pan[i][p] == 0:
                pan[i][p] = color
                if win(pan):
                    pan[i][p] = 0
                    return (i,p)
                pan[i][p] = 0

def to_defend4(pan,color):
    for i in range(15):
        for p in range(15):
            if pan[i][p] == 0:
                pan[i][p] = -color
                if win(pan):
                    pan[i][p] = 0
                    return (i,p)
                pan[i][p] = 0
    
def to_get_double4(pan,color):
    for i in range(15):
        for j in range(15):
            if pan[i][j] == 0:
                pan[i][j] = color
                if to_defend4(pan,-color) != None:
                    pan[to_defend4(pan,-color)[0]][to_defend4(pan,-color)[1]] = -color
                    if to_defend4(pan,-color) != None:
                        pan[to_defend4(pan,-color)[0]][to_defend4(pan,-color)[1]] = 0
                        pan[i][j] = 0
                        return i,j

def to_defend_double4(pan,color):
    for i in range(15):
        for j in range(15):
            if pan[i][j] == 0:
                pan[i][j] = -color
                if to_defend4(pan,color) != None:
                    pan[to_defend4(pan,color)[0]][to_defend4(pan,color)[1]] = color
                    if to_defend4(pan,color) != None:
                        pan[to_defend4(pan,color)[0]][to_defend4(pan,color)[1]] = 0
                        pan[i][j] = 0
                        return i,j


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
                    allans.append([color,n,(i,p),1])
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

def to_get34(pan,color):
    for i in to_defend4(pan):
        if to_defend3(pan) == []:
            pan[i[0]][i[1]] = 1
            if to_defend3(pan) != []:
                pan[i[0]][i[1]] = 0
                return i
            pan[i[0]][i[1]] = 0

def to_defend34(pan,color):
    for i in to_defend4(pan):
        if to_defend3(pan) == []:
            pan[i[0]][i[1]] = 1
            if to_defend3(pan) != []:
                pan[i[0]][i[1]] = 0
                return i
            pan[i[0]][i[1]] = 0

def to_get_double3(pan,color):
    for i in range(15):
        for p in range(15):
            if pan[i][p] == 0:
                pan[i][p] = 1
                if len(to_defend3(pan)) > 1:
                    pan[i][p] = 0
                    return (i,p)
                pan[i][p] = 0

def to_defend_double3(pan,color):
    for i in range(15):
        for p in range(15):
            if pan[i][p] == 0:
                pan[i][p] = 1
                if len(to_defend3(pan)) > 1:
                    pan[i][p] = 0
                    return (i,p)
                pan[i][p] = 0




def cyy_provide_value(pan,color):
    val = np.zeros((15,15))
    for color in [-1,1]:
        for i in range(15):
            for j in range(15):
                if j < 11:
                    s = 0
                    for k in range(5):
                        s += pan[i][j+k]
                    s = -color*s
                    for k in range(5):
                        val[i][j+k] += value_list(s)
                if i < 11:
                    s = 0
                    for k in range(5):
                        s += pan[i+k][j]
                    s = -color*s
                    for k in range(5):
                        val[i+k][j] += value_list(s)
                
                if i < 11 and j < 11:
                    s = 0
                    for k in range(5):
                        s += pan[i+k][j+k]
                    s = -color*s
                    for k in range(5):
                        val[i+k][j+k] += value_list(s)
                
                if i < 11 and j > 3:
                    s = 0
                    for k in range(5):
                        s += pan[i+k][j-k]
                    s = -color*s
                    for k in range(5):
                        val[i+k][j-k] += value_list(s)
    

    return val

#def_clean_3: prereq for to_defend3
def defend_clean_3(pan,color):
    allans = []
    for i in tog(pan,3,-color):
    #color 下， 看对手
        if i[0] == 1:
            if i[3] == 1:
                if 0<i[2][0]<12:
                    if pan[i[2][0]-1][i[2][1]] == 0 and pan[i[2][0]+3][i[2][1]] == 0:
                        allans.append((i[2][0]-1,i[2][1]))
                        allans.append((i[2][0]+3,i[2][1]))

            if i[3] == 2:
                if 0<i[2][1]<12:
                    if pan[i[2][0]][i[2][1]-1] == 0 and pan[i[2][0]][i[2][1]+3] == 0:
                        allans.append((i[2][0],i[2][1]-1))
                        allans.append((i[2][0],i[2][1]+3))
                    
            if i[3] == 3:
                if 0<i[2][1]<12 and 0<i[2][0]<12:
                    if pan[i[2][0]-1][i[2][1]-1] == 0 and pan[i[2][0]+3][i[2][1]+3] == 0:
                        allans.append((i[2][0]-1,i[2][1]-1))
                        allans.append((i[2][0]+3,i[2][1]+3))
                    
            if i[3] == 4:
                if 2<i[2][1]<14 and 0<i[2][0]<12:
                    if pan[i[2][0]+1][i[2][1]-1] == 0 and pan[i[2][0]-3][i[2][1]+3] == 0:
                        allans.append((i[2][0]+1,i[2][1]-1))
                        allans.append((i[2][0]-3,i[2][1]+3))
    return allans

def to_defend3(pan,color):
    l = defend_clean_3(pan,color)
    if l != []:
        k = 0
        s = 0
        val = cyy_provide_value(pan,color)
        for i in l:
            if val[i[0]][i[1]]>s:
                s = val[i[0]][i[1]]
                k = 1
        return i
#get_clean_3: prereq for to_get3
def get_clean_3(pan,color):
    allans = []
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = color
                if defend_clean_3(pan,-color) != []:
                    allans.append((p,q))
                pan[p][q] = 0
    return allans

def to_get3(pan,color):
    l = get_clean_3(pan,color)
    if l != []:
        k = 0
        s = 0
        val = cyy_provide_value(pan,color)
        for i in l:
            if val[i[0]][i[1]]>s:
                s = val[i[0]][i[1]]
                k = 1
        return i

def pre_to_get4 (pan,color):
    allans = []
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = color
                if to_defend4(pan,-color)!=None:
                    allans.append((p,q))
                    pan[p][q] = 0
    return allans

def to_get4 (pan,color):
    l = pre_to_get4(pan,color)
    if l != []:
        k = 0
        s = 0
        val = cyy_provide_value(pan,color)
        for i in l:
            if val[i[0]][i[1]]>s:
                s = val[i[0]][i[1]]
                k = 1
        return i

def to_defend_clean4(pan,color):
    allans = []
    for p in range(15):
        for q in range(15):
            if pan[p][q] == 0:
                pan[p][q] = -color
                if is_clean4(pan):
                    allans.append((p,q))
                    pan[p][q] = 0
                pan[p][q] = 0
    return allans


def is_clean4(pan):
    ans = []
    for i in tog(pan,4,1):
        if i[3] == 1:
            if 0<i[2][0]<11:
                if pan[i[2][0]-1][i[2][1]] == 0 and pan[i[2][0]+4][i[2][1]] == 0:
                    return True
        if i[3] == 2:
            if 0<i[2][1]<11:
                if pan[i[2][0]][i[2][1]-1] == 0 and pan[i[2][0]][i[2][1]+4] == 0:
                    return True
        if i[3] == 3:
            if 0<i[2][0]<11 and 0<i[2][1]<11:
                if pan[i[2][0]-1][i[2][1]-1] == 0 and pan[i[2][0]+4][i[2][1]+4] == 0:
                    return True
        if i[3] == 4:
            if 3<i[2][0]<14 and 0<i[2][1]<11:
                if pan[i[2][0]+1][i[2][1]-1] == 0 and pan[i[2][0]-4][i[2][1]+4] == 0:
                    return True
    return False
                   
def is_sur(pan,pos,ran,color):
    sur = 0
    for p in range(-ran,ran+1):
        for q in range(-ran,ran+1):
            if pan[p][q] == color:
                sur += 1
    return sur





def value_list(n):
    if n == 1:
        return 5
    if n == 2:
        return 50
    if n == 3:
        return 500
    if n == 4:
        return 5000
    if n == 0:
        return 1
    if n == -1:
        return 4
    if n == -2:
        return 40
    if n == -3:
        return 400
    if n == -4:
        return 10000


def judge_cyy(pan,color):
    val = np.zeros((15,15))
    for color in [-1,1]:
        for i in range(15):
            for j in range(15):
                if j < 11:
                    s = 0
                    for k in range(5):
                        s += pan[i][j+k]
                    s = -color*s
                    for k in range(5):
                        val[i][j+k] += value_list(s)
                if i < 11:
                    s = 0
                    for k in range(5):
                        s += pan[i+k][j]
                    s = -color*s
                    for k in range(5):
                        val[i+k][j] += value_list(s)
                
                if i < 11 and j < 11:
                    s = 0
                    for k in range(5):
                        s += pan[i+k][j+k]
                    s = -color*s
                    for k in range(5):
                        val[i+k][j+k] += value_list(s)
                
                if i < 11 and j > 3:
                    s = 0
                    for k in range(5):
                        s += pan[i+k][j-k]
                    s = -color*s
                    for k in range(5):
                        val[i+k][j-k] += value_list(s)
    
    top10 = []
    top10_value = []
    for i in range(15):
        for j in range(15):
            if pan[i][j] == 0:
                if len(top10)<9:
                    top10.append((i,j))
                    top10_value.append(val[i][j])
                elif len(top10) == 9:
                    top10.append((i,j))
                    top10_value.append(val[i][j])
                    for p in range(10):
                        for q in range(9-p):
                            if top10_value[p+q] < top10_value[p+q+1]:
                                top10_value[p+q],top10_value[p+q+1] = top10_value[p+q+1],top10_value[p+q]
                                top10[p+q],top10[p+q+1] = top10[p+q+1],top10[p+q]
                else:
                    if val[i][j] > top10_value[9]:
                        top10_value.pop()
                        top10.pop()
                        top10_value.append(val[i][j])
                        top10.append((i,j))
                        for k in range(9):
                            if top10_value[9-k]>top10_value[8-k]:
                                top10_value[9-k],top10_value[8-k] = top10_value[8-k],top10_value[9-k]
                                top10[9-k],top10[8-k] = top10[8-k],top10[9-k]
    
    return top10[0][0],top10[0][1]
    # We didn't use top10 method
    """
    s = 0
    for i in range(10):
        s+= top10_value[i]
    k = random.randint(1,s)
    for i in range(10):
        if k <= top10_value[i]:
            return top10[i][0],top10[i][1]
        k -= top10_value[i]
    """

    


                