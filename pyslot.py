import pygame
import random, os.path
from pygame.locals import *
main_dir = os.path.split(os.path.abspath(__file__))[0]

longueur = 1600
hauteur = 900

dim_image = 400

SCREENRECT     = Rect(0, 0, longueur, hauteur)

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'assets', file)
    print(file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

pygame.init()



winstyle = 0  # |FULLSCREEN
bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

imm = load_image('7.png')

verticalplace = hauteur/2 - dim_image/2

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.blit(imm, (0, verticalplace))
    screen.blit(imm, (longueur/2-dim_image/2, verticalplace))
    screen.blit(imm, (longueur-dim_image, verticalplace))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()