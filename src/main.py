# import the pygame module, so you can use it
import pygame
from resolutions import RES_4_BY_3
from colors import red, white, light_green

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
    screen = pygame.display.set_mode(RES_4_BY_3[0])

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    screen.fill(red)
                if event.key == pygame.K_RIGHT:
                    screen.fill(white)
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.draw.rect(screen, light_green, (0, 0, 50, 50))
        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
