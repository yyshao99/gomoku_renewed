import torch
import numpy as np
import matplotlib.pyplot as plt

n_data = torch.ones(100,2)
x1 = torch.normal(2*n_data,1)
y1 = torch.zeros(100)
x2 = torch.normal(-2*n_data,1)
y2 = torch.ones(100)
x = torch.cat((x1,x2),0).type(torch.FloatTensor)
y = torch.cat((y1,y2),).type(torch.LongTensor)
plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=y.data.numpy(), s=100, lw=0, cmap='RdYlGn')
plt.show()


class Net(torch.nn.Module):
    def __init__(self, n1, n2, n3):
        super(Net,self).__init__()
        self.hidden = torch.nn.Linear(n1,n2)
        self.out = torch.nn.Linear(n2,n3)

    def forward(self, x):
        x = torch.nn.functional.relu(self.hidden(x))      # activation function for hidden layer
        x = self.out(x)
        return x

net = Net(2,10,2)
print(net)

optimizer = torch.optim.SGD(net.parameters(),lr = 0.02)
loss_func = torch.nn.CrossEntropyLoss()
plt.ion
for t in range(100):
    out = net(x)
    loss = loss_func(out,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if t % 2 == 0:
        plt.cla()
        prediction = torch.max(out, 1)[1]
        pred_y = prediction.data.numpy()
        target_y = y.data.numpy()
        plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=pred_y, s=100, lw=0, cmap='RdYlGn')
        accuracy = float((pred_y == target_y).astype(int).sum()) / float(target_y.size)
        plt.text(1.5, -4, 'Accuracy=%.2f' % accuracy, fontdict={'size': 20, 'color':  'red'})
        plt.pause(1)
plt.ioff()
plt.show()
