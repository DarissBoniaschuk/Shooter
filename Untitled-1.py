from pygame import *

class GameSprite(sprite.Sprite):

    def __init__(self, player_image , player_x , player_y, size_x, syze_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(50 , 50)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset (self):
        window.blit(self.image,(self.rect.x , self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed [K_DOWN] and self.rect.y > 5 :
            self.rect.y -= self.speed  

            keys_pressed = key.get_pressed()
        if keys_pressed [K_UP] and self.rect.y < win_width - 80 :
            self.rect.y += self.speed

#задаємо рух для двох тих плиток ну я хз платформ
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed [K_DOWN] and self.rect.y > 5 :
            self.rect.y -= self.speed  

            keys_pressed = key.get_pressed()
        if keys_pressed [K_UP] and self.rect.y < win_width - 80 :
            self.rect.y += self.speed

#background
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-pong Game")
background = transform.scale(image.load("техас.jpg"), (win_width, win_height))
            

#шрифти ы написи
font.init()
font2 = font.Font(None, 36)

#зображення
racket = 