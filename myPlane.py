import os

import pygame


class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('resource/images', 'me1.png'))
        self.rect = self.image.get_rect()  # get the rect of my plane
        self.width, self.height = bg_size[0], bg_size[1]

        self.rect.left, self.rect.top = (
                                                    self.width - self.rect.width) // 2, self.height - self.rect.height - 60  # my plane position

        self.speed = 10

    def moveUP(self):
        pass

    def moveDOWN(self):
        pass

    def moveLEFT(self):
        pass

    def moveRIGHT(self):
        pass
