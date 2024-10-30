import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # OG positioning
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if player.collision(a):
                print("Game over!")
                return
            for s in shots:
                if s.collision(a):
                    s.kill()
                    a.split()
        
        screen.fill((0,0,0))
        
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        tock = clock.tick(60)
        dt = tock/1000


if __name__ == "__main__":
    main()
