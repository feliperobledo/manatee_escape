from enum import Enum


from src.resolutions import Dimensions
from src.utils.colors import Color, red, brown, blue, yellow, black, light_green, green
from src.utils.math.point import Point


class GameObject:
    def __init__(self, *args, **kwargs):
        self.color = kwargs.get('color', red)
        self.dimensions = kwargs.get('dimensions', Dimensions(width=150, height=150))
        self.position = kwargs.get('position', Point(x=100, y=100))

    @property
    def aabb(self):
        return (self.position.x, self.position.y, self.dimensions.width, self.dimensions.height)


class Pieces(Enum):
    ROCK = 0,
    OCEAN = 1,
    BOAT = 2,
    FLOWER = 3,
    SEAGRASS = 4,
    PLAYER = 5


class PieceFactory:
    _color_codes = {
        Pieces.ROCK: brown,
        Pieces.OCEAN: blue,
        Pieces.BOAT: red,
        Pieces.FLOWER: yellow,
        Pieces.SEAGRASS: light_green,
        Pieces.PLAYER: green,
    }

    @staticmethod
    def instantiate(piece_type, dimensions, position):
        color = PieceFactory._color_codes[piece_type]
        return GameObject(position=position, color=color, dimensions=dimensions)

