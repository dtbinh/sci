'''
Created on 22 sept. 2015

@author: perard
'''
import logging

import random

import wator.agents.actions as actions
from core.agents import agent

logger = logging.getLogger()

class Shark(agent.Agent):
    
    def __init__(self, env, x, y, step, reproduction, starving, vision=1):
        agent.Agent.__init__(self, env, x, y, step)
        self.reproduction = reproduction
        self.starving = starving
        self.timerdeath = 0
        self.timerbaby = 0
        self.color = 'black'
        self.vision = vision
        
    def decide(self):
        acts = []
        n,m = self.environment.shape()
        if self.timerdeath == self.starving:
            acts.append(actions.Die(self))
            return acts
        elif self.timerbaby == self.reproduction: # new born
            x = random.randint(0, m-1)
            y = random.randint(0, n-1)
            step = (random.randint(-1, 1), random.randint(-1, 1))
            fish = Shark(self.environment, x, y, step, self.reproduction, self.starving)
            acts.append(actions.Born(fish))
            self.timerdeath += 1
            self.timerbaby = 0
        else:
            self.timerdeath += 1
            self.timerbaby += 1

        x = random.randint(-1, 1)
        y = random.randint(-1, 1)
        
        acts.append(actions.Move(self, x, y))
            
        return acts
        
    def wall(self, x, y):
        self.step = (0,0)
        return []
    
    def meet(self, agent, x, y):
        if agent.canBeEaten():
            self.timerdeath = 0
            return [actions.Kill(agent)]
        return []
    
    def addToSMA(self, sma):
        sma.addShark(self)
        
    def removeFromSMA(self, sma):
        sma.removeShark(self)
    
    def canBeEaten(self):
        return False