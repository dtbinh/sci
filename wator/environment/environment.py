'''
Created on 22 sept. 2015

@author: perard
'''
import logging

from core.environment import environment

logger = logging.getLogger()

class Environment(environment.Environment):

    def __init__(self, shape, sma):
        environment.Environment.__init__(self, shape, sma)
