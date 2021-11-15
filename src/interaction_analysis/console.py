import os
from configparser import ConfigParser

from interaction_analysis import InteractionAnalysis

cfg = ConfigParser()
cfg.read(os.path.realpath(os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    os.pardir,
    'config.cfg')))
