import torch.nn as nn
import torch.nn.functional as F


class DQN(nn.Module):   # from pytorch documentation

    def __init__(self, n_observations, n_actions):
        super(DQN, self).__init__()
        self.layer1 = nn.Linear(n_observations, 256)
        self.layer2 = nn.Linear(256, n_actions)

    def forward(self, x):
        x = F.relu(self.layer1(x))
        return self.layer2(x)
