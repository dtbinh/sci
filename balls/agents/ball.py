'''
Created on 22 sept. 2015

@author: perard
'''
import logging

import random

from agents import agent

logger = logging.getLogger()

class Ball(agent.Agent):

    def __init__(self, env, x, y, step):
        agent.Agent.__init__(self, env, x, y, step)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        self.fillcolor = '#%02x%02x%02x' % (r, g, b)
        
    def decide(self):
        move = False if (random.randint(0, 9) == 1) else True
        turn = True if (random.randint(0, 19) == 1) else False

        if not move:
            return move

        #if turn:
        #    self.step = (random.randint(-1, 1), random.randint(-1,1))

        move = self.environment.moveAgentOn(self, self.x + self.step[0], self.y + self.step[1])
        return move
    
    def wall(self, x, y):
        step_x = self.step[0]
        step_y = self.step[1]
        if step_x == 0 or step_y == 0:
            step_x, step_y = -step_x, -step_y
        else:
            n, m = self.environment.matrix.shape
            if x >= m or x <= 0:
                step_x = -step_x
            if y >= n or y <= 0:
                step_y = -step_y
        self.step = (step_x, step_y)
        
    def meet(self, agent, x, y):
        self.reverse()
        
    def reverse(self):
        x = self.step[0]
        y = self.step[1]
        self.step = (-x, -y)