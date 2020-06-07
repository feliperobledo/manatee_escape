from resolutions import Dimensions
from utils.colors import Color, red
from utils.math.point import Point


class GameObject:
    def __init__(self, *args, **kwargs):
        self.color = kwargs.get('color', red)
        self.dimensions = kwargs.get('dimensions', Dimensions(width=150, height=150))
        self.position = kwargs.get('position', Point(x=100, y=100))

    @property
    def aabb(self):
        return (self.position.x, self.position.y, self.dimensions.width, self.dimensions.height)


