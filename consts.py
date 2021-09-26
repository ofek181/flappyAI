class BirdConsts:
    BIRD_IMAGES = None
    GRAVITY = 10
    MAX_UP_ANGLE = 45
    MIN_DOWN_ANGLE = -90
    ANGULAR_ACCELERATION = 0.5
    MIN_ANGULAR_ACCELERATION = 5
    JUMP_VELOCITY = -10
    FLAP_DOWN_ANGLE = -45


class PipeConsts:
    TOP_IMAGE = None
    BOT_IMAGE = None
    MIN_LENGTH = 100
    MAX_LENGTH = 300
    VERTICAL_GAP = 150  # gap between top and bottom pipe
    HORIZONTAL_GAP = 200  # gap between pipe pairs on the x axis
    PIPE_VELOCITY = 5


class FloorConsts:
    FLOOR_IMAGE = None
    FLOOR_VELOCITY = 5
