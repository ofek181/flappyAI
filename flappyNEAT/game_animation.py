import pygame
from flappyGame.consts import DisplayConsts


class NeatDisplay:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((DisplayConsts.SCREEN_HEIGHT, DisplayConsts.SCREEN_HEIGHT))

    def show_score(self, score):
        """
            Displays the score over the screen
        """
        font = pygame.font.SysFont(DisplayConsts.FONT_TYPE, DisplayConsts.FONT_SIZE)
        surface = font.render(str(score), True, DisplayConsts.FONT_COLOR)  # show score
        rect = surface.get_rect()
        rect.midtop = (DisplayConsts.SCREEN_WIDTH // 2.5, DisplayConsts.SCREEN_HEIGHT // 20)
        self.screen.blit(surface, rect)
        pygame.display.update()  # update the screen

    def animate_game(self, birds, pipes, floor):
        self.screen.blit(DisplayConsts.BACKGROUND_IMAGE, (0, 0))  # draw background

        self.screen.blit(floor.floor_image[0], (floor.x[0], floor.y))  # draw the first floor
        self.screen.blit(floor.floor_image[1], (floor.x[1], floor.y))  # draw the second floor
        self.screen.blit(floor.floor_image[2], (floor.x[2], floor.y))  # draw the third floor

        for pipe in pipes:  # draw the pipes
            self.screen.blit(pipe.pipe_image[1], (pipe.x, pipe.top_pipe_head))
            self.screen.blit(pipe.pipe_image[0], (pipe.x, pipe.bot_pipe_head))

        for bird in birds:
            rotated_image, rotated_rect = bird.animate()  # animate the angle of the bird
            self.screen.blit(rotated_image, rotated_rect)  # draw the bird

        pygame.time.Clock().tick(DisplayConsts.FPS)  # respect fps for screen updates
        pygame.display.update()  # update the screen



