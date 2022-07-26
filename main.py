import pygame
import sys
import traceback

from pygame.locals import *

import enemy
import myPlane

pygame.init()
pygame.mixer.init()

bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("Aircraft Battle_GG")

background = pygame.image.load("resource/images/background.png").convert()

# load game
pygame.mixer.music.load("resource/sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("resource/sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("resource/sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("resource/sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("resource/sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("resource/sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("resource/sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("resource/sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("resource/sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("resource/sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("resource/sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("resource/sound/me_down.wav")
me_down_sound.set_volume(0.2)


def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)


def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


def main():
    pygame.mixer.music.play(-1)

    # generate my plane
    me = myPlane.MyPlane(bg_size)
    clock = pygame.time.Clock()

    # # generate enemy
    # enemies = pygame.sprite.Group()
    # # small
    # small_enemies = pygame.sprite.Group()
    # add_small_enemies(small_enemies, enemies, 15)
    # # middle
    # mid_enemies = pygame.sprite.Group()
    # add_mid_enemies(mid_enemies, enemies, 4)
    # # big
    # big_enemies = pygame.sprite.Group()
    # add_big_enemies(big_enemies, enemies, 2)

    running = True
    switch_image = True

    # delay of image
    delay = 100

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # get keyboard
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            me.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveRight()

        screen.blit(background, (0, 0))

        # # paint big enemy planes
        # for each in big_enemies:
        #     each.move()
        #     if switch_image:
        #         screen.blit(each.image1, each.rect)
        #     else:
        #         screen.blit(each.image2, each.rect)
        #     if each.rect.bottom > -50:
        #         enemy3_fly_sound.play()
        #
        # # paint mid enemy planes
        # for each in mid_enemies:
        #     each.move()
        #     screen.blit(each.image, each.rect)
        #
        # # paint big enemy planes
        # for each in small_enemies:
        #     each.move()
        #     screen.blit(each.image, each.rect)

        # e = 0
        # while e < 10:
        #     e += 1
        #     pl = enemy.SmallEnemy(bg_size)
        #     pl.move()
        #     screen.blit(pl.image, pl.rect)
        #
        # # switch my Plane
        # if switch_image:
        #     screen.blit(me.image1, me.rect)
        # else:
        #     screen.blit(me.image2, me.rect)

        # delay switch image of plane
        if not (delay % 5):
            switch_image = not switch_image

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()

        clock.tick(60)



    if __name__ == "__main__":
        try:
            main()
        except SystemExit:
            pass
        except:
            traceback.print_exc()
            pygame.quit()
            input()
