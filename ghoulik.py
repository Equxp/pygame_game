import pygame

pygame.init()

x, y = 500, 410
x_k, y_k = 200, 100
x_s, y_s =800, 50

main_heror = [pygame.image.load(
    'main_hero.png'), pygame.image.load('main_hero1.png')]
main_herol = [pygame.image.load(
    'main_herol.png'), pygame.image.load('main_herol1.png')]
monster = pygame.image.load('monster.png')

main_hero_downed = [pygame.image.load(
    'main_hero_downnedr.png'), pygame.image.load('main_hero_downnedl.png')]


door = [pygame.image.load('door_closed.png'),
        pygame.image.load('door_open.png')]
bg = [pygame.image.load('bg1.png'), pygame.image.load('bg2.png'), pygame.image.load(
    'bg3.png'), pygame.image.load('bg4.png'), pygame.image.load('bg2.png'), pygame.image.load('bg3.png')]

key = pygame.image.load('key.png')
spike = pygame.image.load('spike.png')

scr = pygame.display.set_mode((1000, 800))

FPS = 60
clock = pygame.time.Clock()

play = False

right = False
left = False
dont_move = False

level1 = True
level2 = False
level3 = False
level4 = False

start_color = 0
play_color = (0, 0, 0)

animCount = 0

heroCount = 0

keyCount = 10

pickkey1 = False
pickkey2 = False
pickkey3 = False
pickkey4 = False

monster_visible = False

i = 0
speed = 5

is_jump = False
jump_count = 10

downned = False

f1 = pygame.font.SysFont('gayathri', 100)
text1 = f1.render('Play', 1, (30, 30, 30))

f2 = pygame.font.SysFont('uroob', 20)
text2 = f2.render("Why i can't move?!", True, (0, 0, 0))

texts1 = False


run = True


def drawwing():
    global play, start_color, x_s, y_s,play_color, animCount, heroCount, run, x, y, x_k, y_k, keyCount, monster_visible, \
        pickkey4, pickkey1, pickkey2, pickkey3, level1, level2, level3, level4, texts1, dont_move
    if animCount + 1 >= 30:
        animCount = 0
    else:
        scr.blit(bg[animCount//5], (0, 0))
        animCount += 1
    a = pygame.draw.rect(scr, (play_color), (370, 300, 300, 100))
    scr.blit(text1, (440, 310))
    if a.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
        play_color = (20, 20, 20)
        if pygame.mouse.get_pressed()[0]:
            play = True

    else:
        play_color = (0, 0, 0)
    if play == True:
        if level1:
            key_rect = key.get_rect(topleft=(x_k, y_k))
            main_herol_rect1 = main_herol[0].get_rect(topleft=(x, y))
            main_herol_rect2 = main_herol[1].get_rect(topleft=(x, y))
            main_heror_rect1 = main_heror[0].get_rect(topleft=(x, y))
            main_heror_rect2 = main_heror[1].get_rect(topleft=(x, y))
            pygame.mouse.set_visible(False)
            scr.fill((start_color, start_color, start_color))
            pygame.draw.line(scr, (0, 0, 0), (0, 500), (1000, 500), 4)
            if start_color <= 100:
                start_color += 0.5
            if not(pickkey1):
                scr.blit(key, (x_k, y_k))

            if heroCount + 1 >= 30:
                heroCount = 0
            else:
                if right:
                    if not(downned):
                        scr.blit(main_heror[heroCount//15], (x, y))
                        heroCount += 1
                        if main_heror_rect1.colliderect(key_rect) or main_heror_rect2.colliderect(key_rect):
                            pickkey1 = True

                if left:
                    if not(downned):
                        scr.blit(main_herol[heroCount//15], (x, y))
                        heroCount += 1
                        if main_herol_rect1.colliderect(key_rect) or main_herol_rect2.colliderect(key_rect):
                            pickkey1 = True
            if pickkey1:
                if level1:
                    scr.blit(door[0], (0, 500-120))
                    door_rect = door[0].get_rect(topleft=(0, 380))
                    if main_herol_rect1.colliderect(door_rect) or main_herol_rect2.colliderect(door_rect):
                        x = 700
                        level1 = False
                        level2 = True
            else:
                scr.blit(door[1], (0, 500-120))
        elif level2:
            pickkey1 = False
            key_rect = key.get_rect(topleft=(x_k+300, y_k+50))
            main_herol_rect1 = main_herol[0].get_rect(topleft=(x, y))
            main_herol_rect2 = main_herol[1].get_rect(topleft=(x, y))
            main_heror_rect1 = main_heror[0].get_rect(topleft=(x, y))
            main_heror_rect2 = main_heror[1].get_rect(topleft=(x, y))
            pygame.mouse.set_visible(False)
            scr.fill((start_color, start_color, start_color))
            pygame.draw.line(scr, (0, 0, 0), (0, 500), (1000, 500), 4)
            if start_color <= 100:
                start_color += 0.5
            if not(pickkey2):
                scr.blit(key, (x_k+300, y_k+50))
            scr.blit(spike, (449, 450))
            scr.blit(spike, (499, 450))
            spike1 = spike.get_rect(topleft=(449, 450))
            spike2 = spike.get_rect(topleft=(499, 450))
            if heroCount + 1 >= 30:
                heroCount = 0
            else:
                if right:
                    scr.blit(main_heror[heroCount//15], (x, y))
                    heroCount += 1
                    if main_heror_rect1.colliderect(key_rect) or main_heror_rect2.colliderect(key_rect):
                        pickkey2 = True
                    if main_heror_rect1.colliderect(spike1) or main_heror_rect2.colliderect(spike1) or main_heror_rect1.colliderect(spike2) or main_heror_rect2.colliderect(spike2):
                        run = False

                if left:
                    scr.blit(main_herol[heroCount//15], (x, y))
                    heroCount += 1
                    if main_herol_rect1.colliderect(key_rect) or main_herol_rect2.colliderect(key_rect):
                        pickkey2 = True
                    if main_herol_rect1.colliderect(spike1) or main_herol_rect2.colliderect(spike1) or main_herol_rect1.colliderect(spike2) or main_herol_rect2.colliderect(spike2):
                        run = False
            if pickkey2:
                if level2:
                    scr.blit(door[0], (0, 500-120))
                    door_rect = door[0].get_rect(topleft=(0, 380))
                    if main_herol_rect1.colliderect(door_rect) or main_herol_rect2.colliderect(door_rect):
                        x = 700
                        level2 = False
                        level3 = True
            else:
                scr.blit(door[1], (0, 500-120))
        elif level3:
            pickkey2 = False
            key_rect = key.get_rect(topleft=(x_k, y_k))
            main_herol_rect1 = main_herol[0].get_rect(topleft=(x, y))
            main_herol_rect2 = main_herol[1].get_rect(topleft=(x, y))
            main_heror_rect1 = main_heror[0].get_rect(topleft=(x, y))
            main_heror_rect2 = main_heror[1].get_rect(topleft=(x, y))
            pygame.mouse.set_visible(False)
            scr.fill((start_color, start_color, start_color))
            pygame.draw.line(scr, (0, 0, 0), (0, 500), (1000, 500), 4)
            if start_color <= 100:
                start_color += 0.5
            if not(pickkey3):
                scr.blit(key, (x_k, y_k))
            if heroCount + 1 >= 30:
                heroCount = 0
            else:
                if right:
                    scr.blit(main_heror[heroCount//15], (x, y))
                    heroCount += 1
                    if main_heror_rect1.colliderect(key_rect) or main_heror_rect2.colliderect(key_rect):
                        pickkey3 = True
                if left:
                    scr.blit(main_herol[heroCount//15], (x, y))
                    heroCount += 1
                    if main_herol_rect1.colliderect(key_rect) or main_herol_rect2.colliderect(key_rect):
                        pickkey3 = True
            if pickkey3:
                if level3:
                    scr.blit(door[0], (0, 500-120))
                    door_rect = door[0].get_rect(topleft=(0, 380))
                    if main_herol_rect1.colliderect(door_rect) or main_herol_rect2.colliderect(door_rect):
                        x = 700
                        level3 = False
                        level4 = True

            else:
                scr.blit(door[1], (0, 500-120))
        elif level4:
            key_rect = key.get_rect(topleft=(x_k, y_k))
            main_herol_rect1 = main_herol[0].get_rect(topleft=(x, y))
            main_herol_rect2 = main_herol[1].get_rect(topleft=(x, y))
            main_heror_rect1 = main_heror[0].get_rect(topleft=(x, y))
            main_heror_rect2 = main_heror[1].get_rect(topleft=(x, y))
            pygame.mouse.set_visible(False)
            scr.fill((start_color, start_color, start_color))
            pygame.draw.line(scr, (0, 0, 0), (0, 500), (1000, 500), 4)
            if start_color <= 100:
                start_color += 0.5
            if not(pickkey4):
                scr.blit(key, (x_k, y_k))

            if heroCount + 1 >= 30:
                heroCount = 0
            else:
                if right:
                    if not(downned):
                        scr.blit(main_heror[heroCount//15], (x, y))
                        heroCount += 1
                        if main_heror_rect1.colliderect(key_rect) or main_heror_rect2.colliderect(key_rect):
                            pickkey4 = True

                if left:
                    if not(downned):
                        scr.blit(main_herol[heroCount//15], (x, y))
                        heroCount += 1
                        if main_herol_rect1.colliderect(key_rect) or main_herol_rect2.colliderect(key_rect):
                            pickkey4 = True
            if pickkey4:
                if level4:
                    scr.blit(door[0], (0, 500-120))
                    texts1 = True
                    y = 410
                    if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_d]:
                        dont_move = True

            else:
                scr.blit(door[1], (0, 500-120))
            if dont_move:
                if x_s <=830:
                    scr.blit(text2, (x+20, y+20))
                    f3 = pygame.font.SysFont('uroob', 100)
                    text3 = f3.render('Press space many times!', True, (0, 0, 0))
                    scr.blit(text3, (150, y-100))
                    pygame.draw.line(scr, (0,0,0), (200, 50), (x_s, y_s), 5)
                    if x_s >=210:
                        x_s -=10
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        x_s +=20
                else:
                    texts1 = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if not(texts1):
        if keys[pygame.K_d] and x <= 998 - 41:
            x += speed
            right = True
            left = False
        elif keys[pygame.K_a] and x >= 2:
            x -= speed
            left = True
            right = False
        elif keys[pygame.K_s]:
            downned = True
        if not(is_jump):
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -10:
                if jump_count < 0:
                    y += (jump_count ** 2) / 2
                else:
                    y -= (jump_count ** 2) / 2
                jump_count -= 0.5
            else:
                is_jump = False
                jump_count = 10

    drawwing()
    pygame.display.flip()
    clock.tick(FPS)
