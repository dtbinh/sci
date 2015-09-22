import sys
import argparse
import logging

import random

from simulation import sma
from agents.balls import ball
from ui import gui

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--environment', '-env', help="Size of the environment", type=int, nargs=2, required=True)
    parser.add_argument('--balls', '-b', help="Number of balls", type=int, required=True)
    parser.add_argument('--size', '-s', help="Size of the balls", type=int, default=1)
    parser.add_argument('--speed', help="Fix the speed in ms", type=int, default=25)
    parser.add_argument('--debug', '-d', help="Activate the debug mode", action='store_true')
    parser.add_argument('--lines', '-l', help="Display a grid", choices=['true', 'false'], default='true')

    args = parser.parse_args()
    args.lines = True if args.lines == 'true' else False

    return args

def setUpLogging(debug=logging.INFO):
    formatter = logging.Formatter("%(asctime)s -- %(levelname)s -- %(message)s")

    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    handler.setLevel(debug)

    logger = logging.getLogger()
    logger.setLevel(debug)
    logger.addHandler(handler)

    return logger

if __name__ == '__main__':

    # args
    args = parse_arguments()
    env = tuple(args.environment)
    balls = args.balls
    size = args.size
    speed = args.speed
    lines = args.lines
    debug = logging.DEBUG if args.debug else logging.INFO

    # logger
    logger = setUpLogging(debug)

    sma = sma.SMA(env[::-1])
    environment = sma.environment
    for i in range(balls):
        x = random.randint(0, env[0]-1)
        y = random.randint(0, env[1]-1)
        step = (random.randint(-1, 1), random.randint(-1, 1))
        a = ball.Ball(environment, x, y, step)
        sma.addAgent(a)

    ui = gui.UI(sma, size, speed, lines)
    ui.run()
