import pygame
from pygame.draw_py import draw_line
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        #screen.blit(mole_image, mole_image.get_rect(topleft=(0,0)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()


        running = True
        mole = (0,0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[0] // 32 == mole[0] and event.pos[1] // 32 == mole[1]:
                        mole = random.randrange(0, 20), random.randrange(0,15)
            screen.fill("pink")

            for i in range(0,17):
                pygame.draw.line(screen, 'navy', (0,i*32), (640, i*32))
            for i in range(0,21):
                pygame.draw.line(screen, 'navy', (i*32, 0), (i*32, 512))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole[0] * 32, mole[1] * 32)))

            pygame.display.flip()
            clock.tick(60)
            #screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
