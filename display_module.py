import pygame
from bird_module import Bird
from floor_module import Floor
from pipes_module import PipePair
from logic_module import Logic
from consts import DisplayConsts


class Display:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((DisplayConsts.SCREEN_HEIGHT, DisplayConsts.SCREEN_HEIGHT))
        self.font = pygame.font.SysFont('comicsansms', 20)
        self.font_color = (255, 255, 255)  # white RGB color

    def draw_game(self, bird, pipe_pairs, floor):
        while True:

            # draw the background
            self.screen.blit(DisplayConsts.BACKGROUND_IMAGE, (0, 0))

            # draw the moving floor
            self.screen.blit(floor.floor_image[0], (floor.x[0], floor.y))
            self.screen.blit(floor.floor_image[1], (floor.x[1], floor.y))
            self.screen.blit(floor.floor_image[2], (floor.x[2], floor.y))

            # draw the moving pipes
            # for pipe_pair in pipe_pairs:
            self.screen.blit(pipe_pairs.pipe_image[1], (pipe_pairs.x, pipe_pairs.top_pipe_edge))
            self.screen.blit(pipe_pairs.pipe_image[0], (pipe_pairs.x, pipe_pairs.bot_pipe_edge))

            # draw the animated bird
            rotated_image, rotated_rect = bird.animate()
            self.screen.blit(rotated_image, rotated_rect)

            # add additional information
            surface = self.font.render('Score: ' + str(bird.score), True, self.font_color)
            rect = surface.get_rect()
            rect.midtop = (DisplayConsts.SCREEN_WIDTH / 2, DisplayConsts.SCREEN_HEIGHT / 1.8)
            self.screen.blit(surface,rect)

            pygame.display.update()  # show the surface


def main():
    bird = Bird()
    floor = Floor()
    pipe = PipePair()
    flappy = Display()
    flappy.draw_game(bird, pipe, floor)


if __name__ == '__main__':
    main()

