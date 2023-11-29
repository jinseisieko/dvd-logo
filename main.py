import math
import random

import pygame
from PIL import Image, ImageDraw

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
        self.rect.fill((255, 255, 255))

        self.image = Image.open("DVD_logo.png")
        self.image = self.image.resize((200, 100))
        self.pix = self.image.load()
        self.draw = ImageDraw.Draw(self.image)

        size = self.image.size
        data = self.image.tobytes()
        mode = self.image.mode
        self.image_logo = pygame.image.fromstring(data, size, mode)

        self.update_color()

    def update_color(self):
        color = tuple([random.randint(0, 255) for _ in range(3)] + [255])

        pixdata = self.image.load()
        for y in range(self.image.size[1]):
            for x in range(self.image.size[0]):
                r, g, b, a = pixdata[x, y][0], pixdata[x, y][1], pixdata[x, y][2], pixdata[x, y][3]

                if a > 10:
                    pixdata[x, y] = color
        size = self.image.size
        data = self.image.tobytes()
        mode = self.image.mode
        self.image_logo = pygame.image.fromstring(data, size, mode)

    def update(self):
        self.x += self.velocity * math.cos(self.angle) * (-1) ** self.minus_x
        self.y += self.velocity * math.sin(self.angle) * (-1) ** self.minus_y
        if self.x + self.width > FIELD_WIDTH:
            self.update_color()

            self.minus_x = 1
            self.x = FIELD_WIDTH - self.width
        if self.y + self.height > FIELD_HEIGHT:
            self.update_color()

            self.minus_y = 1
            self.y = FIELD_HEIGHT - self.height
        if self.y < 0:
            self.update_color()
            self.minus_y = 0
            self.y = 0
        if self.x < 0:
            self.update_color()
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
    screen.fill((0, 0, 0))

    screen.blit(rectangle.image_logo, (rectangle.x, rectangle.y))

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
