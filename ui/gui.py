import logging

import time
import random

from tkinter import *

logger = logging.getLogger()

class UI(object):

    def __init__(self, sma, delta=1, speed=25):
        self.sma = sma
        self.delta = delta
        self.speed = speed
        self.windows = Tk()
        self.windows.title("Life of balls")
        self.canvas = Canvas(self.windows, width=sma.environment.shape()[1]*delta, height=sma.environment.shape()[0]*delta, background='white')
        self.rectangle = dict()

        for agent in sma.agents:
            color = agent.fillcolor
            rect = self.canvas.create_rectangle(agent.x*delta, agent.y*delta, (agent.x*delta) + delta, (agent.y*delta) + delta, fill=color, outline=color)
            self.rectangle[agent] = rect

        self.canvas.pack()
        self.button = Button(self.windows, text="Live ON!", command=self.live)
        self.button.pack()

    def run(self):
        self.windows.mainloop()

    def live(self):
        delta = self.delta
        while (True):
            random.shuffle(self.sma.agents)
            for agent in self.sma.agents:
                move = agent.decide()
                if move:
                    rect = self.rectangle[agent]
                    self.canvas.move(rect, agent.step[0] * delta, agent.step[1] * delta)
            self.canvas.update()
            self.windows.after(self.speed)
