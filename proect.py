from pygame import*
okno = display.set_mode((500,500))
game = True
clock = time.Clock()
fom = transform.scale(image.load('фон.jpg'),(500,500))
class gameobject(sprite.Sprite):
    def __init__(self,pict,x,y):
        super().__init__()
        self.image = transform.scale(image.load(pict),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lastx = self.rect.x
        self.lasty = self.rect.y
    def ris(self):
        okno.blit(self.image,(self.rect.x,self.rect.y))

class player(gameobject):
    def control(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_LEFT]:
            self.lastx = self.rect.x
            self.rect.x -= 6
        if kn[K_RIGHT]:
            self.lastx = self.rect.x
            self.rect.x += 6
        if kn[K_UP]:
            self.lasty = self.rect.y
            self.rect.y -= 6
        if kn[K_DOWN]:
            self.lasty = self.rect.y
            self.rect.y += 6

geroi = player('god.jpg', 100,100)
class Wall(sprite.Sprite):
    def __init__(self,x,y, shir,vis):
        super().__init__()
        self.image = Surface((shir,vis))
        self.image.fill((200,150,0)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image,(self.rect.x,self.rect.y))

stena = [Wall(250,100,100,50), Wall(200,190,190,50), Wall(100,250,100,100), Wall(300,250,130,50),  Wall(200,500,100,50)]

lose = False
win = False

font.init()
wr = font.Font(None, 30)

points = 0
hp = 100

from random import*
nagrada = []

for i in range(10):
    x1 = randint(0,10) * 45 + 10
    y1 = randint(0,10) * 45 + 10
    priz = gameobject('golds.jpg',x1,y1)
    nagrada.append(priz) 

while game:
    okno.blit(fom,(0,0))
    textpoints = wr.render(str(points), True, (0,255,0))
    okno.blit(textpoints,(20,30))
    heal = wr.render(str(hp), True, (255,0,0))
    okno.blit(heal,(40,50))
    for pr in nagrada:
        pr.ris()
    for i in event.get():
        if i.type == QUIT:
            game = False
    geroi.control()
    for i in stena:
        i.ris()
        if sprite.collide_rect(geroi,i):
            geroi.rect.x = geroi.lastx
            geroi.rect.y = geroi.lasty
    display.update()
    clock.tick(60)
