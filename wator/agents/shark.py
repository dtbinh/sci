'''
Created on 22 sept. 2015

@author: perard
'''
import logging

import random

from agents import agent
from agents.agent import MOVE

logger = logging.getLogger()

BORN = 'born'
DIE = 'die'

class Shark(agent.Agent):
    
    def __init__(self, env, x, y, step, starving, vision=1):
        agent.Agent.__init__(self, env, x, y, step)
        self.starving = starving
        self.timer = 0
        self.color = 'black'
        self.vision = vision
        
    def decide(self):
        actions = []
        n,m = self.environment.shape()
        if self.timer == self.starving:
            sma = self.environment.sma.removeAgent(self)
            actions.append((DIE, self))
            return actions
        else:
            self.timer += 1
        
        choices = []
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                dir_x = (self.x + i) % m
                dir_y = (self.y + j) % n
                if not self.environment.hasAgentOn(dir_x, dir_y):
                    choices.append((dir_x, dir_y))
        
        try:
            x,y = random.choice(choices)
        except IndexError:
            return actions
        
        if self.environment.moveAgentOn(self, x, y):
            actions.append((MOVE, self))
            
        return actions
        
    def wall(self, x, y):
        pass
    
    def meet(self, agent, x, y):
        if agent.canBeEaten():
            sma = self.environment.sma.removeAgent(self)
            sma.kill(agent)
            return True
        return False
    
    def canBeEaten(self):
        return False