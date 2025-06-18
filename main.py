import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def reset_game(player, asteroids, shots):
    print(f"Lives Left: {player.lives}")
    player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.rotation = 0
    for asteroid in asteroids:
        asteroid.kill()
    
    for shot in shots:
        shot.kill()




def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # player inputs
        updatable.update(dt)
        for asteroid in asteroids:
            if (player.detect_collision(asteroid)):
                player.lives -= 1
                if (player.lives <= 0):
                    print("Game Over!")
                    sys.exit()
                else:
                    reset_game(player, asteroids, shots)

            for shot in shots:
                if (asteroid.detect_collision(shot)):
                    is_scorable = asteroid.split()
                    if (is_scorable):
                        player.add_score()
                    shot.kill()

        # rendering
        screen.fill((0.0, 0.0, 0.0))
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        # update delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()