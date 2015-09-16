import logging

import time
import random

from tkinter import *

logger = logging.getLogger()

class UI(object):

    def __init__(self, sma):
        self.sma = sma
        self.windows = Tk()
        self.windows.title("Life of balls")
        self.canvas = Canvas(self.windows, width=sma.environment.shape()[1], height=sma.environment.shape()[0], background='white')
        self.rectangle = dict()

        for agent in sma.agents:
            r = random.randint(0, 2)
            delta = agent.size
            if r == 0:
                color = "red"
            elif r == 1:
                color = "blue"
            else:
                color = "green"
            rect = self.canvas.create_oval(agent.x, agent.y, agent.x+delta, agent.y+delta, fill=color, outline=color)
            self.rectangle[agent] = rect

        self.canvas.pack()
        self.button = Button(self.windows, text="Live ON!", command=self.live)
        self.button.pack()

    def run(self):
        self.windows.mainloop()

    def live(self):
        n = 0
        while (True):
            random.shuffle(self.sma.agents)
            for agent in self.sma.agents:
                delta = agent.size
                move = agent.decide()
                rect = self.rectangle[agent]
                if move:
                    self.canvas.move(rect, agent.step[0] * delta, agent.step[1] * delta)
            n += 1
            self.canvas.update()
            self.windows.after(50)
