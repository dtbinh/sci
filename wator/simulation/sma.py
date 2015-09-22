import logging

from core.simulation import sma

logger = logging.getLogger()

class SMA(sma.SMA):

    def __init__(self, shape):
        sma.SMA.__init__(self, shape)
        self.fishs = []
        self.sharks = []
        
    def addFish(self, fish):
        self.addAgent(fish)
        self.fishs.append(fish)
        
    def removeFish(self, fish):
        self.removeAgent(fish)
        self.fishs.remove(fish)
        
    def addShark(self, shark):
        self.addAgent(shark)
        self.sharks.append(shark)
        
    def removeShark(self, shark):
        self.removeAgent(shark)
        self.sharks.remove(shark)