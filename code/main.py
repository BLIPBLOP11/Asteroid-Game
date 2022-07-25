import pygame
import sys

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("C:\programming\pygame\First game\graphics\ship.png").convert_alpha()
        self.rect = self.image.get_rect(center = (windows_width / 2, windows_height / 2))

        # timer
        self.can_shoot = True
        self.shoot_time = False

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True

    def input_pos(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def laser_shoot(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            print("shooting laser")
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def update(self):
        self.laser_timer()
        self.input_pos()
        self.laser_shoot()

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("C:\programming\pygame\First game\graphics\laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)

# basic setup
pygame.init()
windows_width, windows_height = 1280, 720
display = pygame.display.set_mode((windows_width, windows_height))
pygame.display.set_caption("brooooooooooooooooooooooo")
clock = pygame.time.Clock()

# background
background = pygame.image.load("C:/programming/pygame/First game/graphics/background.png").convert()

# sprite group
spaceship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()

# sprites
ship = Ship(spaceship_group)
laser = Laser((100, 300),laser_group)

while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time
    dt = clock.tick() / 1000

    # background
    display.blit(background, (0,0))

    # update
    spaceship_group.update()

    # graphics
    spaceship_group.draw(display)
    laser_group.draw(display)

    #update the frame
    pygame.display.update()