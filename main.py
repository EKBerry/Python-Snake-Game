# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Nexhi's snake game")
pygame.display.update()

x1 = dis_width / 2
y1 = dis_height / 2

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 30

font_style = pygame.font.SysFont(None, 30)


def message(msg, color):
    mesg = font_style.render(msg, True, blue)
    dis.blit(mesg, [dis_width / 3, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block / 10.0))
    foody = round(random.randrange(0, dis_width - snake_block / 10.0))


while not game_over:
    while game_close == True:
        dis.fill(white)
        message("You Lost! Press Q to quit or E to retry", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.k_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.k_c:
                    gameLoop()
    for event in pygame.event.get()
        if event.type == pygame.QUIT:
            game_over = True
            

            if event.key == pygame.K_LEFT:
               #x1_change = -snake_block
              # y1_change = 0#
            elif event.key == pygame.K_RIGHT:
               # x1_change = snake_block
                #y1_change = 0
            elif event.key == pygame.K_UP:
                # y1_change = -snake_block
              #  x1_change = 0
            elif event.key == pygame.K_DOWN:
                #y1_change = snake_block
              #  x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
           # game_over = True
            clock.tick(snake_speed)
            message("You lost", blue)
            pygame.display.update()
            time.sleep(2)

      #  x1 += x1_change
      #  y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])

        pygame.display.update()
        if event.type == pygame.QUIT:
          #  game_over = True

pygame.quit()
quit()

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
