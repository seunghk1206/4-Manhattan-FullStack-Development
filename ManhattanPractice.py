import pygame

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
        self.walkCount = 0
        self.isJump = False
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17 , self.y + 11, 28, 60)

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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(screen, (255,255,255), self.hitbox, 2)

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

class enemy():
    walkRight = [pygame.image.load('Game/R1E.png'), pygame.image.load('Game/R2E.png'), pygame.image.load('Game/R3E.png'), pygame.image.load('Game/R4E.png'), pygame.image.load('Game/R5E.png'), pygame.image.load('Game/R6E.png'), pygame.image.load('Game/R7E.png'), pygame.image.load('Game/R8E.png'), pygame.image.load('Game/R9E.png'), pygame.image.load('Game/R10E.png'), pygame.image.load('Game/R11E.png')]
    walkLeft = [pygame.image.load('Game/L1E.png'), pygame.image.load('Game/L2E.png'), pygame.image.load('Game/L3E.png'), pygame.image.load('Game/L4E.png'), pygame.image.load('Game/L5E.png'), pygame.image.load('Game/L6E.png'), pygame.image.load('Game/L7E.png'), pygame.image.load('Game/L8E.png'), pygame.image.load('Game/L9E.png'), pygame.image.load('Game/L10E.png'), pygame.image.load('Game/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 3
        self.path = [self.x, self.end] # path = x -----> END 
        self.hitbox = (self.x + 13, self.y + 2, 31, 57)
        self.i = 0

    def draw(self, screen):
        self.move()
        if self.walkCount + 1 >= 33: #33프레임이 넘어가면  -> 사진이 끝까지 왔다는 뜻 
            self.walkCount = 0
        if self.vel > 0: #오른쪽으로 갈때,
            screen.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.vel < 0: #왼쪽으로
            screen.blit(self.walkLeft[self.walkCount//3],(self.x, self.y)) # //3 -> 나머지 값을 제외 한 몫 
            self.walkCount += 1
        self.hitbox = (self.x + 13, self.y + 2, 31, 57) #draw hitbox 
        pygame.draw.rect(screen, (255,255,255), self.hitbox, 2)

    def move(self):
        if self.vel > 0:#vel = 3, x = 30
            if self.x < self.path[1] + self.vel: #path = 450
                self.x += self.vel #오른쪽으로 이동
            else:
                self.vel = self.vel * -1 #와리가리 해야할 구간을 넘어버릴때 왼쪽으로 보내버려라.
                self.x += self.vel
                self.walkCount = 0
        else: #when vel is negative
            if self.x > self.path[0] - self.vel: #path = 초기 x 값
                self.x += self.vel #왼쪽으로 이동
            else:
                self.vel = self.vel * -1 #와리가리 해야할 구간을 넘어버릴때 오른쪽으로 보내버려라.
                self.x += self.vel
                self.walkCount = 0
    def hit(self):
        self.i = self.i + 1
        print("killed goblin: ", self.i)





def drawGameWindow(): #캐릭터가 움직일때마다 모션 표현
    screen.blit(bg,(0,0)) # 내뒤에 있는 사진 지우기용
    man.draw(screen)
    goblin.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()



clock = pygame.time.Clock()
run = True
man = player(50, 400, 64, 64)#main character
goblin = enemy(100, 410, 64, 64, 550)
bullets = [] #각각의 총알의 명령문을 저장 => 총알이 몇알이 나가는지를 세어주는 역할
#instance


while run:
    clock.tick(27) # 27 frames

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius >goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))
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
        if man.jumpCount >= -10:  
            man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5
            man.jumpCount -= 1
        else:
            man.jumpCount = 10
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