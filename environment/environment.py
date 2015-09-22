import logging

import numpy as np
import random

from agents import agent

logger = logging.getLogger()

class Environment(object):

    def __init__(self, shape):
        self.matrix = np.empty(shape, dtype=agent.Agent)

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

    def hasAgentOn(self, x, y):
        present = True if self.matrix[y,x] else False
        return present

    def moveAgentOn(self, agent, x, y):
        n, m = self.matrix.shape
        if x >= m or x < 0 or y >= n or y < 0:
            move = False
            agent.wall(x, y)
        elif not self.hasAgentOn(x, y):
            move = True
            prev_x = agent.x
            prev_y = agent.y
            self.matrix[y,x] = agent
            self.matrix[prev_y, prev_x] = None
            agent.moveOn(x,y)
        else: # other agent
            move = False
            other = self.matrix[y,x]
            agent.meet(other, x, y)

        return move

    def shape(self):
        return self.matrix.shape
