

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
