import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)        
        rad = self.radius - ASTEROID_MIN_RADIUS
        
        a1 = Asteroid(self.position.x, self.position.y, rad)
        a1.velocity = self.velocity.rotate(angle) * 1.2

        a2 = Asteroid(self.position.x, self.position.y, rad)
        a2.velocity = self.velocity.rotate(-angle)
