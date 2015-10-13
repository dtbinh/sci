import logging

from core.environment import environment

logger = logging.getLogger()

class SMA(object):

    def __init__(self, shape):
        self.environment = environment.Environment(shape, self)
        self.agents = []

    def addAgent(self, agent):
        placed = self.environment.addAgent(agent, agent.x, agent.y)
        if not placed:
            x, y = self.environment.firstFreeSpot()
            self.environment.addAgent(agent, x, y)
        self.agents.append(agent)

    def removeAgent(self, agent):
        self.environment.removeAgent(agent, agent.x, agent.y)
        self.agents.remove(agent)
