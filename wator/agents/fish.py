'''
Created on 22 sept. 2015

@author: perard
'''
import logging

import random

from core.agents import agent
import wator.agents.actions as actions

logger = logging.getLogger()

class Fish(agent.Agent):

    def __init__(self, env, x, y, step, reproduction, vision=1):
        agent.Agent.__init__(self, env, x, y, step)
        self.reproduction = reproduction
        self.timer = 0
        self.color = 'blue'
        self.vision = vision
        
    def decide(self):
        actions = []
        n,m = self.environment.shape()
        if self.timer == self.reproduction: # new born
            x = random.randint(0, m-1)
            y = random.randint(0, n-1)
            step = (random.randint(-1, 1), random.randint(-1, 1))
            fish = Fish(self.environment, x, y, step, self.reproduction)
            actions.append(actions.Born(fish))
            self.timer = 0
        else:
            self.timer += 1
        
        choices = []
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                dir_x = (self.x + i) % m
                dir_y = (self.y + j) % n
                if not self.environment.hasAgentOn(dir_x, dir_y):
                    choices.append((i, j))
        
        try:
            x,y = random.choice(choices)
        except IndexError:
            pass
        
        actions.append(actions.Move(self, x, y))
            
        return actions
        
    def wall(self, x, y):
        return False
    
    def meet(self, agent, x, y):
        return False
    
    def canBeEaten(self):
        return True