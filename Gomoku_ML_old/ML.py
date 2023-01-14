#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 17:25:49 2019

@author: young
"""
import numpy as np
import torch
import torch.nn as nn
import torch.utils.data as Data
import torchvision
import matplotlib.pyplot as plt
import original as ori
import random
EPOCH = 20               
BATCH_SIZE = 50
LR = 0.1             # learning rate

a = []
b = []
for i in range(10):
    pan = ori.initialize()
    play = True
    color = 1
    while play:
        (x,y)=ori.decide2(pan,color)
        pan[x][y] = color
        a.append([pan])
        c = x * 15 + y
        b.append(c)
        if ori.tog(pan,5,color)!=[]:
            play = False
            print(str(i)+""+str(color))
        if ori.full(pan):
            play = False
            print(str(i)+'full')
        color = -color
data_a = torch.tensor(a,dtype=torch.float32)
data_b = torch.tensor(b,dtype=torch.float32)

print(data_a.size())
print(data_b.size())
train_data = Data.TensorDataset(data_a, data_b)
train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(
             1,16,5,1,padding = 2
            ),
        nn.ReLU()
        ),
        self.conv2 = nn.Sequential(
            nn.Conv2d(
                16,32,5,1,padding = 2
            ),
            nn.ReLU()
        ),
        self.out = torch.nn.Linear(32*15*15,225)

    def forward(self,x):
        x = self.conv1(x)
        x = self.conv2(x)        # flatten the output of conv2 to (batch_size, 32 * 7 * 7)
        output = self.out(x)
        return output


cnn = CNN()
print(cnn)


optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)   # optimize all cnn parameters
loss_func = nn.CrossEntropyLoss()     

for epoch in range(EPOCH):
    output = cnn(data_a)
    loss = loss_func(output,data_b)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    

