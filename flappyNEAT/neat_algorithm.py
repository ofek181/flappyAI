import pygame
import neat
import sys
import pickle

import flappyGame
from flappyGame import Bird, PipePair, Floor, Logic, Game, consts
from .game_animation import NeatDisplay
global generation


class NeatAI:
    """
        A class implementing the NEAT algorithm on flappyGame.
        ----------------------------
        Methods
        ----------------------------
        eval_genomes(genomes, config):
            Evaluates all genome of birds by pre defined fitness.
        test(config_path, genome_path):
            Loads the winner network and runs the flappy bird game.
        train(config_file):
            Runs the NEAT algorithm to learn how to play flappy bird.

    """
    @staticmethod
    def eval_genomes(genomes, config):
        """
            Evaluates all genome of birds by pre defined fitness.
            :param
                 genomes: each genome includes a list of connection genes.
                 config: the NEAT config file.
            :return:
                None
        """
        # initialize parameters
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
        next_pipe = pipes[1]
        display = NeatDisplay()
        for genome_id, genome in genomes:
            genome.fitness = 0
            network = neat.nn.FeedForwardNetwork.create(genome, config)
            neural_networks.append(network)
            birds.append(Bird())
            genes.append(genome)

        # game loop for each generation
        while len(birds) > 0:
            # game display and event handling
            display.animate_game(birds=birds, pipes=pipes, floor=floor)
            display.show_score_and_birds_alive(score=score, birds=birds)
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

            # check score of bird[0] which is the last to be alive
            if Logic.check_score(bird=birds[0], closest_pipe=closest_pipe):
                score += 1
                closest_pipe = pipes[1]
                next_pipe = pipes[2]

            # run over all birds and move them as well as calculate distances to closest pipe.
            for i, bird in enumerate(birds):
                genes[i].fitness += 0.1
                bird.move()
                delta_y_closest = abs(bird.y - closest_pipe.bot_pipe_head)
                delta_x_closest = abs(bird.x - closest_pipe.x)
                delta_y_next = abs(bird.y- next_pipe.bot_pipe_head)
                delta_x_next = abs(bird.x - next_pipe.x)

                # run the neural network with following inputs:
                # velocity of bird, velocity of closest pipe, x axis distance and y axis distance for next 2 pipes
                output = neural_networks[birds.index(bird)].activate((bird.velocity, closest_pipe.velocity,
                                                                      delta_x_closest, delta_y_closest,
                                                                      delta_x_next, delta_y_next))
                # jump if output neuron returns value over 0.5
                if output[0] > 0.5:
                    bird.jump()

            # move all pipes
            for pipe in pipes:
                pipe.move()

            # move the floor
            floor.move()

            # pop bird if it collides
            for i, bird in enumerate(birds):
                if Logic.check_collision(floor, closest_pipe, bird):
                    genes[i].fitness -= 2
                    neural_networks.pop(i)
                    genes.pop(i)
                    birds.pop(i)

    @staticmethod
    def test(config_path, genome_path="flappyNEAT/winner.pkl"):
        """
            Loads the winner network and runs the flappy bird game
            :param
                config_file: location of config file.
                genome_path: winner network.
            :return:
                None
            """
        # Load NEAT config
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                    neat.DefaultStagnation, config_path)

        # Unpickle saved winner
        with open(genome_path, "rb") as f:
            genome = pickle.load(f)

        # audio parameters
        pygame.mixer.init()
        background_sound = pygame.mixer.Sound(consts.AudioConsts.BACKGROUND_AUDIO)
        game_over_sound = pygame.mixer.Sound(consts.AudioConsts.GAME_OVER_AUDIO)
        score_sound = pygame.mixer.Sound(consts.AudioConsts.SCORE_AUDIO)
        pygame.mixer.Sound.set_volume(background_sound, 0.5)
        channel1 = pygame.mixer.Channel(0)
        channel2 = pygame.mixer.Channel(1)

        # initialization
        bird = Bird()
        floor = Floor()
        pipes = [PipePair(x_pos=500 + i * consts.PipeConsts.HORIZONTAL_GAP)
                 for i in range(10)]  # create 10 pipes
        closest_pipe = pipes[0]
        next_pipe = pipes[1]
        display = flappyGame.Display()
        game_over_manager = Game()
        neural_network = neat.nn.FeedForwardNetwork.create(genome, config)

        channel1.play(background_sound, loops=-1)
        while True:
            # game display and event handling
            display.animate_game(bird=bird,pipe_pairs=pipes,floor=floor)
            display.show_score(bird=bird)
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

            # check score of bird
            if Logic.check_score(bird=bird, closest_pipe=closest_pipe):
                channel2.play(score_sound)
                bird.score += 1
                closest_pipe = pipes[1]
                next_pipe = pipes[2]

            bird.move()
            delta_y_closest = abs(bird.y - closest_pipe.bot_pipe_head)
            delta_x_closest = abs(bird.x - closest_pipe.x)
            delta_y_next = abs(bird.y - next_pipe.bot_pipe_head)
            delta_x_next = abs(bird.x - next_pipe.x)

            output = neural_network.activate((bird.velocity, closest_pipe.velocity,
                                              delta_x_closest, delta_y_closest,
                                              delta_x_next, delta_y_next))

            # jump if output neuron returns value over 0.5
            if output[0] > 0.5:
                bird.jump()

            # move all pipes
            for pipe in pipes:
                pipe.move()

            # move the floor
            floor.move()

            if Logic.check_collision(floor, closest_pipe, bird):
                channel1.play(game_over_sound)
                while True:
                    display.show_game_over()
                    display.animate_game(bird, pipes, floor)
                    # animate bird falling
                    if bird.y + bird.bird_image.get_height() <= floor.y:
                        bird.move()

                    # exit the game
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pygame.event.post(pygame.event.Event(pygame.QUIT))

    @staticmethod
    def train(config_file):
        """
            Runs the NEAT algorithm to learn how to play flappy bird.
            :param
                config_file: location of config file
            :return:
                saves the defined winner in a pkl file
            """
        global generation
        generation = 0
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

        with open("flappyNEAT/winner.pkl", "wb") as f:
            pickle.dump(winner, f)
            f.close()

        # Display the winning genome.
        print('\nBest genome:\n{!s}'.format(winner))


