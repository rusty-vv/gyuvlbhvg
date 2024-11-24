from pygame import *
number = 0
table = 0
wasd = input('Привет игрок 1! Как мне называть тебя?')
dsaw = input('Привет игрок 2! А как тебя мне называть?')

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
class Boll(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x, player_speed_y, size_x, size_y):
        self.image = transform.scale(image.load(player_image) , (size_x, size_y))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def update(self):
        global table
        global number
        if sprite.collide_rect(self, one):
            self.speed_x *= -1
        if sprite.collide_rect(self, two):
            self.speed_x *= -1
        if self.rect.y <=0:
            self.speed_y *= -1
        if self.rect.y >= 550:
            self.speed_y *= -1
        self.rect.x += self.speed_x     
        self.rect.y += self.speed_y
        if self.rect.x <=0:
            self.rect.x = 575
            self.rect.y = 260
            table += 1
        if self.rect.x >=1150:
            self.rect.x = 576
            self.rect.y = 262
            number += 1

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


win = display.set_mode((1200, 600))
background = transform.scale(image.load('pole.jpg') , (1200, 600))
win.blit(background, (0,0))
display.set_caption('pp.py')

font.init()
font = font.SysFont('Arial', 35)
play1er = font.render(f'{wasd}: ', True, (255, 255, 255))
play2er = font.render(f'{dsaw}: ', True, (255, 255, 255))
fdg = font.render('первый игрок одержал победу!', True, (255,255,255))
winn = font.render('второй игрок одержал победу!', True, (255,255,255))

x1 = 157
y1 = 70
x2 = 300
y2 = 300
x3 = 1013
y3 = 70

one = Player('1player.png', x1, y1, 15, 38, 200 )
two = Player('2player.png', x3, y3, 15, 38, 194)
ball = Boll('vzxbr.png', x2, y2, 10, 10, 50, 50)
clock = time.Clock()

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        win.blit(background, (0,0))  
        play1er = font.render(f'{wasd}: {str(number)}', True, (125, 232, 143))
        play2er = font.render(f'{dsaw}: {str(table)}', True, (125, 232, 143))
        win.blit(play1er, (198, 50))
        win.blit(play2er, (764, 50))
        one.update()
        two.update2()
        ball.update()

        one.reset()
        two.reset()
        ball.reset()
        if number >=3:
            finish = True
            win.blit(fdg, (370, 522))
        if table >=3:
            finish = True
            win.blit(winn, (370, 522))


    display.update()
    clock.tick(60)

