import pygame, sys, random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((360, 640))
pygame.display.set_caption("Flappy Bird with no bird")
clock = pygame.time.Clock()
fps = 60

#Sounds
mixer.music.load('putin_chiquito.mp3')
mixer.music.play(-1)

#Values
tilesize = 30
game_running = False
velocity = 0
gravity = 0.45
piller_change = 3

#Colors
s_blue = (0,181,226)
yellow = (255, 165, 0)
black = (0, 0, 0)
green = (21, 71, 52)
white = (255, 255, 255)

#Font
font = pygame.font.SysFont('Comic Sans', 30)
score = 0

#Game assets
player = pygame.Rect(30, 305, tilesize, tilesize)
enemy_up = pygame.Rect(360, 640 - 200, 45, 200)
enemy_down = pygame.Rect(360, 0, 45, 200)
background = pygame.image.load('night.png')

#Functions
def draw(name, x, y):
    screen.blit(name, (x, y))

print("Backgrounds and the keys")
print("Moonlit night : 'N'")
print("Beach : 'B'")
print("Mountain : 'M'")
print("Parallel World : 'V'")
print("Planets : 'C'")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and game_running == False:
                game_running = True
            if event.key == pygame.K_SPACE:
                velocity = -7.5
                sound = mixer.Sound('laser.wav')
                sound.play()
            if event.key == pygame.K_n:
                background = pygame.image.load('night.png')
            if event.key == pygame.K_b:
                background = pygame.image.load('beach.png')
            if event.key == pygame.K_m:
                background = pygame.image.load('mountain.png')
            if event.key == pygame.K_v:
                background = pygame.image.load('parallel_world.png')
            if event.key == pygame.K_c:
                background = pygame.image.load('space.png')
    if game_running == False:
        draw(background, 0, 0)
        start = font.render("Press Enter to Start", True, white)
        draw(start, 25, 320)   
    else:
        draw(background, 0, 0)
        pygame.draw.rect(screen, yellow, player)
        pygame.draw.rect(screen, green, enemy_down)
        pygame.draw.rect(screen, green, enemy_up)
        score_text = font.render(f"Score : {score}", True, white)
        draw(score_text, 0, 0)
        velocity += gravity
        player.y += velocity
        enemy_up.x -= piller_change
        enemy_down.x -= piller_change
        if enemy_down.x <= -45 and enemy_up.x <= -45:
            enemy_up.x, enemy_down.x = 360, 360
            enemy_up.height, enemy_down.height = random.randint(170, 270), random.randint(170, 270)
            enemy_down.y = 640 - enemy_down.height
            enemy_up.y = 0
            score += 1
        if player.y >= 640 or player.colliderect(enemy_up) or player.colliderect(enemy_down):
            game_over_sound = mixer.Sound('explosion.wav')
            game_over_sound.play()
            piller_change = 0
            gravity = 0
            player.y = 640
            game_over_text = font.render("GAME OVER", True, white)
            final_score = font.render(f"Final score is {score}", True, white)
            draw(game_over_text, 80, 300)
            draw(final_score, 70, 330)
            
    clock.tick(fps)
    pygame.display.update()