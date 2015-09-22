import logging

import random

logger = logging.getLogger()

class Agent(object):

    def __init__(self, env, x, y, step):
        self.environment = env
        self.x = x
        self.y = y
        self.step = step # step(x,y) i.e. step(1,0) -> move to the right

    def decide(self):
        pass

    def wall(self, x, y):
        pass
    
    def meet(self, agent, x, y):
        pass
    
    def moveOn(self, x, y):
        self.x = x
        self.y = y

    def reverse(self):
        x = self.step[0]
        y = self.step[1]
        self.step = (-x, -y)
