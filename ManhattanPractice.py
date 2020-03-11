import pygame
pygame.init()

walkRight = [pygame.image.load('MainChara_R/R1.png'), pygame.image.load('MainChara_R/R2.png'), pygame.image.load('MainChara_R/R3.png')]#, pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('MainChara_R/L1.png'), pygame.image.load('MainChara_R/L2.png'), pygame.image.load('MainChara_R/L3.png')]#, pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
bg2 = pygame.image.load('bg_map/bg2.png')
#dungeon = pygame.image.load('')
char = pygame.image.load('MainChara_R/standing.png')
score = 0 # Tuple -> list
#walkRight[4] = 5번째 사진??? 0번째가 첫번째다!!!

screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption("MANhattan game project")
icon = pygame.image.load('MainChara_R/R1.png')
pygame.display.set_icon(icon)

bulletSound = pygame.mixer.Sound('SoundEff/bullet.wav')
hitSound = pygame.mixer.Sound('SoundEff/hit.wav')
music = pygame.mixer.music.load('SoundEff/gameBGM.mp3')
pygame.mixer.music.play(-1)

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
        if self.walkCount + 1 >= 9:
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
        self.hitbox = (self.x + 17, self.y + 11, 29, 52) #x, y, width, height
        #x-axis = man.hitbox[0]
        #y-axis = man.hitbox[1]
        #width = man.hitbox[2]
        #height = man.hitbox[3]
        #pygame.draw.rect(screen, (255,255,255), self.hitbox, 2)

    def hit(self):##if hit function operates, must initialize the position
        self.jumpCount = 10
        self.isJump = False
        self.x = 50
        self.y = 400
        self.walkCount = 0#####################################
        #죽었다고 나오는 메세지 출력
        msg = pygame.font.SysFont('comicsans', 100)
        text = msg.render('Dead',1, (255,0,0))############################
        screen.blit(text, (300 - (text.get_width()/2), 200)) #메세지 출력
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i = i + 1
            for eachEvent in pygame.event.get(): 
                if eachEvent.type == pygame.QUIT:
                    pygame.quit()
        ############################


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

class portal():
    dungeonPortal = [pygame.image.load('door/door_m.png'), pygame.image.load('door/door_n.png')]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, screen):
        if beginning == 1: # 1st stage
            screen.blit(self.dungeonPortal[0], (self.x, self.y))
        elif second == 1: # 2nd stage
            screen.blit(self.dungeonPortal[1], (self.x, self.y))

class enemy():
    walkRight = [pygame.image.load('Game/R1E.png'), pygame.image.load('Game/R2E.png'), pygame.image.load('Game/R3E.png'), pygame.image.load('Game/R4E.png'), pygame.image.load('Game/R5E.png'), pygame.image.load('Game/R6E.png'), pygame.image.load('Game/R7E.png'), pygame.image.load('Game/R8E.png'), pygame.image.load('Game/R9E.png'), pygame.image.load('Game/R10E.png'), pygame.image.load('Game/R11E.png')]
    walkLeft = [pygame.image.load('Game/L1E.png'), pygame.image.load('Game/L2E.png'), pygame.image.load('Game/L3E.png'), pygame.image.load('Game/L4E.png'), pygame.image.load('Game/L5E.png'), pygame.image.load('Game/L6E.png'), pygame.image.load('Game/L7E.png'), pygame.image.load('Game/L8E.png'), pygame.image.load('Game/L9E.png'), pygame.image.load('Game/L10E.png'), pygame.image.load('Game/L11E.png')]
    walkRight2 = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
    walkLeft2 = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
    
    def __init__(self, x, y, width, height, end, vel, health, maxHP):
        self.visible = True
        if self.visible:
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.walkCount = 0
            self.vel = vel
            self.path = [self.x, self.end] # path = x -----> END 
            self.hitbox = (self.x + 13, self.y + 2, 31, 57)
            self.score = 0
            self.health = health #Remove health bar and enemy when the it is dead
            self.maxHP = maxHP

    def draw(self, screen):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33: #33프레임이 넘어가면  -> 사진이 끝까지 왔다는 뜻 
                self.walkCount = 0
            if self.vel > 0: #오른쪽으로 갈때,
                screen.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.vel < 0: #왼쪽으로
                screen.blit(self.walkLeft[self.walkCount//3],(self.x, self.y)) # //3 -> 나머지 값을 제외 한 몫 
                self.walkCount += 1
            self.hitbox = (self.x + 13, self.y + 2, 31, 57) #draw hitbox 
            pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) #Red is background color
            pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/self.maxHP)*(self.maxHP - self.health)), 10))
            #pygame.draw.rect(screen, (255,255,255), self.hitbox, 2) self.move()
    
    def draw2(self, screen):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 27: #33프레임이 넘어가면  -> 사진이 끝까지 왔다는 뜻 
                self.walkCount = 0
            if self.vel > 0: #오른쪽으로 갈때,
                screen.blit(self.walkRight2[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.vel < 0: #왼쪽으로
                screen.blit(self.walkLeft2[self.walkCount//3],(self.x, self.y)) # //3 -> 나머지 값을 제외 한 몫 
                self.walkCount += 1
            self.hitbox = (self.x + 13, self.y + 2, 31, 57) #draw hitbox 
            pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)) #Red is background color
            pygame.draw.rect(screen, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/self.maxHP)*(self.maxHP - self.health)), 10))
    

    def move(self):
        if self.visible:
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
        if self.visible:
            hitSound.play()
            if self.health > 0:
                self.health = self.health - 1
            else:
                self.visible = False
        
clock = pygame.time.Clock()
beginning = 1 # 1 = true
second = 0 #0 = false, do not start stage two yet

man = player(50, 400, 64, 64)#main character
goblin = enemy(100, 410, 64, 64, 550, 5, 10, 10) #goblin = class를 가진 instance. 
boss = enemy(80, 410, 64, 64, 550, 7, 20, 20)

n_door = portal(500, 400, 64, 27)
m_door = portal(500, 400, 64, 27)

bullets = [] #각각의 총알의 명령문을 저장 => 총알이 몇알이 나가는지를 세어주는 역할
font = pygame.font.SysFont('cosmicsans', 30, True)
#instance

def drawGameWindow(): #캐릭터가 움직일때마다 모션 표현
    screen.blit(bg,(0,0)) # 내뒤에 있는 사진 지우기용
    text = font.render('Score: ' + str(score), 2, (0,0,0)) # font 설정!
    screen.blit(text, (450, 10))
    m_door.draw(screen)
    man.draw(screen)
    goblin.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()

def drawGameWindow2(): #캐릭터가 움직일때마다 모션 표현
    screen.blit(bg2,(0,0)) # 내뒤에 있는 사진 지우기용
    text = font.render('Score: ' + str(score), 2, (0,0,0)) # font 설정!
    screen.blit(text, (450, 10))
    n_door.draw(screen)
    man.draw(screen)
    boss.draw2(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()

def spaceBar():
    if man.left:
            facing = -1
    else:
        facing = 1
    if len(bullets) < 1:
        bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

def leftKey():
    man.x -= man.velocity
    man.left = True
    man.right = False # left일때 오른쪽 키를 누르면 절대 안되기 때문
    man.standing = False

def rightKey():
    man.x += man.velocity
    man.right = True
    man.left= False
    man.standing = False

def jumpUp():
    man.isJump = True
    man.right = False
    man.left = False
    man.standing = False
    man.walkCount = 0

def jumpDown():
    if man.jumpCount >= -10:  
        man.y -= (man.jumpCount * abs(man.jumpCount)) * 0.5
        man.jumpCount -= 1
    else:
        man.jumpCount = 10
        man.isJump = False

def StageTwo():
    second = 1
    man.x = 50
    man.y = 400
    
while beginning == 1:
    clock.tick(27) # 27 frames
    if goblin.visible:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2]  >goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if goblin.visible:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius >goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    score = score + 1
                    bullets.pop(bullets.index(bullet))
            if bullet.x < 600 and bullet.x > 0: #벽을 뚫지 않게
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet)) #[0 . 3 4 8 9] #501 픽셀로 가버리면 불릿을 없애버리는 코드
                #현재의 불릿 인덱스*(위치)를 찾아서 지움
        else:
            if bullet.x < 600 and bullet.x > 0: #벽을 뚫지 않게
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

    pressed = pygame.key.get_pressed()
    ##작은 칸을 넘어가야함. 50 < x < 66 
    if pressed[pygame.K_DOWN]:
        if not goblin.visible:
            if 460 < man.x < 500:
                beginning = 0
                second = 1
                StageTwo()
                break
    if pressed[pygame.K_SPACE]:
        bulletSound.play()
        spaceBar()
    if pressed[pygame.K_LEFT] and man.x > man.velocity: 
        leftKey()
        
    elif pressed[pygame.K_RIGHT] and man.x < 600 - man.width - 5: 
        rightKey()

    else: # If jus standing
        man.standing = True
        man.walkCount = 0

########## 캐릭터의 점프 ###########
    if not (man.isJump): 
        if pressed[pygame.K_UP]:
            jumpUp()

    else:
        jumpDown()
    drawGameWindow()
#while문 나옴.

while second == 1:
    clock.tick(27) # 27 frames
    if boss.visible:
        if man.hitbox[1] < boss.hitbox[1] + boss.hitbox[3] and man.hitbox[1] + man.hitbox[3] > boss.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2]  >boss.hitbox[0] and man.hitbox[0] < boss.hitbox[0] + boss.hitbox[2]:
                man.hit()
                score = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if boss.visible:
            if bullet.y - bullet.radius < boss.hitbox[1] + boss.hitbox[3] and bullet.y + bullet.radius > boss.hitbox[1]:
                if bullet.x + bullet.radius >boss.hitbox[0] and bullet.x - bullet.radius < boss.hitbox[0] + boss.hitbox[2]:
                    boss.hit()
                    score = score + 1
                    bullets.pop(bullets.index(bullet))
            if bullet.x < 600 and bullet.x > 0: #벽을 뚫지 않게
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet)) #[0 . 3 4 8 9] #501 픽셀로 가버리면 불릿을 없애버리는 코드
                #현재의 불릿 인덱스*(위치)를 찾아서 지움
        else:
            if bullet.x < 600 and bullet.x > 0: #벽을 뚫지 않게
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

    pressed = pygame.key.get_pressed()
    ##작은 칸을 넘어가야함. 50 < x < 66 
    if pressed[pygame.K_DOWN]:
        if not goblin.visible:
            if 460 < man.x < 500:
                beginning = 0
                second = 1
                StageTwo()
                break
    if pressed[pygame.K_SPACE]:
        bulletSound.play()
        spaceBar()
    if pressed[pygame.K_LEFT] and man.x > man.velocity: 
        leftKey()
        
    elif pressed[pygame.K_RIGHT] and man.x < 600 - man.width - 5: 
        rightKey()

    else: # If jus standing
        man.standing = True
        man.walkCount = 0

########## 캐릭터의 점프 ###########
    if not (man.isJump): 
        if pressed[pygame.K_UP]:
            jumpUp()

    else:
        jumpDown()

    drawGameWindow2()


pygame.quit()