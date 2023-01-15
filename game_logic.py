
import random
import numpy as np
import ui

class GameLogic:
    def __init__(self):
        self.pan = np.zeros((15,15))
        self.player_turn = 1
        self.playing = True
        self.ui = ui.UI()
    
    def play_chess(self,pos):
        if self.pan[pos[0],pos[1]] == 0:
            self.pan[pos[0],pos[1]] = self.player_turn
            self.player_turn *= -1