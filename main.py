# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

import pygame

# init sets up the gui for the game.
pygame.init()

# Color variables in RGB Format
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
green = (0, 255, 0)
eh = (200, 50, 57)

# Measurements of the display for the GUI
dis_width = 800
dis_height = 600

# Sets the display setting, to later be called on.
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Nexhi's snake game")
# Applies any updates to the display after every change.
pygame.display.update()

# Setting the variable for clock to exit the game automatically.
clock = pygame.time.Clock()

# Setting the size of the of the snake block thatll be eating the dots
snake_block = 10

# setting the speed of the snake, try not to set this high unless you have excellent reaction skills.
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, green)
    dis.blit(value, [0, 0])


# Sets the player's snake.
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# Display any message with any desired color on the GUI.
def message(msg, color):
    mesg = font_style.render(msg, True, blue)
    dis.blit(mesg, [dis_width / 3, dis_height / 3])


# This activates the game and keeps it on.
def gameLoop():
    # Setting these both to false
    # game over being when the program is done, game close is when the game is done
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            dis.fill(white)
            message("Try again? Y or N", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_y:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
            if event.type == pygame.QUIT:
                game_over = True

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(eh)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake-1)
        pygame.display.update()
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10
            Length_of_snake += 1
            print("Yummy!!")
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()

# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
