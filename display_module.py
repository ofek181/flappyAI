import pygame
from consts import DisplayConsts


class Display:
    """
             A class to implement the display of the game.
             ----------------------------
             Attributes
             ----------------------------
             screen : pygame object
                 an attribute to represent the screen of the game.
             font : pygame object
                 implements the font of the game.
             font_color : int tuple
                 three integer tuple to represent the RGB color
             ----------------------------
             Methods
             ----------------------------
             __init__(self):
                 Constructs all the necessary attributes for the Display object.
             animate_game(self):
                 Uses pygame methods in order to display the game on the screen.
    """
    def __init__(self):
        """
            Constructs all the necessary attributes for the Display object.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((DisplayConsts.SCREEN_HEIGHT, DisplayConsts.SCREEN_HEIGHT))
        self.font = pygame.font.SysFont(DisplayConsts.FONT_TYPE, DisplayConsts.FONT_SIZE)
        self.font_color = DisplayConsts.FONT_COLOR  # white RGB color

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
            self.screen.blit(pipe_pair.pipe_image[1], (pipe_pair.x, pipe_pair.top_pipe_edge))
            self.screen.blit(pipe_pair.pipe_image[0], (pipe_pair.x, pipe_pair.bot_pipe_edge))

        rotated_image, rotated_rect = bird.animate()  # animate the angle of the bird
        self.screen.blit(rotated_image, rotated_rect)  # draw the bird

        surface = self.font.render('Score: ' + str(bird.score), True, self.font_color)  # show score
        rect = surface.get_rect()
        rect.midtop = (DisplayConsts.SCREEN_WIDTH // 12, DisplayConsts.SCREEN_HEIGHT // 15)
        self.screen.blit(surface,rect)

        pygame.time.Clock().tick(DisplayConsts.FPS)  # respect fps for screen updates
        pygame.display.update()  # update the screen


