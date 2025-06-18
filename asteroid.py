import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.random_color = random.randint(1,3)


    def draw(self, screen):
        color = "white"
        if (self.random_color == 1):
            color = "white"
        elif (self.random_color == 2):
            color = "green"
        else:
            color = "red"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)
    

    def update(self, dt):
        self.position += (self.velocity * dt)
        
        # Wrap around code
        #-----------------------------------------------
        if (self.position.x > 1340 or self.position.x < -60):
            if (self.position.x > 1340):
                self.position.x = 1340
            else:
                self.position.x = -60
            self.position.x = 1280 - self.position.x
        
        if (self.position.y > 780 or self.position.y < -60):
            if (self.position.y > 780):
                self.position.y = 780
            else:
                self.position.y = -60
            self.position.y = 720 - self.position.y
    

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return True
        else:
            random_angle = random.uniform(20, 50)
            first_asteroid_velocity = self.velocity.rotate(random_angle)
            second_asteroid_velocity = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = first_asteroid_velocity * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = second_asteroid_velocity * 1.2
            return False