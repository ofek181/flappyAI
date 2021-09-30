import os
from .neat_algorithm import NeatAI


def start_neat():
    """
        Determine path to configuration file. This path manipulation is
        here so that the script will run successfully regardless of the
        current working directory.
    """
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    NeatAI.train(config_path)  # train

    # NeatAI.test(config_path)  # test

