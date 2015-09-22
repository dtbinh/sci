import logging

import numpy as np
import random

from core.agents import agent

logger = logging.getLogger()

class Environment(object):

    def __init__(self, shape, sma):
        self.matrix = np.empty(shape, dtype=agent.Agent)
        self.sma = sma

    def addAgent(self, agent, x, y):
        n, m = self.matrix.shape
        if x >= m or x < 0 or y >= n or y < 0:
            new_x = random.randint(0, m-1)
            new_y = random.randint(0, n-1)
            self.addAgent(agent, new_x, new_y)
        elif self.hasAgentOn(x, y):
            new_x = random.randint(0, m-1)
            new_y = random.randint(0, n-1)
            self.addAgent(agent, new_x, new_y)
        else: # free spot
            self.matrix[y,x] = agent
            agent.moveOn(x,y)
        
    def removeAgent(self, agent, x, y):
        self.matrix[y, x] = None

    def hasAgentOn(self, x, y):
        present = True if self.matrix[y,x] else False
        return present

    def moveAgentOn(self, agent, x, y):
        n, m = self.matrix.shape
        if x >= m or x < 0 or y >= n or y < 0: # wall
            action = agent.wall(x, y)
        elif not self.hasAgentOn(x, y): # free spot
            prev_x = agent.x
            prev_y = agent.y
            self.matrix[y,x] = agent
            self.matrix[prev_y, prev_x] = None
            action = agent.moveOn(x,y)
        else: # other agent
            other = self.matrix[y,x]
            action = agent.meet(other, x, y)

        return action

    def shape(self):
        return self.matrix.shape
