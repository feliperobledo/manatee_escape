# import the pygame module, so you can use it
import pygame
from src.resolutions import Dimensions, RES_4_BY_3
import src.utils.colors as Colors
from src.utils.math import Point
from src.gameobject import GameObject, PieceFactory, Pieces

ASSETS_DIR = "./assets/"
ART_DIR = "{assets_dir}/art".format(assets_dir=ASSETS_DIR)


def get_art_asset_path(asset_name):
    return "{base_path}/{asset_name}".format(base_path=ART_DIR, asset_name=asset_name)


# define a main function
def main():

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(get_art_asset_path("logo32x32.png"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Manatee Escape")

    # create a surface on screen that has the size of 240 x 180
    chosen_resolution = RES_4_BY_3[0]
    screen = pygame.display.set_mode(chosen_resolution.raw)

    # define a variable to control the main loop
    running = True

    map = [
        ["P", " ", " ", " ", " "],
        [" ", "R", " ", "R", " "],
        [" ", " ", "", " ", " "],
        [" ", "R", " ", "R", " "],
        [" ", " ", " ", " ", " "],
    ]

    map_rows = len(map)
    map_columns = len(map[0])

    dimensions = Dimensions(
        width=chosen_resolution.width /  map_columns,
        height=chosen_resolution.height / map_rows,
    )

    go_list = []
    for row_index, row_data in enumerate(map):
        for col_index, col_data in enumerate(row_data):
            position = Point(
                x=dimensions.width * col_index,
                y=dimensions.height * row_index,
            )

            if col_data == "R":
                go_list.append(PieceFactory.instantiate(Pieces.ROCK, dimensions, position))
            elif col_data == " ":
                pass
            elif col_data == "P":
                player = PieceFactory.instantiate(Pieces.PLAYER, dimensions, position)


    # main loop
    while running:
        screen.fill(Colors.black.rgb)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.position.x -= player.dimensions.width
                if event.key == pygame.K_RIGHT:
                    player.position.x += player.dimensions.width
                if event.key == pygame.K_DOWN:
                    player.position.y += player.dimensions.height
                if event.key == pygame.K_UP:
                    player.position.y -= player.dimensions.height
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        for go in go_list:
            pygame.draw.rect(screen, go.color.rgb, go.aabb)

        pygame.draw.rect(screen, player.color.rgb, player.aabb)

        pygame.display.update()
