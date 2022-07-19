import os
import pygame as pg

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")


def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pg.mixer.Sound(fullname)

    return sound



background_colour = (255,255,255)
width, height = (1280, 480)

if __name__ == "__main__":
    # pg.display.init()
    pg.init()
    screen = pg.display.set_mode((width, height), pg.SCALED)
    pg.display.set_caption("Map Painter")
    screen.fill(background_colour)
    pg.mouse.set_visible(True)
    pg.display.flip()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False