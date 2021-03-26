import pygame
import random
import os

WIDTH = 800
HIEGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0,0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "Gaming_Pictures")
print(img_folder)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HIEGHT / 2)
        self.y_speed = 5

    def update(self):

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_RIGHT]:
            self.rect.x += 5
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 5
        if keystate[pygame.K_UP]:
            self.rect.y -= 5
        if keystate[pygame.K_DOWN]:
            self.rect.y += 5
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HIEGHT))
pygame.display.set_caption("Gaming as a Gamer!")

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLUE)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
