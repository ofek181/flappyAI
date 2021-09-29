import pygame
import neat
import sys
from flappyGame import Bird, PipePair, Floor, Logic, consts
from game_animation import NeatDisplay
try:
    import cPickle as pickle  # pylint: disable=import-error
except ImportError:
    import pickle  # pylint: disable=import-error

global generation


class NeatAI:
    @staticmethod
    def eval_genomes(genomes, config):
        global generation
        generation += 1
        score = 0
        neural_networks = []
        birds = []
        genes = []
        floor = Floor()
        pipes = [PipePair(x_pos=500 + i * consts.PipeConsts.HORIZONTAL_GAP)
                 for i in range(10)]  # create 10 pipes
        closest_pipe = pipes[0]
        display = NeatDisplay()

        for genome_id, genome in genomes:
            genome.fitness = 0
            network = neat.nn.FeedForwardNetwork.create(genome, config)
            neural_networks.append(network)
            birds.append(Bird())
            genes.append(genome)

        while len(birds) > 0:
            display.animate_game(birds=birds, pipes=pipes, floor=floor)
            display.show_score(score=score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            # remove pipe if it moves out of screen and append another pipe to the list
            if pipes[0].x + consts.PipeConsts.TOP_IMAGE.get_width() < 0:
                pipes.pop(0)  # remove the passed pipe
                pipes.append(PipePair(pipes[-1].x + consts.PipeConsts.HORIZONTAL_GAP,
                                      velocity=pipes[-1].velocity))  # append another pipe

            if Logic.check_score(bird=birds[0], closest_pipe=closest_pipe):
                score += 1
                closest_pipe = pipes[1]

            for i, bird in enumerate(birds):
                genes[i].fitness += 0.1
                bird.move()
                delta_y = abs(bird.y - closest_pipe.bot_pipe_head)
                delta_x = abs(bird.x - closest_pipe.x)

                output = neural_networks[birds.index(bird)].activate((bird.velocity, delta_x, delta_y))
                if output[0] > 0.5:
                    bird.jump()

            for pipe in pipes:
                pipe.move()

            floor.move()

            for bird in birds:
                if Logic.check_collision(floor, closest_pipe, bird):
                    genes[birds.index(bird)].fitness -= 1
                    neural_networks.pop(birds.index(bird))
                    genes.pop(birds.index(bird))
                    birds.pop(birds.index(bird))

    @staticmethod
    def replay_genome(config_path, genome_path="winner.pkl"):
        global generation
        generation = 0
        # Load requried NEAT config
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                    neat.DefaultStagnation, config_path)

        # Unpickle saved winner
        with open(genome_path, "rb") as f:
            genome = pickle.load(f)

        # Convert loaded genome into required data structure
        genomes = [(1, genome)]

        # Call game with only the loaded genome
        NeatAI.eval_genomes(genomes, config)

    @staticmethod
    def run(config_file):
        global generation
        generation = 0
        """
            runs the NEAT algorithm to learn how to play flappy bird.
            :param config_file: location of config file
            :return: None
            """
        # Load configuration.
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                             neat.DefaultSpeciesSet, neat.DefaultStagnation,
                             config_file)

        # Create the population, which is the top-level object for a NEAT run.
        p = neat.Population(config)

        # Add a stdout reporter to show progress in the terminal.
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)

        # Run for up to 100 generations.
        winner = p.run(NeatAI.eval_genomes, 100)

        with open("winner.pkl", "wb") as f:
            pickle.dump(winner, f)
            f.close()

        # Display the winning genome.
        print('\nBest genome:\n{!s}'.format(winner))


