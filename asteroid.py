import pygame
import random
from constants import *
from circleshape import * 


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            first_vector = self.velocity.rotate(angle)
            second_vector = self.velocity.rotate(-angle)
            first_ast_radius = self.radius - ASTEROID_MIN_RADIUS
            second_ast_radius = self.radius - ASTEROID_MIN_RADIUS
            first_ast = Asteroid(self.position.x, self.position.y, first_ast_radius)
            second_ast = Asteroid(self.position.x, self.position.y, second_ast_radius)
            first_ast.velocity = first_vector*1.2
            second_ast.velocity = second_vector*1.2

            


