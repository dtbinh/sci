import logging

from core.ui import gui

logger = logging.getLogger()

class UI(gui.UI):

    def __init__(self, title, sma, delta=1, speed=25, lines=True):
        gui.UI.__init__(self, title, sma, delta, speed, lines)