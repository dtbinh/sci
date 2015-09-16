import logging

import random

import environment
import agent

logger = logging.getLogger()

class SMA(object):

    def __init__(self, shape):
        self.environment = environment.Environment(shape)
        self.agents = []

    def addAgent(self, agent):
        self.environment.addAgent(agent, agent.x, agent.y)
        self.agents.append(agent)
