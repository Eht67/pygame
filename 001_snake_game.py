import pygame
import random
import os

pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
darkred = (190, 0, 0)
black = (0, 0, 0)
grey = (220,220,220)
dark_green = (0,150,0)
yellow = (200,200,0)
pink = (255,105,180)
lightskyblue = (140,211,255)

# Creating window
screen_width = 1080
screen_height = 1328
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snake Game by Ehtsham")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 80)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# wellcome function
def welcome():
    exit_game = False
    while not exit_game:
        pygame.mixer.music.load("snake_wellcome.mp3")
        pygame.mixer.music.play(-1)
        gameWindow.fill(dark_green)
        text_screen("Welcome to Snakes By EHK", black, 150, 490)
        text_screen("Press ENTER key To Play", yellow, 180, 550)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(60, 1030)
    food_y = random.randint(60, 1278)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(grey)
            text_screen("Game Over! Press Enter To Continue!", darkred, 40, 400)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if velocity_x == 0:
                            velocity_x = init_velocity
                            velocity_y = 0

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if velocity_x == 0:
                            velocity_x = - init_velocity
                            velocity_y = 0

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if velocity_y == 0:
                            velocity_y = - init_velocity
                            velocity_x = 0

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if velocity_y == 0:
                            velocity_y = init_velocity
                            velocity_x = 0

                    if event.key == pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<snake_size and abs(snake_y - food_y)<snake_size:
                score +=10
                food_x = random.randint(60, 850)
                food_y = random.randint(60, 550)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(lightskyblue)
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), darkred, 5, 5)
            pygame.draw.rect(gameWindow, pink, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()