import pygame


class BirdConsts:
    BIRD_IMAGES = [pygame.image.load('images/bird_wing_middle.png'),
                   pygame.image.load('images/bird_wing_up.png'),
                   pygame.image.load('images/bird_wing_down.png')]
    GRAVITY = 2.5
    MAX_VELOCITY = 14
    MAX_UP_ANGLE = 45
    MIN_DOWN_ANGLE = -90
    ANGULAR_ACCELERATION = 0.5
    MIN_ANGULAR_ACCELERATION = 7
    JUMP_VELOCITY = -22
    FLAP_DOWN_ANGLE = -45


class PipeConsts:
    BOT_IMAGE = pygame.image.load('images/pipe.png')
    TOP_IMAGE = pygame.transform.flip(BOT_IMAGE, False, True)
    MIN_LENGTH = 100
    MAX_LENGTH = 250
    VERTICAL_GAP = 130  # gap between top and bottom pipe
    HORIZONTAL_GAP = 200  # gap between pipe pairs on the x axis
    PIPE_STARTING_VELOCITY = 6
    PIPE_MAX_VELOCITY = 18
    PIPE_ACCELERATION_X = 0.005


class FloorConsts:
    FLOOR_IMAGE = pygame.image.load('images/floor.png')
    FLOOR_STARTING_VELOCITY = 6
    FLOOR_MAX_VELOCITY = 18
    FLOOR_ACCELERATION_X = 0.005


class DisplayConsts:
    FPS = 30
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 500
    FONT_COLOR = (255, 255, 255)
    FONT_SIZE = 50
    FONT_TYPE = 'comicsansms'
    BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load('images/background.png'),
                                              (SCREEN_WIDTH, SCREEN_HEIGHT))
