import logging

import numpy as np
import random

from core.agents import agent

logger = logging.getLogger()

class Environment(object):

    def __init__(self, shape, sma):
        self.matrix = np.empty(shape, dtype=agent.Agent)
        self.sma = sma

    def __getitem__(self, key):
        x,y = key
        return self.matrix[y,x]

    def firstFreeSpot(self):
        n, m = self.shape()
        for x in range(m):
            for y in range(n):
                if not self.hasAgentOn(x, y):
                    return (x,y)
        return (-1, -1)

    def addAgent(self, agent, x, y):
        if not self.hasAgentOn(x, y):
            self.matrix[y,x] = agent
            agent.moveOn(x, y)
            return True
        return False

    def removeAgent(self, agent, x, y):
        self.matrix[y, x] = None

    def hasAgentOn(self, x, y):
        present = True if self.matrix[y,x] else False
        return present

    def neighboursOf(self, agent):
        n,m = self.shape()
        x = agent.x
        y = agent.y
        return self.matrix[max(y-1, 0):min(y+2, n), max(x-1, 0):min(x+2, m)]

    def moveAgentOn(self, agent, x, y):
        prev_x = agent.x
        prev_y = agent.y
        self.matrix[y,x] = agent
        self.matrix[prev_y, prev_x] = None
        action = agent.moveOn(x,y)

        return action

    def shape(self):
        return self.matrix.shape
