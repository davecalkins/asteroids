import pygame
from constants import *
from player import *

def main():
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )

    surf = pygame.display.get_surface()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.draw(surf)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
