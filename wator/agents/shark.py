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

class Shark(agent.Agent):

    def __init__(self, env, x, y, step, reproduction, starving):
        agent.Agent.__init__(self, env, x, y, step)
        self.reproduction = reproduction
        self.starving = starving
        self.timerdeath = 0
        self.timerbaby = 0
        self.color = 'black'

    def decide(self):
        acts = []

        if self.timerdeath == self.starving:
            acts.append(actions.Die(self))
            return acts

        neigh = self.neighbours()
        f = np.vectorize(canMove)
        print(neigh)
        weight = f(neigh)
        print(weight)
        move = np.any(np.equal(weight, 2)) or np.any(np.equal(weight, 1)) # can eat OR move on free spot

        if move:
            choices = np.where(np.equal(weight, 2))
            xchoices = choices[1]
            ychoices = choices[0]
            if xchoices.size == 0:
                choices = np.where(np.equal(weight, 1))
                xchoices = choices[1]
                ychoices = choices[0]
                choice = random.randint(0, len(xchoices)-1)
                x = xchoices[choice] - 1
                y = ychoices[choice] - 1
                acts.append(actions.Move(self, x, y))
            else:
                choice = random.randint(0, len(xchoices)-1)
                x = xchoices[choice] - 1
                y = ychoices[choice] - 1
                acts.append(actions.Kill(neigh[y+1, x+1]))
                acts.append(actions.Move(self, x, y))

            if self.timerbaby >= self.reproduction: # new born
                x = self.x
                y = self.y
                step = (random.randint(-1, 1), random.randint(-1, 1))
                shark = Shark(self.environment, x, y, step, self.reproduction)
                acts.append(actions.Born(shark))
                self.timerbaby = 0

        self.timerbaby += 1
        self.timerdeath += 1
        return acts

    def wall(self, x, y):
        self.step = (0,0)
        return -1

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

def canMove(spot):
    if spot != None:
        if spot.canBeEaten():
            return 2
        else:
            return 0
    else:
        return 1
