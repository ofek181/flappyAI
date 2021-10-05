import pygame
import os
local_dir_images = os.path.join(os.path.dirname(__file__), "images")
local_dir_music = os.path.join(os.path.dirname(__file__), "music")


class BirdConsts:
    BIRD_IMAGES = [pygame.image.load(os.path.join(local_dir_images, 'bird_wing_middle.png')),
                   pygame.image.load(os.path.join(local_dir_images, 'bird_wing_up.png')),
                   pygame.image.load(os.path.join(local_dir_images, 'bird_wing_down.png'))]
    GRAVITY = 2
    MAX_VELOCITY = 14
    MAX_UP_ANGLE = 45
    MIN_DOWN_ANGLE = -90
    ANGULAR_ACCELERATION = 0.3
    MIN_ANGULAR_ACCELERATION = 7
    JUMP_VELOCITY = -16
    FLAP_DOWN_ANGLE = -45


class PipeConsts:
    BOT_IMAGE = pygame.image.load(os.path.join(local_dir_images, 'pipe.png'))
    TOP_IMAGE = pygame.transform.flip(BOT_IMAGE, False, True)
    MIN_LENGTH = 100
    MAX_LENGTH = 250
    VERTICAL_GAP = 130  # gap between top and bottom pipe
    HORIZONTAL_GAP = 200  # gap between pipe pairs on the x axis
    PIPE_STARTING_VELOCITY = 6
    PIPE_MAX_VELOCITY = 13
    PIPE_ACCELERATION_X = 0.002


class FloorConsts:
    FLOOR_IMAGE = pygame.image.load(os.path.join(local_dir_images, 'floor.png'))
    FLOOR_STARTING_VELOCITY = 6
    FLOOR_MAX_VELOCITY = 13
    FLOOR_ACCELERATION_X = 0.002


class DisplayConsts:
    FPS = 30
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 500
    FONT_COLOR = (255, 255, 255)
    GAME_OVER_FONT_COLOR = (200, 40, 80)
    FONT_SIZE = 70
    GAME_OVER_FONT_SIZE = 80
    FONT_TYPE = 'Comic Sans MS'
    GAME_OVER_FONT_TYPE = 'Comic Sans MS'
    BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join(local_dir_images, 'background.png')),
                                              (SCREEN_WIDTH, SCREEN_HEIGHT))


class AudioConsts:
    BACKGROUND_AUDIO = os.path.join(local_dir_music, 'background_music.wav')
    GAME_OVER_AUDIO = os.path.join(local_dir_music, 'game_over.wav')
    SCORE_AUDIO = os.path.join(local_dir_music, 'score.wav')




