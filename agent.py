import logging

import random

logger = logging.getLogger()

class Agent(object):

    def __init__(self, env, x, y, step, size):
        self.environment = env
        self.x = x
        self.y = y
        self.step = step # step(x,y) i.e. step(1,0) -> move to the right
        self.size = size if size else 5

    def decide(self):
        move = False if (random.randint(0, 9) == 1) else True
        turn = True if (random.randint(0, 19) == 1) else False

        if not move:
            return move

        #if turn:
        #    self.step = (random.randint(-1, 1), random.randint(-1,1))

        move = self.environment.moveAgentOn(self, self.x + (self.step[0] * self.size), self.y + (self.step[1] * self.size))
        return move

    def moveOn(self, x, y):
        self.x = x
        self.y = y

    def wall(self, x, y):
        step_x = self.step[0]
        step_y = self.step[1]
        if step_x == 0 or step_y == 0:
            step_x, step_y = -step_x, -step_y
        else:
            n, m = self.environment.matrix.shape
            delta = self.size
            if x+delta >= n or x <= 0:
                step_x = -step_x
            if y+delta >= m or y <= 0:
                step_y = -step_y
        self.step = (step_x, step_y)

    def reverse(self):
        self.step = self.oppositeOf(self.step)

    def oppositeOf(self, step):
        x = step[0]
        y = step[1]
        return (self.turn(x), self.turn(y))

    def turn(self, pos):
        return -pos
