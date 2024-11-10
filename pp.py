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
        if key_pressed[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 376:
            self.rect.y += self.speed

    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 376:
            self.rect.y += self.speed

win = display.set_mode((1200, 600))
background = transform.scale(image.load('pole.jpg') , (1200, 600))
win.blit(background, (0,0))
display.set_caption('pp.py')

x1 = 157
y1 = 70
x2 = 300
y2 = 300
x3 = 270
y3 = 270

one = Player('1player.png', x1, y1, 10, 38, 200 )
two = Player('2player.png', x3, y3, 15, 350, 700)
#ball = ('vzxbr.png', x2, y2, 10, 20, 20)
clock = time.Clock()

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(background, (0,0))        
    one.update()
    two.update2()
    
    #ball.update()
    one.reset()
    two.reset()

    display.update()
    clock.tick(60)

