import pygame
import random, os.path, time, sys
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

def roll():
    i = 0
    result = spin_slot_machine()
    while i < 40:
        screen.blit(img_list[(i + 1) % 7], (0, verticalplace))
        screen.blit(img_list[(i - 2) % 7], (longueur/2-dim_image/2, verticalplace))
        screen.blit(img_list[(i +2) % 7], (longueur-dim_image, verticalplace))
        i += 1
        pygame.display.flip()
        time.sleep(0.1)

    screen.blit(result[0], (0, verticalplace))
    screen.blit(result[1], (longueur/2-dim_image/2, verticalplace))
    screen.blit(result[2], (longueur-dim_image, verticalplace))
    pygame.display.flip()

def spin_slot_machine():
    # Spin the slot machine
    result = [random.choice(img_list) for _ in range(3)]
    return result

pygame.init()


winstyle = 0  # |FULLSCREEN
bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

img_7 = load_image('7.png')
img_bean = load_image('bean.png')
img_icebath = load_image('icebath.png')
img_jdg = load_image('jdg.png')
img_loup = load_image('loup.png')
img_sherb = load_image('sherb.png')
img_singe = load_image('singe.png')

img_list = [img_7,img_bean,img_icebath,img_jdg,img_loup,img_sherb,img_singe]

verticalplace = hauteur/2 - dim_image/2

running = True


while running:
    # input("Press Enter to spin. Press 'q' to quit.\n")
    # roll()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
            roll()
            time.sleep(0.5)
            # if keydown event happened
            # than printing a string to output
            print("A key has been pressed")
#     # Did the user click the window close button?
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Fill the background with white
#     screen.blit(imm, (0, verticalplace))
#     screen.blit(imm, (longueur/2-dim_image/2, verticalplace))
#     screen.blit(imm, (longueur-dim_image, verticalplace))

#     # Flip the display
#     pygame.display.flip()

# Done! Time to quit.
pygame.quit()