import pygame
from flappyGame.floor_module import Floor
from flappyGame.pipes_module import PipePair
from flappyGame.bird_module import Bird
from flappyGame.consts import PipeConsts


class Logic:
    """
          A class defining logic for the game.
          ----------------------------
          Methods
          ----------------------------
          check_collision(floor, pipe_pair, bird):
              Checks for collision between the bird object and the pipe/floor/sky.
          check_score(bird, pipe):
              Checks for if the bird had passed the pipe.
      """
    @staticmethod
    def check_collision(floor, pipe_pair, bird) -> bool:
        """
            Checks for collision between bird object and the pipe/floor/sky
               Parameters:
                   floor (Floor): Floor object
                   pipe_pair (PipePair): PipePair object
                   bird (Bird): Bird object
               :returns
               True if collision is detected
               False if collision is not detected

        """
        collision = False
        floor_pos = floor.y  # y position of the floor
        bird_butt = bird.y + bird.bird_image.get_height()  # bottom of the bird
        bird_mask = pygame.mask.from_surface(bird.bird_image)  # mask of bird
        bot_pipe_mask = pygame.mask.from_surface(pipe_pair.pipe_image[0])  # mask of bot pipe
        top_pipe_mask = pygame.mask.from_surface(pipe_pair.pipe_image[1])  # mask of top pipe

        top_pipe_offset = (round(pipe_pair.x - bird.x), round(pipe_pair.top_pipe_head - bird.y))  # integer offset
        bot_pipe_offset = (round(pipe_pair.x - bird.x), round(pipe_pair.bot_pipe_head - bird.y))  # integer offset

        pipe_collide_top = bird_mask.overlap(top_pipe_mask, top_pipe_offset)
        pipe_collide_bot = bird_mask.overlap(bot_pipe_mask, bot_pipe_offset)

        if pipe_collide_top is not None:  # collision with top pipe
            collision = True
        if pipe_collide_bot is not None:  # collision with bot pipe
            collision = True
        if bird_butt > floor_pos:  # collision with floor
            collision = True
        if bird.y < 0:  # collision with sky
            collision = True

        return collision

    @staticmethod
    def check_score(bird, closest_pipe) -> bool:
        """
            Checks if the bird had passed the pipe
               Parameters:
                   closest_pipe (PipePair): The closest pipe to the bird on the x axis
                   bird (Bird): the bird object of the game
               :returns
               True if bird had passed the pipe
               False if bird had not passed the pipe

        """
        bird_passed = False
        if bird.x > closest_pipe.x + PipeConsts.TOP_IMAGE.get_width():
            bird_passed = True

        return bird_passed



