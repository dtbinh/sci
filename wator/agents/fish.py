'''
Created on 22 sept. 2015

@author: perard
'''
import logging

import random

import wator.agents.actions as actions
from core.agents import agent

logger = logging.getLogger()

class Fish(agent.Agent):

    def __init__(self, env, x, y, step, reproduction, vision=1):
        agent.Agent.__init__(self, env, x, y, step)
        self.reproduction = reproduction
        self.timer = 0
        self.color = 'blue'
        self.vision = vision
        
    def decide(self):
        acts = []
        neigh = self.neighbours()
        
        if self.timer == self.reproduction: # new born
            if len(neigh) != 8:
                x = self.x
                y = self.y
                step = (random.randint(-1, 1), random.randint(-1, 1))
                shark = Fish(self.environment, x, y, step, self.reproduction)
                acts.append(actions.Born(shark))
                self.timer = 0
        else:
            self.timer += 1
        
        x = 0
        y = 0
        if len(self.neighbours()) != 8:
            while x == 0 and y == 0:
                x = random.randint(-1, 1)
                y = random.randint(-1, 1)
        
        acts.append(actions.Move(self, x, y))
            
        return acts
        
    def wall(self, x, y):
        self.step = (0,0)
        return -1
    
    def meet(self, agent, x, y):
        self.step = (0,0)
        return []
    
    def addToSMA(self, sma):
        sma.addFish(self)
        
    def removeFromSMA(self, sma):
        sma.removeFish(self)
    
    def canBeEaten(self):
        return True