from pygame import*
okno = display.set_mode((500,500))
game = True
clock = time.Clock()
fom = transform.scale(image.load('images.jpg'),(500,500))
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
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
