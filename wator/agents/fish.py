'''
Created on 22 sept. 2015

@author: perard
'''
import logging

import numpy as np
import random

import wator.agents.actions as actions
from core.agents import agent

logger = logging.getLogger()

class Fish(agent.Agent):

    def __init__(self, env, x, y, step, reproduction):
        agent.Agent.__init__(self, env, x, y, step)
        self.reproduction = reproduction
        self.timerbaby = 0
        self.color = 'blue'

    def decide(self):
        acts = []
        neigh = self.neighbours()
        canMove = np.any(np.equal(neigh, None))

        if canMove:
            choices = np.where(np.equal(neigh, None))
            xchoices = choices[1]
            ychoices = choices[0]
            choice = random.randint(0, len(xchoices)-1)
            x = xchoices[choice] - 1
            y = ychoices[choice] - 1
            acts.append(actions.Move(self, x, y))

            if self.timerbaby >= self.reproduction: # new born
                x = self.x
                y = self.y
                step = (random.randint(-1, 1), random.randint(-1, 1))
                fish = Fish(self.environment, x, y, step, self.reproduction)
                acts.append(actions.Born(fish))
                self.timerbaby = 0

        self.timerbaby += 1
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
