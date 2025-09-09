import sys
import pygame
from constants import *
from pygame.color import THECOLORS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    
    Player.containers = (updatable, drawable)
    
    
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)    
        
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collides_with(bullet):
                    asteroid.split()
                    bullet.kill()
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        
        screen.fill('black')
    
        for object in drawable:
            object.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    

if __name__ == "__main__":
    main()
