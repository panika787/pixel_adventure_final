from pygame import *
from random import * 
font.init()

display.set_caption('Pixel Adventure')

clock = time.Clock()
FPS = 30
score = 0

finish = False
onGround = False
gravity = True
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            window.blit(walk_left[player_anim_count], (self.rect.topleft, self.rect.topleft))
        elif keys[K_RIGHT] and self.rect.x < 700 - 0:
            self.rect.x += self.speed
            window.blit(walk_right[player_anim_count], (ship.rect.x, ship.rect.y))
        else:
            window.blit(self.image, (self.rect.x, self.rect.y))
    def fail(self):
        if gravity == True:
            self.rect.y += self.speed
    def enemies(self):
        if self.rect.x <= 500:
            self.direction = "right"
        if self.rect.x >= 850:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
   def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       super().__init__()
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height
       # картинка стены - прямоугольник нужных размеров и цвета
       self.image = Surface((self.width, self.height))
       self.image.fill((color_1, color_2, color_3))
       # каждый спрайт должен хранить свойство rect - прямоугольник
       self.rect = self.image.get_rect()
       self.rect.x = wall_x
       self.rect.y = wall_y
   def draw_wall(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Unit():
    def __init__(self):
        self.last = pygame.time.get_ticks()
        self.cooldown = 300


#класс главного игрока
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
            window.blit(walk_left[player_anim_count], (self.rect.topleft, self.rect.topleft))
        elif keys[K_d] and self.rect.x < 1294 - 70:
            self.rect.x += self.speed
            window.blit(walk_right[player_anim_count], (ship.rect.x, ship.rect.y))
        elif keys[K_SPACE]:
            if onGround == True:
                gravity = False
                for i in range(20):
                    self.rect.y -= 7
                    window.blit(jump[player_anim_jump], (self.rect.x, self.rect.y))
                gravity = True
        else:
            window.blit(idle_player[player_anim_idle], (self.rect.x, self.rect.y))


window = display.set_mode((1294,700))
background = transform.scale(image.load('level1.png'),(1294,700))
background2 = transform.scale(image.load('level2.png'),(1294,700))
ship = Player("idle_1.png", 90, 300, 70, 70, 10)
trap1 = GameSprite("Off.png", 415, 370, 63, 25, 4)
trap2 = GameSprite("Off.png", 570, 395, 63, 25, 4)
trap3 = GameSprite("Off.png", 727, 365, 63, 25, 4)
trap4 = GameSprite("Off.png", 864, 354, 63, 25, 4)
apple = GameSprite("Apple.png", 580, 350, 33, 42, 4)
cherries = GameSprite("Cherries.png", 740, 320, 33, 50, 4)
pineapple = GameSprite("Pineapple.png", 870, 310, 33, 42, 4)
strawberry = GameSprite("Strawberry.png", 428, 315, 33, 42, 4)  
melon = GameSprite("Melon.png", 576, 505, 54, 36, 4)
kiwi = GameSprite("Kiwi.png", 698, 505, 42, 42, 4)
orange = GameSprite("Orange.png", 800, 505, 54, 42, 4)
brown = GameSprite("Brown.png", 500, 545, 96, 24, 9)
game = True
game2 = True
idle_player = [
    transform.scale(image.load('idle_1.png'),(70,70)),
    transform.scale(image.load('idle_1.png'),(70,70)),
    transform.scale(image.load('idle_2.png'),(70,70)),
    transform.scale(image.load('idle_2.png'),(70,70)),
    transform.scale(image.load('idle_3.png'),(70,70)),
    transform.scale(image.load('idle_3.png'),(70,70)),
    transform.scale(image.load('idle_4.png'),(70,70)),
    transform.scale(image.load('idle_4.png'),(70,70)),
    transform.scale(image.load('idle_5.png'),(70,70)),
    transform.scale(image.load('idle_5.png'),(70,70)),
    transform.scale(image.load('idle_6.png'),(70,70)),
    transform.scale(image.load('idle_6.png'),(70,70)),
    transform.scale(image.load('idle_7.png'),(70,70)),
    transform.scale(image.load('idle_7.png'),(70,70)),
    transform.scale(image.load('idle_8.png'),(70,70)),
    transform.scale(image.load('idle_8.png'),(70,70)),
]

walk_left = [
    transform.scale(image.load('Run_left_1.png'),(70,70)),
    transform.scale(image.load('Run_left_1.png'),(70,70)),    
    transform.scale(image.load('Run_left_2.png'),(70,70)),
    transform.scale(image.load('Run_left_3.png'),(70,70)),
    transform.scale(image.load('Run_left_3.png'),(70,70)),
    transform.scale(image.load('Run_left_4.png'),(70,70)),
    transform.scale(image.load('Run_left_5.png'),(70,70)),
    transform.scale(image.load('Run_left_5.png'),(70,70)),
    transform.scale(image.load('Run_left_6.png'),(70,70)),
    transform.scale(image.load('Run_left_7.png'),(70,70)),
    transform.scale(image.load('Run_left_7.png'),(70,70)),
    transform.scale(image.load('Run_left_8.png'),(70,70)),
    transform.scale(image.load('Run_left_9.png'),(70,70)),
    transform.scale(image.load('Run_left_9.png'),(70,70)),
    transform.scale(image.load('Run_left_10.png'),(70,70)),
    transform.scale(image.load('Run_left_11.png'),(70,70)),   
    transform.scale(image.load('Run_left_11.png'),(70,70)),
    transform.scale(image.load('Run_left_12.png'),(70,70))
]
walk_right = [
    transform.scale(image.load('Run_right_1.png'),(70,70)),
    transform.scale(image.load('Run_right_1.png'),(70,70)),    
    transform.scale(image.load('Run_right_2.png'),(70,70)),
    transform.scale(image.load('Run_right_3.png'),(70,70)),
    transform.scale(image.load('Run_right_3.png'),(70,70)), 
    transform.scale(image.load('Run_right_4.png'),(70,70)),
    transform.scale(image.load('Run_right_5.png'),(70,70)),
    transform.scale(image.load('Run_right_5.png'),(70,70)),
    transform.scale(image.load('Run_right_6.png'),(70,70)),
    transform.scale(image.load('Run_right_7.png'),(70,70)),
    transform.scale(image.load('Run_right_7.png'),(70,70)),
    transform.scale(image.load('Run_right_8.png'),(70,70)),
    transform.scale(image.load('Run_right_9.png'),(70,70)),
    transform.scale(image.load('Run_right_9.png'),(70,70)),
    transform.scale(image.load('Run_right_10.png'),(70,70)),
    transform.scale(image.load('Run_right_11.png'),(70,70)),  
    transform.scale(image.load('Run_right_11.png'),(70,70)),
    transform.scale(image.load('Run_right_12.png'),(70,70))
]

jump = [
    transform.scale(image.load('Double_Jump_1.png'),(70,70)),
    transform.scale(image.load('Double_Jump_2.png'),(70,70)),
    transform.scale(image.load('Double_Jump_3.png'),(70,70)),
    transform.scale(image.load('Double_Jump_4.png'),(70,70)),
    transform.scale(image.load('Double_Jump_5.png'),(70,70)),
    transform.scale(image.load('Double_Jump_6.png'),(70,70))
]

player_anim_idle = 0
player_anim_jump = 0
player_anim_count = 0

mixer.init()
mixer.music.load('Midnight-Motorist-—-FNaF-6-OST-_www.lightaudio.ru_.ogg')
mixer.music.play()

floor1 = Wall(213, 204, 158, 44, 385, 150, 0 )
floor2 = Wall(213, 204, 158, 245, 427, 60, 0 )
floor3 = Wall(213, 204, 158, 248, 555, 70, 0 )
floor4 = Wall(213, 204, 158, 330, 597, 80, 0 )
floor5 = Wall(213, 204, 158, 33, 639, 2000, 0 )
floor6 = Wall(213, 204, 158, 833, 590, 100, 0 )
floor7 = Wall(213, 204, 158, 958, 555, 100, 0 )
floor8 = Wall(213, 204, 158, 1038, 485, 30, 0 )
floor9 = Wall(213, 204, 158, 1015, 375, 30, 0 )
floor10 = Wall(213, 204, 158, 1083, 282, 1000, 0 )
floor11 = Wall(213, 204, 158, 1205, 251, 30, 0 )

floor20 = Wall(213, 204, 158, 27, 543, 430, 0 )
floor21 = Wall(213, 204, 158, 434, 630, 120, 0 )
floor22 = Wall(213, 204, 158, 33, 675, 2000, 0 )
floor23 = Wall(213, 204, 158, 907, 587, 70, 0 )
floor24 = Wall(213, 204, 158, 959, 454, 200, 0 )


portal = Wall(213, 203, 158, 1241, 59, 0, 250)
font1 = font.Font('PublicPixel-z84yD.ttf',36)




while game:
    window.blit(background,(0,0))  
    floor1.draw_wall()
    floor2.draw_wall()
    floor3.draw_wall()
    floor4.draw_wall()
    floor5.draw_wall()
    floor6.draw_wall()
    floor7.draw_wall()
    floor8.draw_wall()
    floor9.draw_wall()
    floor10.draw_wall()
    floor11.draw_wall()
    portal.draw_wall()



    keys = key.get_pressed()
    
    if player_anim_count == 15:
        player_anim_count = 0
    else:
        player_anim_count += 1   
    
    if player_anim_idle == 14:
        player_anim_idle = 0
    else:
        player_anim_idle += 1   

    if player_anim_jump == 5:
        player_anim_jump = 0
    else:
        player_anim_jump += 1 


    if sprite.collide_rect(ship, floor1):
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, floor2):
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, floor3):
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, floor4):
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, floor5):
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, floor6):
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, floor7):
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, floor8):
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, floor9):
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, floor10):
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, floor11):
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, trap1):
        for i in range(1):
            trap1.rect.y += 10
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, trap2):
        for i in range(1):
            trap2.rect.y += 10
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, trap3):
        for i in range(1):
            trap3.rect.y += 10
        gravity = False
        onGround = True
    elif sprite.collide_rect(ship, trap4):
        for i in range(1):
            trap4.rect.y += 10
        gravity = False
        onGround = True
    else:
        onGround = False
        gravity = True    
   
    popal = font1.render("собрано:" + str(score), 1, (255, 255, 255))
    window.blit(popal,(160,50))
    if sprite.collide_rect(ship, strawberry):
        score = score + 1
        strawberry.rect.x += 1000
    if sprite.collide_rect(ship, cherries):
        score = score + 1
        cherries.rect.x += 1000
    if sprite.collide_rect(ship, pineapple):
        score = score + 1
        pineapple.rect.x += 1000
    if sprite.collide_rect(ship, apple):
        score = score + 1
        apple.rect.x += 1000




    apple.update()
    pineapple.update()
    cherries.update()
    strawberry.update()
    trap1.update()
    trap2.update()
    trap3.update()
    trap4.update()
    
    

    for e in event.get():
            if e.type == QUIT:
                game = False
    if sprite.collide_rect(ship, portal):

        score == 30
        finish = True
        while game2:
            window.blit(background2,(0,0))
            
        

            
            keys = key.get_pressed()
    
            if player_anim_count == 15:
                player_anim_count = 0
            else:
                player_anim_count += 1   
            
            if player_anim_idle == 14:
                player_anim_idle = 0
            else:
                player_anim_idle += 1   

            if player_anim_jump == 5:
                player_anim_jump = 0
            else:
                player_anim_jump += 1 
            if sprite.collide_rect(ship, floor20):
                gravity = False
                onGround = True
            elif sprite.collide_rect(ship, floor21):
                gravity = False
                onGround = True
            elif sprite.collide_rect(ship, floor22):
                gravity = False
                onGround = True
            elif sprite.collide_rect(ship, floor23):
                gravity = False
                onGround = True
            elif sprite.collide_rect(ship, floor24):
                gravity = False
                onGround = True
            else:
                onGround = False
                gravity = True
            popal = font1.render("собрано:" + str(score), 1, (255, 255, 255))
            window.blit(popal,(160,50))        

            floor20.draw_wall()
            floor21.draw_wall()
            floor22.draw_wall()
            floor23.draw_wall()
            floor24.draw_wall()


            if sprite.collide_rect(ship, brown):          
                gravity = False
                onGround = True
            elif sprite.collide_rect(ship,floor20):
                gravity = False
                onGround = True
            elif sprite.collide_rect(ship,floor21):
                gravity = False
                onGround = True
            elif sprite.collide_rect(ship,floor22):
                gravity = False
                onGround = True
            elif sprite.collide_rect(ship,floor23):
                gravity = False
                onGround = True
            elif sprite.collide_rect(ship,floor24):
                gravity = False
                onGround = True            
            else:
                onGround = False
                gravity = True  

            if sprite.collide_rect(ship, melon):
                score = score + 1
                melon.rect.x += 1000
            if sprite.collide_rect(ship, orange):
                score = score + 1
                orange.rect.x += 1000
            if sprite.collide_rect(ship, kiwi):
                score = score + 1
                kiwi.rect.x += 1000

            kiwi.update()
            orange.update()    
            melon.update()
            brown.enemies()
            brown.update()
            ship.update()   
            ship.fail()
            clock.tick(FPS)
            display.update()
            
            
            for e in event.get():
                    if e.type == QUIT:
                        game = False
                        game2 = False
            
            
    ship.update()   
    ship.fail()
    clock.tick(FPS)
    display.update()






