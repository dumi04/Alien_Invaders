import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((1024, 800))

# Background
background = pygame.image.load('background.jpg')

# Title and Icon
pygame.display.set_caption("2D-Game")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('spaceship.png')
playerX = 450
playerY = 700
playerX_change = 0

# Enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 20

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 963))
    enemyY.append(random.randint(10, 250))
    enemyX_change.append(4)
    enemyY_change.append(50)

# Bullet
# ready state = cant see the bullet
# fire state = the bullet is moving
bulletimg = []
bulletX = []
bulletY = []
bulletX_change = []
bulletY_change = []
bullet_state = []
num_of_bullets = 3

for i in range(num_of_bullets):
    bulletimg.append(pygame.image.load('bullet.png'))
    bulletX.append(0)
    bulletY.append(700)
    bulletX_change.append(0)
    bulletY_change.append(20)
    bullet_state.append("ready")

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (350, 400))


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def firebullet(x, y, i):
    global bullet_state
    bullet_state[i] = "fire"
    screen.blit(bulletimg[i], (x + 16, y + 10))


def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether it's left or right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerX_change = -4
        if keys[pygame.K_RIGHT]:
            playerX_change = 4
        if keys[pygame.K_SPACE]:
            for i in range(num_of_bullets):
                if bullet_state[i] == "ready":
                    bulletX[i] = playerX
                    firebullet(bulletX[i], bulletY[i], i)

        if event.type == pygame.KEYUP and (
                event.key == pygame.K_LEFT or pygame.K_RIGHT) and event.key != pygame.K_SPACE:
            playerX_change = 0

    playerX += playerX_change

    if playerX < 0:
        playerX = 0
    if playerX > 963:
        playerX = 963

    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 690:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] < 0:
            enemyX[i] = 0
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        if enemyX[i] > 963:
            enemyX[i] = 963
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
            # Collision
        for num in range(num_of_bullets):
            col = collision(enemyX[i], enemyY[i], bulletX[num], bulletY[num])
            if col:
                bulletY[num] = 700
                bullet_state[num] = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 963)
                enemyY[i] = random.randint(10, 250)
            enemy(enemyX[i], enemyY[i], i)
    # Bullet movement
    for num in range(num_of_bullets):
        if bulletY[num] <= 0:
            bulletY[num] = 700
            bullet_state[num] = "ready"

        if bullet_state[num] == "fire":
            firebullet(bulletX[num], bulletY[num], num)
            bulletY[num] -= bulletY_change[num]

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
