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
           top_pipe_length : int
               length of the top pipe
           top_pipe_edge: int
               the upper edge of the top pipe
           bot_pipe_edge: int
               the upper edge of the bot pipe
           ----------------------------
           Methods
           ----------------------------
           __init__(self, x):
               Constructs all the necessary attributes for the PipePair object.
           move(self):
               Moves the pipe pair at each frame.
           set_positions(self):
               Sets random height positions of the pipe pair with fixed vertical gap
    """
    def __init__(self, x_pos: int = 600):
        """
           Constructs all the necessary attributes for the PipePair object.
              Parameters:
                  x_pos (int): x position of the pipe pair
        """
        self.x = x_pos  # x position of the pipe pair
        self.pipe_image = []
        self.pipe_image[0] = PipeConsts.BOT_IMAGE  # index 0 represents bottom pipe
        self.pipe_image[1] = PipeConsts.TOP_IMAGE  # index 1 represents top pipe
        self.top_pipe_length = self.pipe_image[1].get_height() - random.randrange(PipeConsts.MIN_LENGTH,
                                                                                  PipeConsts.MAX_LENGTH)
        self.top_pipe_edge = self.top_pipe_length - self.pipe_image[1].get_length()
        self.bot_pipe_edge = self.top_pipe_length + PipeConsts.VERTICAL_GAP  # y position of the bottom pipe's edge

    def move(self):
        """
           Implements the movement of the pipe pair.
        """
        self.x -= PipeConsts.PIPE_VELOCITY

    def set_positions(self):
        """
           Sets random height for the pipe pair with fixed vertical gap.
        """
        self.top_pipe_length = self.pipe_image[1].get_height() - random.randrange(PipeConsts.MIN_LENGTH,
                                                                                  PipeConsts.MAX_LENGTH)
        self.top_pipe_edge = self.top_pipe_length - self.pipe_image[1].get_length()
        self.bot_pipe_edge = self.top_pipe_length + PipeConsts.VERTICAL_GAP  # y position of the bottom pipe's edge


