import os

import pygame


class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load(os.path.join('resource/images', 'me1.png'))
        self.image2 = pygame.image.load(os.path.join('resource/images', 'me2.png'))
        self.rect = self.image1.get_rect()  # get the rect of my plane
        self.width, self.height = bg_size[0], bg_size[1]

        self.rect.left, self.rect.top = (
                                                    self.width - self.rect.width) // 2, self.height - self.rect.height - 60  # my plane position

        self.speed = 10

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.height - 60 > self.rect.bottom:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width
