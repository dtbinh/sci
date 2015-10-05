'''
Created on 22 sept. 2015

@author: perard
'''
import logging

from core.agents import action

logger = logging.getLogger()

class Move(action.Action):

    def __init__(self, agent, x, y):
        action.Action.__init__(self, agent)
        self.x = x
        self.y = y
        
    def execute(self, sma, canvas, delta):
        acts = sma.environment.moveAgentOn(self.agent, self.agent.x + self.x, self.agent.y + self.y)
        shape = self.agent.shape
        if acts != -1:
            canvas.move(shape, self.x * delta, self.y * delta)
        else:
            acts = []
        return acts
        
class Born(action.Action):

    def __init__(self, agent):
        action.Action.__init__(self, agent)
        
    def execute(self, sma, canvas, delta):
        self.agent.addToSMA(sma)
        color = self.agent.color
        shape = canvas.create_rectangle(self.agent.x * delta, self.agent.y * delta, (self.agent.x * delta) + delta, (self.agent.y * delta) + delta, fill=color, outline=color)
        self.agent.shape = shape
        return []
        
class Die(action.Action):

    def __init__(self, agent):
        action.Action.__init__(self, agent)
        
    def execute(self, sma, canvas, delta):
        self.agent.removeFromSMA(sma)
        shape = self.agent.shape
        canvas.delete(shape)
        return []
        
class Kill(action.Action):

    def __init__(self, agent):
        action.Action.__init__(self, agent)
        
    def execute(self, sma, canvas, delta):
        self.agent.removeFromSMA(sma)
        shape = self.agent.shape
        canvas.delete(shape)
        return []