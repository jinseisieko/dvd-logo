import math
import random

import pygame

pygame.init()
FIELD_WIDTH, FIELD_HEIGHT = 1500, 1000


class Rectangle:
    def __init__(self, width, height, x, y, angle):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.angle = angle
        self.velocity = 2.0
        self.minus_x = 0
        self.minus_y = 0
        self.rect = pygame.Surface((width, height))
        self.rect.fill((255, 255, 255, 128))

    def update(self):
        self.x += self.velocity * math.cos(self.angle) * (-1) ** self.minus_x
        self.y += self.velocity * math.sin(self.angle) * (-1) ** self.minus_y
        if self.x + self.width > FIELD_WIDTH:
            self.minus_x = 1
            self.x = FIELD_WIDTH - self.width
        if self.y + self.height > FIELD_HEIGHT:
            self.minus_y = 1
            self.y = FIELD_HEIGHT - self.height
        if self.y < 0:
            self.minus_y = 0
            self.y = 0
        if self.x < 0:
            self.minus_x = 0
            self.x = 0


field: pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
screen: pygame.Surface = pygame.display.set_mode((FIELD_WIDTH, FIELD_HEIGHT))

rectangle = Rectangle(200, 100, 0, 0, 0.5)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    rectangle.update()
    screen.fill(([random.randint(0, 255) for _ in range(3)]))
    screen.blit(rectangle.rect, (rectangle.x, rectangle.y))

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
