import random
from consts import PipeConsts


class PipePair:
    """
           A class to represent a pipe pair.
           ----------------------------
           Attributes
           ----------------------------
           x : int
               x position of the pipe pair on the screen
           pipe_image : list
               list of images for the top and bottom pipes
           top_pipe_head: int
               the upper edge of the top pipe
           bot_pipe_head: int
               the upper edge of the bot pipe
           velocity: float
               the velocity of the moving pipe (same as floor)
           ----------------------------
           Methods
           ----------------------------
           __init__(self, x):
               Constructs all the necessary attributes for the PipePair object.
           move(self):
               Moves the pipe pair at each frame.
    """
    def __init__(self, x_pos: int = 500, velocity: int = PipeConsts.PIPE_STARTING_VELOCITY):
        """
           Constructs all the necessary attributes for the PipePair object.
              Parameters:
                  x_pos (int): x position of the pipe pair
                  velocity (int) : starting velocity of the instance
        """
        self.x = x_pos  # x position of the pipe pair
        self.pipe_image = []
        self.pipe_image.append(PipeConsts.BOT_IMAGE)  # index 0 represents bottom pipe
        self.pipe_image.append(PipeConsts.TOP_IMAGE)  # index 1 represents top pipe

        # Setting random height for the pipe pair with fixed vertical gap.
        self.top_pipe_head = - random.randrange(PipeConsts.MIN_LENGTH, PipeConsts.MAX_LENGTH)
        self.bot_pipe_head = self.top_pipe_head + self.pipe_image[1].get_height() + PipeConsts.VERTICAL_GAP  # y position of the bottom pipe's edge
        self.velocity = velocity

    def move(self):
        """
           Implements the movement of the pipe pair with acceleration
        """
        self.velocity += PipeConsts.PIPE_ACCELERATION_X
        self.velocity = min(self.velocity, PipeConsts.PIPE_MAX_VELOCITY)
        self.x -= self.velocity



