#Создай собственный Шутер!
from random import *
from pygame import *
#создай окно игры
window = display.set_mode((700,500))
display.set_caption("Шутер")
background=transform.scale(image.load("galaxy.jpg"),(700,700))
clock=time.Clock()
FPS=60
win_widht=700
win_height=500
mixer.init()
mixer.music.load("space.ogg")
kick_fire=mixer.Sound("fire.ogg")     
mixer.music.play()
font.init()
font1= font.SysFont("Arial",36)
font3=font.SysFont("Arial",100)
run=True
finish=False
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(size_x,size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x< win_widht - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet=Bullet("bullet.png",self.rect.centerx,self.rect.top,-15,15,20)
        bullet.add(Bullets)

        
lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.x = randint(80,700)
            self.rect.y = 0
            lost += 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <0:
            self.kill()
Bullets=sprite.Group()

        
monsters = sprite.Group()
for i in range(1,6):
    monster=Enemy("ufo.png",randint(80,630),0,randint(1,5),80,50)
    monsters.add(monster)
rocket=Player("rocket.png",400,400,10,80,100)


score=0
lose=font3.render("YOU LOSE",1,(255,3,3))
win=font3.render("YOU WIN",1,(18,255,18))
while run != False:
    clock.tick(FPS)
    for e in event.get():
        if e.type==QUIT:
            run=False
        elif e.type== KEYDOWN:
            if e.key== K_SPACE:
                rocket.fire()
                kick_fire.play()
    collides=sprite.groupcollide(monsters,Bullets,True,True)
    if not finish:          
        window.blit(background,(0,0))
        text_lose=font1.render("Пропущено: " + str(lost),1,(255,255,255))
        text=font1.render("Cчет: " + str(score),1,(255,255,255))
        window.blit(text_lose,(10,50))
        window.blit(text,(10,25))
        monsters.draw(window)
        monsters.update()
        rocket.reset()
        rocket.update()
        clock.tick(FPS)
        Bullets.update()
        Bullets.draw(window)
        for c in collides:
            score += 1
            monster=Enemy("ufo.png",randint(80,630),0,randint(1,5),80,50)
            monsters.add(monster)
        if sprite.spritecollide(rocket,monsters,False) or lost > 3:
            finish=True
            window.blit(lose,(200,200)) 
        if score >= 10:
            finish=True 
            window.blit(win,(200,200)) 
        display.update()
    
  
  
