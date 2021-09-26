import pygame


class BirdConsts:
    BIRD_IMAGES = [pygame.image.load('images/bird_wing_middle.png'),
                   pygame.image.load('images/bird_wing_up.png'),
                   pygame.image.load('images/bird_wing_down.png')]
    GRAVITY = 10
    MAX_UP_ANGLE = 45
    MIN_DOWN_ANGLE = -90
    ANGULAR_ACCELERATION = 0.5
    MIN_ANGULAR_ACCELERATION = 5
    JUMP_VELOCITY = -10
    FLAP_DOWN_ANGLE = -45


class PipeConsts:
    BOT_IMAGE = pygame.image.load('images/pipe.png')
    TOP_IMAGE = pygame.transform.flip(BOT_IMAGE, False, True)
    MIN_LENGTH = 100
    MAX_LENGTH = 300
    VERTICAL_GAP = 150  # gap between top and bottom pipe
    HORIZONTAL_GAP = 200  # gap between pipe pairs on the x axis
    PIPE_VELOCITY = 5


class FloorConsts:
    FLOOR_IMAGE = pygame.image.load('images/floor.png')
    FLOOR_VELOCITY = 5


class DisplayConsts:
    FPS = 30
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 550
    BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load('images/background.png'),
                                              (SCREEN_WIDTH, SCREEN_HEIGHT))
