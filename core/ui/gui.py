import logging

import random

from tkinter import *

logger = logging.getLogger()

class UI(object):

    def __init__(self, title, sma, delta=1, speed=25, lines=True):
        self.sma = sma
        self.delta = delta
        self.speed = speed
        self.windows = Tk()
        self.windows.title(title)
        width = (sma.environment.shape()[1] * delta) + 100
        height = (sma.environment.shape()[0] * delta) + 100
        self.canvas = Canvas(self.windows, width=width, height=height, background='white')

        self.canvas.pack()
        self.button = Button(self.windows, text="Live ON!", command=self.live)
        self.button.pack()
        
        for agent in sma.agents:
            color = agent.color
            shape = self.canvas.create_rectangle(agent.x * delta, agent.y * delta, (agent.x * delta) + delta, (agent.y * delta) + delta, fill=color, outline=color)
            agent.shape = shape
        
        if lines and delta > 2:
            self.build_lines()
    
    def build_lines(self):
        sma = self.sma
        delta = self.delta
        for i in range(0, sma.environment.shape()[1] * delta, delta):
            self.canvas.create_line(i, 0, i, sma.environment.shape()[0] * delta, fill='lightgray')
        
        for j in range(0, sma.environment.shape()[0] * delta, delta):
            self.canvas.create_line(0, j, sma.environment.shape()[1] * delta, j, fill='lightgray')

    def run(self):
        self.windows.mainloop()
        
    def stop(self):
        return False

    def live(self):
        while not self.stop():
            random.shuffle(self.sma.agents)
            for agent in self.sma.agents:
                actions = agent.decide()
                
                for action in actions:
                    suppactions = action.execute(self.sma, self.canvas, self.delta)
                    for suppaction in suppactions:
                        suppaction.execute(self.sma, self.canvas, self.delta)
            
            self.canvas.update()
            self.windows.after(self.speed)