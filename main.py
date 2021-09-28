import pygame
import sys
from bird_module import Bird
from floor_module import Floor
from pipes_module import PipePair
from display_module import Display
from logic_module import Logic
import consts


def main():
    bird = Bird()  # create bird
    floor = Floor()  # create floor
    pipes = [PipePair(x_pos=500 + i * consts.PipeConsts.HORIZONTAL_GAP)
             for i in range(10)]  # create 10 pipes
    closest_pipe = pipes[0]
    display = Display()  # create the display
    while True:
        display.animate_game(bird=bird, pipe_pairs=pipes, floor=floor)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                else:
                    bird.jump()
        bird.move()
        floor.move()
        for pipe in pipes:
            pipe.move()
        if Logic.check_collision(bird=bird, pipe_pair=pipes[0], floor=floor):
            pass
            # print("collision!")
        if Logic.check_score(bird=bird, closest_pipe=closest_pipe):
            bird.score += 1
            closest_pipe = pipes[1]
        if pipes[0].x + consts.PipeConsts.TOP_IMAGE.get_width() < 0:
            pipes.pop(0)  # remove the passed pipe
            pipes.append(PipePair(pipes[-1].x + consts.PipeConsts.HORIZONTAL_GAP,
                                  velocity=pipes[-1].velocity))  # append another pipe
        print(bird.velocity)


if __name__ == '__main__':
    main()
