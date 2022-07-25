from re import T, X
import pygame
import sys
from random import randint, uniform

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("C:\programming\pygame\Asteroid-Game\graphics\ship.png").convert_alpha()
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
            Laser(self.rect.midtop, laser_group)
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def update(self):
        self.laser_timer()
        self.input_pos()
        self.laser_shoot()

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("C:\programming\pygame\Asteroid-Game\graphics\laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 500
        
    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        self.font = pygame.font.Font("C:\programming\pygame\Asteroid-Game\graphics\subatomic.ttf",)

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("C:\programming\pygame\Asteroid-Game\graphics\meteor.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5),1)
        self.speed = randint(250, 300)
    
    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

class Score:
    def __init__(self):
        self.font = pygame.font.Font("C:\programming\pygame\Asteroid-Game\graphics\subatomic.ttf", 50)
    
    def display(self):
        score_text = f'Score: {pygame.time.get_ticks() // 1000}'
        text_surf = self.font.render(score_text,True,('white'))
        text_rect = text_surf.get_rect(midbottom = (windows_width / 2 , windows_height - 80))
        display.blit(text_surf, text_rect)
        pygame.draw.rect(display, ('white'), text_rect.inflate(30,30), width = 8, border_radius = 5)

# basic setup
pygame.init()
windows_width, windows_height = 1280, 720
display = pygame.display.set_mode((windows_width, windows_height))
pygame.display.set_caption("Asteroid-shoother")
clock = pygame.time.Clock()

# background
background = pygame.image.load("C:/programming/pygame/Asteroid-Game/graphics/background.png").convert()

# sprite group
spaceship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()

# sprites
ship = Ship(spaceship_group)

# timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer,400)

# score
score = Score()

while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == meteor_timer:
            meteor_y_pos = randint(-150, -50)
            meteor_x_pos = randint(-100, windows_width + 100)
            Meteor((meteor_x_pos, meteor_y_pos), meteor_group)

    # delta time
    dt = clock.tick() / 1000
    print(int(clock.get_fps()))

    # background
    display.blit(background, (0,0))

    # update
    spaceship_group.update()
    laser_group.update()
    meteor_group.update()

    # score
    score.display()

    # graphics
    spaceship_group.draw(display)
    laser_group.draw(display)
    meteor_group.draw(display)

    #update the frame
    pygame.display.update()