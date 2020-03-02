import pygame
import random
from random import sample

pygame.init()

walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

#walkRight[4] = 5번째 사진??? 0번째가 첫번째다!!!

screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("MANhattan game project")
surface = pygame.image.load('Game/R1.png')
pygame.display.set_icon(surface)

#python = object oriented (객체 지향)
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.left = False
        self.right = False
        self.walkCount = 0 #standing 
        self.isJump = False
        self.jumpCount = 5
        self.standing = True

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount//3],(self.x, self.y)) # //3 -> 나머지 값을 제외 한 몫
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount += 1 
        else: #if man is standing still
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            else:#if left
                screen.blit(walkLeft[0], (self.x, self.y))

class projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing #Facing must be -1 or 1
        self.vel = 25 * facing #8 * -1 = -8 (Left)
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        #tuple = list랑 비슷하지만 숫자를 변경 할 수 있는 놈

def drawGameWindow(): #캐릭터가 움직일때마다 모션 표현
    screen.blit(bg,(0,0)) # 내뒤에 있는 사진 지우기용
    man.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()



clock = pygame.time.Clock()
run = True
man = player(50, 400, 64, 64)#main character
bullets = [] #각각의 총알의 명령문을 저장 => 총알이 몇알이 나가는지를 세어주는 역할
#instance


while run:
    clock.tick(27) # 27 frames

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x < 600 and bullet.x > 0: #벽을 뚫지 않게
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet)) #[0 . 3 4 8 9] #501 픽셀로 가버리면 불릿을 없애버리는 코드
            #현재의 불릿 인덱스*(위치)를 찾아서 지움

    pressed = pygame.key.get_pressed()
    ##작은 칸을 넘어가야함. 50 < x < 66 
    if pressed[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 1 :
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

    if pressed[pygame.K_LEFT] and man.x > man.velocity: 
        man.x -= man.velocity
        man.left = True
        man.right = False # left일때 오른쪽 키를 누르면 절대 안되기 때문
        man.standing = False
        
    elif pressed[pygame.K_RIGHT] and man.x < 500 - man.width - 5: 
        man.x += man.velocity
        man.right = True
        man.left= False
        man.standing = False
    
    else: # If jus standing
        man.standing = True
        man.walkCount = 0

    if pressed[pygame.K_w]:
        man.x = 500
        man.y = 999
########## 캐릭터의 점프 ###########
    if not (man.isJump): 
        if pressed[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.standing = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -5:  
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5
            man.jumpCount -= 1
        else:
            man.jumpCount = 5
            man.isJump = False
    
    # movement = random.sample(range(1,2), 1)
    # if movement == 1:
    #     x += velocity
    #     right = True
    #     left = False
    # if movement == 2:
    #     x -= velocity
    #     right = False
    #     left = True
####################################
    drawGameWindow()
    
pygame.quit()