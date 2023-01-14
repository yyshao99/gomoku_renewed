def win(pan):
    for color in [-1,1]:
        for i in range(15):
            for j in range(15):
                w1 = False
                w2 = False
                w3 = False
                w4 = False
                if j < 11:
                    w1 = True
                    for k in range(5):
                        w1 = w1 and (pan[i][j+k] == color)
                
                if i < 11:
                    w2 = True
                    for k in range(5):
                        w2 = w2 and (pan[i+k][j] == color)
                
                if i < 11 and j < 11:
                    w3 = True
                    for k in range(5):
                        w3 = w3 and (pan[i+k][j+k] == color)
                
                if i < 11 and j > 3:
                    w4 = True
                    for k in range(5):
                        w4 = w4 and (pan[i+k][j-k] == color)
                if w1 or w2 or w3 or w4:
                    return True
    return False
                