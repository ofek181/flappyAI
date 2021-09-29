import os
from neat_algorithm import NeatAI


def main():
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward')
    NeatAI.run(config_path)


if __name__ == '__main__':
    main()
