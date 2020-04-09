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
    dungeonPortal = [pygame.image.load('door/door_n.png'), pygame.image.load('door/door_m.png')]
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
class npc():
    standing = pygame.image.load('Game/Standing.png')
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, screen):
        #self.walkCount = 0 #이유-> 사진이 9 개인데 카운트를 하나씩 늘려서 0번째부터 9번쨰까지 다 process 시키려고
        screen.blit(self.standing, (self.x, self.y))
    def dialogue(self, writings):
        self.writings = writings
        dia = dia_font.render(self.writings, 25, (255,0,0))

        screen.blit(dia, (200, 410))


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
    
    def manHit(self):
        if self.visible:
            if man.hitbox[1] < self.hitbox[1] + self.hitbox[3] and man.hitbox[1] + man.hitbox[3] > self.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2]  >self.hitbox[0] and man.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
                    man.hit()
                    score = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False   