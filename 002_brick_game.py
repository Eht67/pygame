# importing and initializing pygame module
import pygame
pygame.init()
pygame.mixer.init()

# defining colors
red = (255, 0, 0)
pink = (255,105,180)
dark_green = (0,100,0)
white = (255,255,255)
yellow = (255,255,0)
black = (0,0,0)

# making bricks
bricks1 = [pygame.Rect(23 + i*95, 40, 80, 30) for i in range(6)]
bricks2 = [pygame.Rect(23 + i*95, 80, 80, 30) for i in range(6)]
bricks3 = [pygame.Rect(23 + i*95, 120, 80, 30) for i in range(6)]
bricks4 = [pygame.Rect(23 + i*95, 160, 80, 30) for i in range(6)]
bricks5 = [pygame.Rect(23 + i*95, 200, 80, 30) for i in range(6)]
bricks6 = [pygame.Rect(23 + i*95, 240, 80, 30) for i in range(6)]

# this fuction draws text on screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

# making game window
screen_size = (600, 700)
gamewindow = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Brick Breaker by Ehtsham")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# this function draw bricks
def drawBricks(bricks):
    for brick in bricks:
        pygame.draw.rect(gamewindow, pink, brick)

# game specific variables
score = 0
velocity = [8,8]
paddle = pygame.Rect(10, 680, 250, 10)
ball = pygame.Rect(250 , 300, 12, 12)

gameContinue = True

# game loop
pygame.mixer.music.load("brick_song.mp3")
pygame.mixer.music.play(-1)
while gameContinue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameContinue = False
    gamewindow.fill(dark_green)

    drawBricks(bricks1)
    drawBricks(bricks2)
    drawBricks(bricks3)
    drawBricks(bricks4)
    drawBricks(bricks5)
    drawBricks(bricks6)

    pygame.draw.rect(gamewindow, black, paddle)
    pygame.draw.rect(gamewindow, white, ball)
    
    # displaying score on screen
    text_screen(f"Score: {str(score)}", white, 23, 7)
    
    # paddle movement
    if event.type == pygame.KEYDOWN:
        if paddle.x < 350:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_6:
                paddle.x += 20

        if paddle.x > 0:
            if event.key == pygame.K_LEFT or event.key == pygame.K_4:
                paddle.x -= 20

    # ball movement
    ball.x += velocity[0]
    ball.y -= velocity[1]

    if ball.y <= 0:
        velocity[1] = -velocity[1]

    if ball.x <= 0 or ball.x >= 590:
        velocity[0] = -velocity[0]

    # collision detection
    if paddle.collidepoint(ball.x+12, ball.y+12):
        velocity[1] = -velocity[1]

    for brick in bricks1:
        if brick.collidepoint(ball.x, ball.y):
            bricks1.remove(brick)        
            velocity[1] = -velocity[1]
            score += 10

    for brick in bricks2:
        if brick.collidepoint(ball.x, ball.y) :
            bricks2.remove(brick)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score += 10

    for brick in bricks3:
        if brick.collidepoint(ball.x, ball.y):
            bricks3.remove(brick)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score += 10

    for brick in bricks4:
        if brick.collidepoint(ball.x, ball.y):
            bricks4.remove(brick)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score += 10

    for brick in bricks5:
        if brick.collidepoint(ball.x, ball.y):
            bricks5.remove(brick)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score += 10

    for brick in bricks6:
        if brick.collidepoint(ball.x, ball.y):
            bricks6.remove(brick)
            velocity[0] = -velocity[0]
            velocity[1] = -velocity[1]
            score += 10

    if score == 360:
        text_screen("You Won The Game!!!", white, 150, 330)
        pygame.mixer.music.load("Bell Transition.mp3")
        pygame.mixer.music.play()

        pygame.display.update()

        pygame.time.wait(3000)

        break

    if ball.y > 700:
        
        text_screen("Game Over!!!", red, 200, 330)
        pygame.mixer.music.load("game_over.mp3")
        pygame.mixer.music.play()
        
        pygame.display.update()

        pygame.time.wait(3000)

        break

    pygame.display.update()
    clock.tick(60)