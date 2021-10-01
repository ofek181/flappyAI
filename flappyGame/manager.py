import pygame
import sys
from flappyGame.bird_module import Bird
from flappyGame.floor_module import Floor
from flappyGame.pipes_module import PipePair
from flappyGame.display_module import Display
from flappyGame.logic_module import Logic
import flappyGame.consts as consts


class Game:
    """
         Implements the main loop of the game.
         ----------------------------
         Attributes
         ----------------------------
         bird :
             the bird object of the game.
         floor :
             the floor of the game.
         pipes :
             a list of all the pipe pairs.
         closest pipe :
             the closest pipe to the bird on the x axis.
         display :
             the display of the game.
         BACKGROUND_SOUND :
             background music for the game.
         GAME_OVER_SOUND:
             game over music.
         SCORE_SOUND:
             scoring sound when bird passes a pipe.
         channel1:
             first channel that plays background and game over sounds.
         channel2:
             second channel that plays the scoring sound so that it doesn't override the background music.

         ----------------------------
         Methods
         ----------------------------
         __init__(self):
             Constructs all the necessary attributes for the Game class.
         calc_frame(self):
             Calculates a single frame of the game.
         run_game(self):
             Implements the main loop of the game.
         game_over(self):
             Handles the game over scheme.
    """
    def __init__(self):
        """
           Constructs all the necessary attributes for the Game object.
        """
        self.bird = Bird()  # create bird
        self.floor = Floor()  # create floor
        self.pipes = [PipePair(x_pos=500 + i * consts.PipeConsts.HORIZONTAL_GAP)
                      for i in range(10)]  # create 10 pipes
        self.closest_pipe = self.pipes[0]
        self.display = Display()  # create the display
        self.display.show_score(bird=self.bird)  # show the 0 score

        # sound attributes
        pygame.mixer.init()
        # pygame.mixer.set_num_channels(2)
        self.BACKGROUND_SOUND = pygame.mixer.Sound(consts.AudioConsts.BACKGROUND_AUDIO)
        self.GAME_OVER_SOUND = pygame.mixer.Sound(consts.AudioConsts.GAME_OVER_AUDIO)
        self.SCORE_SOUND = pygame.mixer.Sound(consts.AudioConsts.SCORE_AUDIO)
        pygame.mixer.Sound.set_volume(self.BACKGROUND_SOUND, 0.5)
        self.channel1 = pygame.mixer.Channel(0)
        self.channel2 = pygame.mixer.Channel(1)

    def calc_frame(self):
        """
            Calculates a single frame of the game
        """
        # move bird floor and pipes
        self.bird.move()
        self.floor.move()
        for pipe in self.pipes:
            pipe.move()

        # remove pipe if it moves out of screen and append another pipe to the list
        if self.pipes[0].x + consts.PipeConsts.TOP_IMAGE.get_width() < 0:
            self.pipes.pop(0)  # remove the passed pipe
            self.pipes.append(PipePair(self.pipes[-1].x + consts.PipeConsts.HORIZONTAL_GAP,
                                       velocity=self.pipes[-1].velocity))  # append another pipe

        # check for collisions
        if Logic.check_collision(bird=self.bird, pipe_pair=self.pipes[0], floor=self.floor):
            self.channel1.play(self.GAME_OVER_SOUND)
            self.game_over()
        else:
            self.display.show_score(bird=self.bird)

        # check for score
        if Logic.check_score(bird=self.bird, closest_pipe=self.closest_pipe):
            self.channel2.play(self.SCORE_SOUND)
            self.bird.score += 1
            self.closest_pipe = self.pipes[1]  # because the don't delete the pipe until it moved out of screen

    def run_game(self):
        """
            Implements the while loop running the game
        """
        # background audio initialization
        self.channel1.play(self.BACKGROUND_SOUND, loops=-1)

        while True:
            self.display.animate_game(bird=self.bird, pipe_pairs=self.pipes, floor=self.floor)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))
                    else:
                        self.bird.jump()

            self.calc_frame()

    def game_over(self):
        """
            Handles the game over scheme.
            Restarts the game or exits depending on the action of the user.
        """
        while True:
            self.display.show_game_over()
            self.display.animate_game(self.bird, self.pipes, self.floor)

            # animate bird falling
            if self.bird.y + self.bird.bird_image.get_height() <= self.floor.y:
                self.bird.move()

            # restart the game or exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))
                    # restart is allowed when bird touches the ground
                    elif self.bird.y > self.floor.y - self.floor.floor_image[0].get_height():
                        self.__init__()
                        self.run_game()

