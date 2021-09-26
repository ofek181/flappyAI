import pygame
from consts import BirdConsts


class Bird:
    """
        A class to represent a bird.
        ----------------------------
        Attributes
        ----------------------------
        bird_image : png
            images of the bird flapping its wings
        x, y position : int
            x,y position of the bird in the screen
        counter_from_last_jump : int
            number of frames the bird had passed
        angle: int
            angle of the bird during flight
        velocity: int
            velocity of the bird's flight
        score: int
            number of pipes the bird had passed
        ----------------------------
        Methods
        ----------------------------
        __init__(self, x, y):
            Constructs all the necessary attributes for the bird object.
        move(self):
            Moves the bird for each frame.
        jump(self):
            Implements the jumping action of the bird.
        animate(self):
            Implements the animation of the bird during jumps and flaps
        """
    def __init__(self, x_pos: int, y_pos: int):
        """
            Constructs all the necessary attributes for the bird object.
                   Parameters:
                           x_pos (int): x position of the bird
                           y_pos (int): y position of the bird
        """
        self.image_index = 0  # there's a list of images for making the animation
        self.bird_image = BirdConsts.BIRD_IMAGES[self.image_index]  # use first image as starting image
        self.x, self.y = x_pos, y_pos  # starting x and y position of the bird
        self.counter_from_last_jump = 0  # counting each jump to form acceleration
        self.angle = 0  # starting angle
        self.velocity = 0  # starting velocity
        self.score = 0  # starting score

    def move(self):
        """
            Implements the bird's movement for each frame using d = vt + 1/2at^2
        """
        self.counter_from_last_jump += 1  # happens for each frame
        accelerate = 1 / 2 * BirdConsts.GRAVITY * self.counter_from_last_jump ** 2
        distance = self.velocity * self.counter_from_last_jump + accelerate  # Distance equation
        self.y = self.y + distance  # update the position of the bird with distance
        if distance < 0:  # the bird is going upwards
            if self.angle < BirdConsts.MAX_UP_ANGLE:  # the upper limit of the bird's angle
                angle_diff = (BirdConsts.MAX_UP_ANGLE - self.angle)
                self.angle += BirdConsts.ANGULAR_ACCELERATION * angle_diff  # accelerate angle up
            else:
                self.angle = BirdConsts.MAX_UP_ANGLE
        else:   # the bird is going downwards
            if self.angle > BirdConsts.MIN_DOWN_ANGLE:
                angle_diff = (BirdConsts.MIN_DOWN_ANGLE - self.angle)
                self.angle += BirdConsts.ANGULAR_ACCELERATION * angle_diff  # accelerate angle down
            else:
                self.angle = BirdConsts.MIN_DOWN_ANGLE

    def jump(self):
        """
            Implements the bird's jumping mechanism
        """
        self.velocity = BirdConsts.JUMP_VELOCITY  # jumping force
        self.counter_from_last_jump = 0  # when we jump, we reset the count to 0

    def animate(self) -> [BirdConsts.BIRD_IMAGES[0], pygame.rect]:
        """
            Implements the bird's animation for flying upwards and downwards
            :returns
                angled_image: the rotated image of the bird
                angled_rect: the rotated rectangle with the original image center
        """
        if self.angle < BirdConsts.FLAP_DOWN_ANGLE:  # bird doesn't flap when falling
            self.image_index = 0
            self.bird_image = BirdConsts.BIRD_IMAGES[self.image_index]

        elif self.image_index >= len(BirdConsts.BIRD_IMAGES):  # zero out counter when reaches end
            self.image_index = 0

        # update image and index to form the flapping wings animation
        self.bird_image = BirdConsts.BIRD_IMAGES[self.image_index]
        self.image_index += 1

        # rotate the bird image
        angled_image = pygame.transform.rotate(self.bird_image, self.angle)
        # store the center of unrotated image
        origin_center = self.bird_image.get_rect(topleft=(self.x, self.y)).center
        # update the center of the rotated image rectangle
        angled_rect = angled_image.get_rect(center=origin_center)
        # return the rotated image and rectangle
        return angled_image, angled_rect


