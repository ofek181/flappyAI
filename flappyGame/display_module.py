import pygame
from flappyGame.consts import DisplayConsts, AudioConsts


class Display:
    """
             A class to implement the display of the game.
             ----------------------------
             Attributes
             ----------------------------
             screen : pygame object
                 an attribute to represent the screen of the game.
             ----------------------------
             Methods
             ----------------------------
             __init__(self):
                 Constructs all the necessary attributes for the Display object.
             show_game_over(self):
                 Displays the game over screen
             show_score(self, bird):
                 Displays the score of the bird
             animate_game(self, bird, pipe_pairs, floor):
                 Uses pygame methods in order to display the game on the screen.
    """
    def __init__(self):
        """
            Constructs all the necessary attributes for the Display object.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((DisplayConsts.SCREEN_HEIGHT, DisplayConsts.SCREEN_HEIGHT))

    def show_game_over(self):
        """
            Displays the game over screen
        """
        font = pygame.font.SysFont(DisplayConsts.GAME_OVER_FONT_TYPE, DisplayConsts.GAME_OVER_FONT_SIZE)
        surface = font.render("Game Over", True, DisplayConsts.GAME_OVER_FONT_COLOR)  # Display game over
        rect = surface.get_rect()
        rect.midtop = (DisplayConsts.SCREEN_WIDTH // 2.5, DisplayConsts.SCREEN_HEIGHT // 20)
        self.screen.blit(surface, rect)
        pygame.display.update()  # update the screen

    def show_score(self, bird):
        """
            Displays the score over the screen
        """
        font = pygame.font.SysFont(DisplayConsts.FONT_TYPE, DisplayConsts.FONT_SIZE)
        surface = font.render(str(bird.score), True, DisplayConsts.FONT_COLOR)  # show score
        rect = surface.get_rect()
        rect.midtop = (DisplayConsts.SCREEN_WIDTH // 2.5, DisplayConsts.SCREEN_HEIGHT // 20)
        self.screen.blit(surface, rect)
        pygame.display.update()  # update the screen

    def animate_game(self, bird, pipe_pairs, floor):
        """
            Implements the game animation on the screen attribute.
                Parameters:
                    bird : bird object that will be drawn.
                    pipe_pairs: list of pipes to be drawn.
                    floor: floor of the game to be drawn.

        """
        self.screen.blit(DisplayConsts.BACKGROUND_IMAGE, (0, 0))  # draw background

        self.screen.blit(floor.floor_image[0], (floor.x[0], floor.y))  # draw the first floor
        self.screen.blit(floor.floor_image[1], (floor.x[1], floor.y))  # draw the second floor
        self.screen.blit(floor.floor_image[2], (floor.x[2], floor.y))  # draw the third floor

        for pipe_pair in pipe_pairs:  # draw the pipes
            self.screen.blit(pipe_pair.pipe_image[1], (pipe_pair.x, pipe_pair.top_pipe_head))
            self.screen.blit(pipe_pair.pipe_image[0], (pipe_pair.x, pipe_pair.bot_pipe_head))

        rotated_image, rotated_rect = bird.animate()  # animate the angle of the bird
        self.screen.blit(rotated_image, rotated_rect)  # draw the bird

        pygame.time.Clock().tick(DisplayConsts.FPS)  # respect fps for screen updates
        pygame.display.update()  # update the screen



