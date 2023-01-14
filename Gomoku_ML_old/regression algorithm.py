#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:10:37 2019

@author: young
"""

import torch
import numpy as np
import matplotlib.pyplot as plt

x = torch.unsqueeze(torch.linspace(-1,1,100),dim = 1)
y = x.pow(2)+0.3*torch.rand(x.size())



class Net(torch.nn.Module):
    def __init__(self,n_feature,n_hidden,n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature,n_hidden) 
        self.predict = torch.nn.Linear(n_hidden,n_output)
    
    def forward(self,x):
        x = torch.nn.functional.relu(self.hidden(x))
        x = self.predict(x)
        return x

net = Net(1,10,1)
print(net)

optimizer = torch.optim.SGD(net.parameters(),lr = 0.2)
loss_func = torch.nn.MSELoss()

plt.ion() 

for t in range(200):
    prediction = net(x)
    loss = loss_func(prediction,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if t % 5 == 0:
        # plot and show learning process
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color':  'red'})
        plt.pause(0.1)

plt.ioff()
plt.show()