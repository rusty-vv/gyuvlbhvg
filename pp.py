from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image) , (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_DOWN] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_UP] and self.rect.y < 635:
            self.rect.y += self.speed

win = display.set_mode((1800, 900))
background = transform.scale(image.load('поле пп.jpg') , (1800, 900))
win.blit(background, (0,0))
display.set_caption('пинг понг ру')

x1 = 
y1 = 
x2 = 500
y2 = 500
x3 = 
y3 = 

one = Player('rocket.png', x1, y1, 10, 80, 100 )
two = Player('bullet.png', x3, y3, 15, 20, 20)
ball = ('vzxbr.png', x2, y2, 10, 20, 20)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
   
    display.update()
    clock.tick(60)
