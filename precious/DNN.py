

import torch
import torch.nn as nn
import torch.nn.functional as F


class Model(nn.Module):
    def __init__(self, input_size,hidden_size,output_size):
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, input):
        return self.linear2(F.relu(self.linear1(input)))

x = torch.randn(32,100)
y = torch.randn(32, 1)

model = Model(100,200,1)
Loss = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

for i in range(epoch):
    pred = model(x)
    loss = Loss(pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
