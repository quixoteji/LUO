import numpy as np

#
# Configuration
#

# Number of MBSs
MBS = 1
# Number of SBSs
SBS = 10
# Number of users
UE = 100

# Quality threshold of user
QoUE = 10
# Power of MBS
PoMBS = 1000
# Power of SBS
# PoSBS = 40
PoSBS = 1000
# Number of SBS a user can reach
noSBS = 3

class Scenario(object):
    def __init__(self):
        
        self.state = np.zeros((UE, (MBS+SBS))) 
        self.action = np.zeros((UE, (MBS+SBS)))

        self.action_size = self.action.size
        self.state_size = self.state.size

    def reset(self):
        self.state = np.zeros((UE, (MBS+SBS)))
        return self.state

    def step(self, action):
        action = action.reshape(100,11)
        self.state = self.state + action
        next_state = self.state

        (r, c) = next_state.shape

        for i in range(r):
            for j in range(c):
                if next_state[i][j] < 0:
                    next_state[i][j] = 0
        

        rewards = np.zeros((100,11))
        #rewards
        v = np.sum(next_state, axis=0)
        h = np.sum(next_state, axis=1)
        d = 0
        if v[0] > PoMBS:
            for i in range(100):
                rewards[i][0] = rewards[i][0] - 0.1    
        else:
            d = d + 1 

        for t in range(1,11):
            if v[t] > PoSBS:
                for i in range(100):
                    rewards[i][t] = rewards[i][t] - 0.1    
            else:
                d = d+1

        for i in range(100):
            if h[i] < QoUE:
                for j in range(11):
                    rewards[i][j] = rewards[i][j] + 0.2
            
            else:
                d = d+1

        if d == 111:
            done = True
            print("Success")
        else: 
            done = False

        next_state = next_state.reshape(1,1100)
        rewards = rewards.reshape(1,1100)
        return rewards, next_state, done


