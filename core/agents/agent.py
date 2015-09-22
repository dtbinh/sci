import logging

logger = logging.getLogger()

MOVE = 'move'

class Agent(object):
    """
    Represent an individual agent in the simulation
    
    It is associated to an environment.
    It has a position (x,y) on the environment.
    And it has a direction (x,y) x,y may be {-1, 0, 1}.
    """

    def __init__(self, env, x, y, direction):
        self.environment = env
        self.x = x
        self.y = y
        self.direction = direction # step(x,y) i.e. step(1,0) -> move to the right

    def decide(self):
        """
        Decide what actions the agent has to take.
        It can return 0, 1 or more actions
        """
        pass

    def wall(self, x, y):
        """
        What append if the agent hit a wall of the environment
        """
        pass
    
    def meet(self, agent, x, y):
        """
        What append if the agent hit another agent
        """
        pass
    
    def addToSMA(self, sma):
        sma.addAgent(self)
        
    def removeFromSMA(self, sma):
        sma.removeAgent(self)
    
    def position(self):
        return (self.x, self.y)
    
    def moveOn(self, x, y):
        """
        Setter to change the position of the agent
        """
        self.x = x
        self.y = y
