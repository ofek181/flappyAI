from consts import FloorConsts


class Floor:
    """
           A class to represent the floor.
           ----------------------------
           Attributes
           ----------------------------
           floor_image : list[pngs]
               list of three identical images of the floor to implement the movement animation
           x : list[int]
               x position of the three images
           y : int
               y position of the images
           ----------------------------
           Methods
           ----------------------------
           __init__(self, y):
               Constructs all the necessary attributes for the floor object.
           move(self):
               Moves the floor with the velocity of the pipes
    """
    def __init__(self, y_pos: int = 400):
        """
            Constructs all the necessary attributes for the floor object.
               Parameters:
                   y_pos (int): y position of the floor
        """
        # three identical images of the floor will be used to animate the floor's movement.
        self.floor_image = [FloorConsts.FLOOR_IMAGE, FloorConsts.FLOOR_IMAGE, FloorConsts.FLOOR_IMAGE]
        self.x = [0, FloorConsts.FLOOR_IMAGE.get_width(), FloorConsts.FLOOR_IMAGE.get_width() * 2]
        self.y = y_pos  # the y position of the floor image
        self.velocity = FloorConsts.FLOOR_STARTING_VELOCITY

    def move(self):
        """
           Implements the movement of the floor with respect to game velocity.
        """
        self.velocity += FloorConsts.FLOOR_ACCELERATION_X
        self.velocity = min(self.velocity, FloorConsts.FLOOR_MAX_VELOCITY)
        self.x = [pos - self.velocity
                  for pos in self.x]  # move position left with respect to velocity
        if abs(self.x[0]) > abs(FloorConsts.FLOOR_IMAGE.get_width()):  # if the images move out of screen
            self.x[0] = self.x[2] + FloorConsts.FLOOR_IMAGE.get_width()
        if abs(self.x[1]) > abs(FloorConsts.FLOOR_IMAGE.get_width()):  # if the images move out of screen
            self.x[1] = self.x[0] + FloorConsts.FLOOR_IMAGE.get_width()
        if abs(self.x[0]) > abs(FloorConsts.FLOOR_IMAGE.get_width()):  # if the images move out of screen
            self.x[2] = self.x[1] + FloorConsts.FLOOR_IMAGE.get_width()


