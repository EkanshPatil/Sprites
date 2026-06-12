import pygame

WIDTH = 600
HEIGHT = 600
TITLE = "SpritesInPygame"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
rocket_img = pygame.image.load("rocket.png")
space_img = pygame.image.load("space.png")
run = True

class Rocket(pygame.sprite.Sprite):
    def __init__(self,image,x,y,):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
rocket1 = Rocket(rocket_img,300,300)



sprite_group = pygame.sprite.Group()
sprite_group.add(rocket1)

while run == True:
    screen.blit(space_img,(0,0))
    sprite_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_w:
                 rocket1.rect.y -= 10
             if event.key == pygame.K_s:
                  rocket1.rect.y += 10
             if event.key == pygame.K_a:
                 rocket1.rect.x -= 10
             if event.key == pygame.K_d:
                 rocket1.rect.x += 10
    if rocket1.rect.y > 390:
        rocket1.rect.y = 390
    if rocket1.rect.y < 0:
        rocket1.rect.y = 0
    if rocket1.rect.x > 470:
        rocket1.rect.x = 470
    if rocket1.rect.x < 0:
        rocket1.rect.x = 0

    pygame.display.update()
