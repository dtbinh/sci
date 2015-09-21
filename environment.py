import logging

import numpy as np
import random

import agent

logger = logging.getLogger()

class Environment(object):

    def __init__(self, shape):
        self.matrix = np.empty(shape, dtype=agent.Agent)

    def __getitem__(self, key):
        return self.matrix[key]

    def addAgent(self, agent, x, y):
        delta = agent.size
        m, n = self.matrix.shape
        if x+delta >= n or x <= 0 or y+delta >= m or y <= 0:
            new_x = x + (random.randint(-1, 1) * delta)
            new_y = y + (random.randint(-1, 1) * delta)
            self.addAgent(agent, new_x, new_y)
        elif (np.all(np.equal(self.matrix[x:x+delta,y:y+delta], None))):
            self.matrix[x:x+delta,y:y+delta] = agent
            agent.moveOn(x,y)
        else:
            new_x = x + random.randint(-1, 1)
            new_y = y + random.randint(-1, 1)
            self.addAgent(agent, new_x, new_y)

    def hasAgentOn(self, x, y):
        present = True if self.matrix[x,y] else False

    def moveAgentOn(self, agent, x, y):
        delta = agent.size
        m, n = self.matrix.shape
        if x+delta >= n or x <= 0 or y+delta >= m or y <= 0:
            move = False
            agent.wall(x, y)
        elif (np.all(np.equal(self.matrix[x:x+delta,y:y+delta], None))):
            move = True
            prev_x = agent.x
            prev_y = agent.y
            self.matrix[x:x+delta,y:y+delta] = agent
            self.matrix[prev_x:prev_x+delta, prev_y:prev_y+delta] = None
            agent.moveOn(x,y)
        else:
            move = False
            agent.reverse()

        return move

    def shape(self):
        return self.matrix.shape
