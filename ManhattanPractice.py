import pygame
from ManhattanP_classes import *
pygame.init()

walkRight = [pygame.image.load('MainChara_R/R1.png'), pygame.image.load('MainChara_R/R2.png'), pygame.image.load('MainChara_R/R3.png')]#, pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('MainChara_R/L1.png'), pygame.image.load('MainChara_R/L2.png'), pygame.image.load('MainChara_R/L3.png')]#, pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
bg2 = pygame.image.load('bg_map/bg2.png')
bg3 = pygame.image.load('bg_map/bg3.png')
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

clock = pygame.time.Clock()
beginning = 1 # 1 = true
second = 0 #0 = false, do not start stage two yet

man = player(50, 400, 64, 64)#main character
goblin = enemy(100, 410, 64, 64, 550, 5, 10, 10) #goblin = class를 가진 instance. 
boss = enemy(80, 410, 64, 64, 550, 7, 20, 20)
human = npc(200, 410, 64, 64)#self, x, y, width, height

n_door = portal(500, 400, 64, 27)
m_door = portal(500, 400, 64, 27)

bullets = [] #각각의 총알의 명령문을 저장 => 총알이 몇알이 나가는지를 세어주는 역할
font = pygame.font.SysFont('cosmicsans', 30, True)
dia_font = pygame.font.SysFont('cosmicsans', 20, True)
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
    text = font.render('Score: ' + str(score), 2, (255,255,255)) # font 설정!
    screen.blit(text, (450, 10))
    n_door.draw(screen)
    man.draw(screen)
    boss.draw2(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()

def drawGameWindow3(): #캐릭터가 움직일때마다 모션 표현
    screen.blit(bg3,(0,0)) # 내뒤에 있는 사진 지우기용
    text = font.render('Score: ' + str(score), 2, (0,0,0)) # font 설정!
    screen.blit(text, (450, 10))
    m_door.draw(screen)
    man.draw(screen)
    human.draw(screen)
    human.dialogue('You killed me! But you destroyed the city also!')
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

def Control():
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

while beginning == 1:
    clock.tick(27) # 27 frames
    goblin.manHit()
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
    Control()
    drawGameWindow()
#while문 나옴.

while second == 1:
    clock.tick(27) # 27 frames
    boss.manHit()
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
        if not boss.visible:
            if 460 < man.x < 500:
                second = 0
                Third = 1
                StageTwo()
                break
    Control()
    drawGameWindow2()

while Third == 1:
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
    if pressed[pygame.K_DOWN]:
        if not boss.visible:
            if 460 < man.x < 500:
                beginning = 0
                fourth = 1
                StageTwo()
                break
        if 168< man.x <232:
            human.dialogue('You killed me! But you destroyed the city also!')
    Control()
    drawGameWindow3()
pygame.quit()