import sys
import argparse
import logging

import random

import sma
import agent
import ui

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--environment', '-env', help="Size of the environment", type=int, nargs=2, required=True)
    parser.add_argument('--balls', '-b', help="Number of balls", type=int, required=True)
    parser.add_argument('--size', '-s', help="Size of the balls", type=int)
    parser.add_argument('--debug', '-d', help="Activate the debug mode", action='store_true')

    args = parser.parse_args()

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
    debug = logging.DEBUG if args.debug else logging.INFO

    # logger
    logger = setUpLogging(debug)

    sma = sma.SMA(env)
    environment = sma.environment
    for i in range(balls):
        x = random.randint(0, env[0]-1)
        y = random.randint(0, env[1]-1)
        step = (random.randint(-1, 1), random.randint(-1, 1))
        a = agent.Agent(environment, x, y, step, size)
        sma.addAgent(a)

    ui = ui.UI(sma)
    ui.run()
