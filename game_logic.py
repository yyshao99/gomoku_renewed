
import random
import numpy as np
import ui

class GameLogic:
    def __init__(self):
        self.pan = np.zeros((15,15))
        self.player_turn = 1
        self.playing = True
    
    def play_chess(self,pos):
        if self.playing:
            if self.pan[pos[0],pos[1]] == 0:
                self.pan[pos[0],pos[1]] = self.player_turn
                self.player_turn *= -1
                return -self.player_turn
        return None

    def replay(self):
        self.pan = np.zeros((15,15))
        self.player_turn = 1
        self.playing = True

    def win(self):
        # check rows
        for i in range(11):
            for j in range(15):
                if sum(self.pan[i:i+5,j]) == 5:
                    self.playing = False
                    return 1
                if sum(self.pan[i:i+5,j]) == -5:
                    self.playing = False
                    return -1
        # check columns
        for i in range(11):
            for j in range(15):
                if sum(self.pan[j,i:i+5]) == 5:
                    self.playing = False
                    return 1
                if sum(self.pan[j,i:i+5]) == -5:
                    self.playing = False
                    return -1
        # check diagonals
        for i in range(11):
            for j in range(11):
                if sum(self.pan[i:i+5,j:j+5].diagonal()) == 5:
                    self.playing = False
                    return 1
                if sum(self.pan[i:i+5,j:j+5].diagonal()) == -5:
                    self.playing = False
                    return -1
        # check anti-diagonals
        for i in range(11):
            for j in range(11):
                part = self.pan[i:i+5,j:j+5]
                if sum(np.fliplr(part).diagonal()) == 5:
                    self.playing = False
                    return 1
                if sum(np.fliplr(part).diagonal()) == -5:
                    self.playing = False
                    return -1
        return 0