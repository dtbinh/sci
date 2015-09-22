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
        
    def execute(self, sma, canvas, shapes, delta):
        sma.environment.moveAgentOn(self.agent, self.agent.x + self.x, self.agent.y + self.y)
        shape = shapes[self.agent]
        canvas.move(shape, self.x * delta, self.y * delta)
        
class Born(action.Action):

    def __init__(self):
        action.Action.__init__(self)
        
    def execute(self, sma, agent, canvas, shapes, delta):
        color = agent.color
        shape = canvas.create_rectangle(agent.x * delta, agent.y * delta, (agent.x * delta) + delta, (agent.y * delta) + delta, fill=color, outline=color)
        self.shapes[agent] = shape
        agent.addToSMA(sma)
        
class Die(action.Action):

    def __init__(self):
        action.Action.__init__(self)
        
    def execute(self, sma, agent, canvas, shapes, delta):
        shape = shapes[agent]
        self.canvas.delete(shape)
        del self.shapes[agent]
        agent.removeFromSMA(sma)
        
class Kill(action.Action):

    def __init__(self):
        action.Action.__init__(self)
        
    def execute(self, sma, agent, canvas, shapes, delta):
        shape = shapes[agent]
        self.canvas.delete(shape)
        del self.shapes[agent]
        agent.removeFromSMA(sma)