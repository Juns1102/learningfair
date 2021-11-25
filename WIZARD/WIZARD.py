import os
import pygame
import random
import time
from datetime import datetime


pygame.init()


size = [500, 950]
screen = pygame.display.set_mode(size)

title = "WIZARD"
pygame.display.set_caption(title)

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")
game_font = pygame.font.Font(None, 40)
wave_font = pygame.font.Font(None, 80)
game_font2 = pygame.font.SysFont('malgungothic', 30)

start_ticks = pygame.time.get_ticks()
total_time = 100

enemy1_hp = [5, 5, 7]
enemy1_speed = [2.5, 3.2, 3.2]
enemy2_hp = [20, 25, 28]
enemy2_speed = [1.0, 1.3, 1.4]
wave = 0
wave_start = False
wave_count = 0
enemy_num = [10, 15, 20, 100000]
boss_count = 3
enemy_count = enemy_num[wave]
enemy = ["enemy1.png", "enemy3.png", "enemy5.png"]
enemy_boss = ["enemy2.png", "enemy4.png", "enemy6.png"]
background1 = pygame.image.load(os.path.join(image_path, "background1.png"))
background2 = pygame.image.load(os.path.join(image_path, "background2.png"))
background3 = pygame.image.load(os.path.join(image_path, "background3.png"))
background4 = pygame.image.load(os.path.join(image_path, "end1.png"))
background5 = pygame.image.load(os.path.join(image_path, "end2.png"))
bg = pygame.image.load(os.path.join(image_path, "start.png"))


clock = pygame.time.Clock()

class obj:
    def __init__(tmp):
        tmp.x = 0
        tmp.y = 0
        tmp.move = 0
        tmp.hp = 0
    def put_img(tmp, file_name):
        tmp.img = pygame.image.load(os.path.join(image_path, file_name))
        tmp.sx, tmp.sy = tmp.img.get_size()
    def change_size(tmp, sx, sy):
        tmp.img = pygame.transform.scale(tmp.img, (sx, sy))
        tmp.sx, tmp.sy = tmp.img.get_size()
    def show(tmp):
        screen.blit(tmp.img, (tmp.x,tmp.y))

def crash(a, b):
    if (a.x-b.sx <= b.x) and (b.x <= a.x+a.sx):
        if (a.y-b.sy <= b.y) and (b.y <= a.y+a.sy):
            return True
        else:
            return False
    else : 
        return False

character = obj()
character.put_img("character.png")
character.change_size(100,100)
character.x = round(size[0]/2- character.sx/2)
character.y = size[1] -character.sy
character.move = 0.6
character.hp = 3


left = False
right = False
skill_1 = False
skill_2 = False
skill_3 = False
skill_4 = False
game_stop = False

attack_list = []
enemy1_list = []
enemy2_list = []
skill1_list = []
skill2_list = []
skill3_list = []
skill4_list = []
skill11_q = 9
skill22_q = 25
skill33_q = 8
skill44_q = 13
skill11_qq = 0
skill22_qq = 0
skill33_qq = 0
skill44_qq = 0
skill11_qc = 0
skill22_qc = 0
skill33_qc = 0
skill44_qc = 0

attack_start = True
enemy1_r = 0
reset = 0
skill1_r = 0
skill1_c = 0
skill1_cc = True
skill2_r = 0
skill2_c = 0
skill2_cc = True
skill3_r = 0
skill3_c = 0
skill3_cc = True
skill4_r = 0
skill4_c = 0
skill4_cc = True
enemy1_start = random.randint(1, 2)
enemy2_start = False
enemy2_stop = False



running = 0
while running == 0:
    time = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = 1
    screen.blit(bg, (0, 0))
    msg = game_font.render("-PRESS SPACE TO START-", True, (255, 255, 255))
    screen.blit(msg, (75, 700))
    pygame.display.flip()


start_time = datetime.now()
running = 2
while running == 2:
    time = clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            elif event.key == pygame.K_RIGHT:
                right = True
            elif event.key == pygame.K_q:
                skill_1 = True
            elif event.key == pygame.K_w:
                skill_2 = True
            elif event.key == pygame.K_e:
                skill_3 = True
            elif event.key == pygame.K_r:
                skill_4 = True
            elif event.key == pygame.K_SPACE:
                game_stop = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            elif event.key == pygame.K_RIGHT:
                right = False
            elif event.key == pygame.K_q:
                skill_1 = False
            elif event.key == pygame.K_w:
                skill_2 = False
            elif event.key == pygame.K_e:
                skill_3 = False
            elif event.key == pygame.K_r:
                skill_4 = False
            elif event.key == pygame.K_SPACE:
                game_stop = False

                
    now_time = datetime.now()
    delta_time = round((now_time - start_time).total_seconds())
    
    wave_count += 1
    if wave_count >= 60*3:
        wave_start = True
    else:
        wave_start = False
    skill1_r += 1
    skill1_c += 1
    skill11_qq += 1
    if skill11_qq % 60 == 0:
        skill11_qc += 1  
    if skill1_c >= 60*9:
        skill1_cc = True
    skill2_r += 1
    skill2_c += 1
    skill22_qq += 1
    if skill22_qq % 60 == 0:
        skill22_qc += 1
    if skill2_c >= 60*25:
        skill2_cc = True
    skill3_r += 1
    skill3_c += 1
    skill33_qq += 1
    if skill33_qq % 60 == 0:
        skill33_qc += 1
    if skill3_c >= 60*8:
        skill3_cc = True
    skill4_r += 1
    skill4_c += 1
    skill44_qq += 1
    if skill44_qq % 60 == 0:
        skill44_qc += 1
    if skill4_c >= 60*13:
        skill4_cc = True
    enemy1_r += 1
    reset += 1

    if left == True:
        character.x -= character.move * time
        if character.x <= 0:
            character.x = 0
    elif right == True:
        character.x += character.move * time
        if character.x >= size[0] - character.sx:
            character.x = size[0] - character.sx

    
    if reset > 80 and attack_start == True and wave_start == True and boss_count != 0:
        attack = obj()
        attack.put_img("attack.png")
        attack.change_size(20,40)
        attack.x = round(character.x + character.sx/2 - attack.sx/2)
        attack.y = character.y + 45
        attack.move = 20
        attack.hp = 1
        attack_list.append(attack)
        reset = 0
    
    del_attack_list = []    
    for i in range(len(attack_list)):
        attack = attack_list[i]
        attack.y -= attack.move
        if attack.y <= -attack.sy:
            del_attack_list.append(i)
    del_attack_list.reverse()
    for b1 in del_attack_list:
        del attack_list[b1]

    if skill_1 == True and skill1_cc == True and wave_start == True and boss_count != 0:
        skill1 = obj()
        skill1.put_img("skill1_c.png")
        skill1.change_size(150,850)
        skill1.x = character.x - 25
        skill1.y = character.y - 200
        skill1.move = 100
        skill1.hp = 1
        skill1_list.append(skill1)
        skill1_r = 0
        skill1_c = 0
        skill11_qq = 0
        skill11_qc = 0
        skill1_cc = False
        attack_start = False

    del_skill1_list = []
    for i in range(len(skill1_list)):
        skill1 = skill1_list[i]
        skill1.x = character.x - 25
        skill1.y -= skill1.move
        if skill1.y <= 0:
            skill1.y = 0
    del_skill1_list.reverse()
    for b1 in del_skill1_list:
        del skill1_list[b1]

    if skill_2 == True and skill2_cc == True and wave_start == True and boss_count != 0:
        skill2 = obj()
        skill2.put_img("skill2.png")
        skill2.change_size(100,100)
        skill2.x = character.x
        skill2.y = character.y
        skill2.move = 0
        skill2.hp = 1
        if character.hp < 3:
            character.hp += 1
        skill2_list.append(skill2)
        skill2_r = 0
        skill2_c = 0
        skill22_qq = 0
        skill22_qc = 0
        skill2_cc = False

    del_skill2_list = []
    for i in range(len(skill2_list)):
        skill2 = skill2_list[i]
        skill2.x = character.x
        skill2.y = character.y
    del_skill2_list.reverse()
    for b1 in del_skill2_list:
        del skill2_list[b1]

    if skill_3 == True and skill3_cc == True and wave_start == True and boss_count != 0:
        skill3 = obj()
        skill3.put_img("skill3.png")
        skill3.change_size(200,850)
        skill3.x = character.x - 50
        skill3.y = character.y - 200
        skill3.move = 6
        skill3.hp = 1
        skill3_list.append(skill3)
        skill3_r = 0
        skill3_c = 0
        skill33_qq = 0
        skill33_qc = 0
        skill3_cc = False

    del_skill3_list = []
    for i in range(len(skill3_list)):
        skill3 = skill3_list[i]
        skill3.y -= skill3.move
        if skill3.y <= -skill3.sy or wave_start == False and boss_count != 0:
            del_skill3_list.append(i)
    del_skill3_list.reverse()
    for b1 in del_skill3_list:
        del skill3_list[b1]

    if skill_4 == True and skill4_cc == True and wave_start == True and boss_count != 0:
        skill4 = obj()
        skill4.put_img("skill4.png")
        skill4.change_size(500,950)
        skill4.x = 0
        skill4.y = 0
        skill4.move = 0
        skill4.hp = 1
        skill4_list.append(skill4)
        skill4_r = 0
        skill4_c = 0
        skill44_qq = 0
        skill44_qc = 0
        skill4_cc = False
        
    if enemy1_start*60 < enemy1_r and wave_start == True and boss_count != 0:
        enemy1 = obj()
        enemy1.put_img(enemy[wave])
        enemy1.change_size(70,70)
        enemy1.x = random.randrange(0, size[0]-enemy1.sx-round(character.sx/2))
        enemy1.y = -enemy1.sy
        enemy1.move = enemy1_speed[wave]
        enemy1.hp = enemy1_hp[wave]
        enemy1_list.append(enemy1)
        enemy1_start = random.randint(2, 3)
        enemy1_r=0
    
    del_enemy1_list = []
    for i in range(len(enemy1_list)):
        enemy1 = enemy1_list[i]
        if skill4_c <= 60*4 and skill4_cc == False:
            enemy1.y += enemy1.move / 2 
        else:
            enemy1.y += enemy1.move
        if enemy1.y >= character.y:
            del_enemy1_list.append(i)
            character.hp -= 1
        if wave_start == False:
            del_enemy1_list.append(i)
    del_enemy1_list.reverse()
    for b1 in del_enemy1_list:
        del enemy1_list[b1]
        enemy_num[wave] -= 1
        if enemy_num[wave] == 0:
            enemy2_start = True
        

    if enemy2_start == True and wave_start == True and enemy2_stop == False and boss_count != 0:
        enemy2 = obj()
        enemy2.put_img(enemy_boss[wave])
        enemy2.change_size(200,200)
        enemy2.x = 150
        enemy2.y = -enemy2.sy
        enemy2.move = enemy2_speed[wave]
        enemy2.hp = enemy2_hp[wave]
        enemy2_list.append(enemy2)
        enemy2_start = False
        enemy2_stop = True
    
    del_enemy2_list = []
    for i in range(len(enemy2_list)):
        enemy2 = enemy2_list[i]
        if skill4_c <= 60*4 and skill4_cc == False:
            enemy2.y += enemy2.move / 2 
        else:
            enemy2.y += enemy2.move
        if enemy2.y >= character.y:
            del_enemy2_list.append(i)
            character.hp -= 3
    del_enemy2_list.reverse()
    for b1 in del_enemy2_list:
        del enemy2_list[b1]
        boss_count -= 1
        wave_count = 0
        if wave == 3:
            wave += 0
        else:
            wave += 1
        enemy2_stop = False
    
    da_list = []
    dt_list = []
    for a in range(len(attack_list)):
        for t in range(len(enemy1_list)):
            a1 = attack_list[a]
            t1 = enemy1_list[t]
            if crash(a1,t1) == True:
                a1.hp -= 1
                t1.hp -= 1
                if a1.hp <= 0:
                    da_list.append(a)
                if t1.hp <= 0:
                    dt_list.append(t)
    da_list = list(set(da_list))
    dt_list = list(set(dt_list))
    da_list.reverse()
    dt_list.reverse()
    for da in da_list:
        del attack_list[da]
    for dt in dt_list:
        del enemy1_list[dt]
        enemy_num[wave] -= 1
        if enemy_num[wave] == 0:
            enemy2_start = True

    dab_list = []
    dtb_list = []
    for a in range(len(attack_list)):
        for t in range(len(enemy2_list)):
            a1 = attack_list[a]
            t1 = enemy2_list[t]
            if crash(a1,t1) == True:
                a1.hp -= 1
                t1.hp -= 1
                if a1.hp <= 0:
                    dab_list.append(a)
                if t1.hp <= 0:
                    dtb_list.append(t)
    dab_list = list(set(dab_list))
    dtb_list = list(set(dtb_list))
    dab_list.reverse()
    dtb_list.reverse()
    for da in dab_list:
        del attack_list[da]
    for dt in dtb_list:
        del enemy2_list[dt]
        boss_count -= 1
        wave_count = 0
        if wave == 3:
            wave += 0
        else:
            wave += 1
        enemy2_stop = False

    ds1_list = []
    dt1_list = []
    for s1 in range(len(skill1_list)):
        for t2 in range(len(enemy1_list)):
            s = skill1_list[s1]
            t = enemy1_list[t2]
            if skill1_r >= 60*3 or wave_start == False:
                ds1_list.append(s1)
                attack_start = True
            if crash(s,t) == True and skill1_r % 30 == 0:
                t.hp -= 2
                if t.hp <= 0:
                    dt1_list.append(t2)
    ds1_list = list(set(ds1_list))
    dt1_list = list(set(dt1_list))
    ds1_list.reverse()
    dt1_list.reverse()
    for ds1 in ds1_list:
        del skill1_list[ds1]
    for dt1 in dt1_list:
        del enemy1_list[dt1]
        enemy_num[wave] -= 1
        if enemy_num[wave] == 0:
            enemy2_start = True

    dsb1_list = []
    dtb1_list = []
    for s1 in range(len(skill1_list)):
        for t2 in range(len(enemy2_list)):
            s = skill1_list[s1]
            t = enemy2_list[t2]
            if skill1_r >= 60*3 or wave_start == False:
                dsb1_list.append(s1)
                attack_start = True
            if crash(s,t) == True and skill1_r % 30 == 0:
                t.hp -= 2
                if t.hp <= 0:
                    dtb1_list.append(t2)
    dsb1_list = list(set(dsb1_list))
    dtb1_list = list(set(dtb1_list))
    dsb1_list.reverse()
    dtb1_list.reverse()
    for ds1 in dsb1_list:
        del skill1_list[ds1]
    for dt1 in dtb1_list:
        del enemy2_list[dt1]
        boss_count -= 1
        wave_count = 0
        if wave == 3:
            wave += 0
        else:
            wave += 1
        enemy2_stop = False

    ds2_list = []
    for s2 in range(len(skill2_list)):
        s = skill2_list[s2]
        if skill2_r >= 60*1:
            ds2_list.append(s2)
    ds2_list = list(set(ds2_list))
    ds2_list.reverse()
    for ds2 in ds2_list:
        del skill2_list[ds2]

    for s1 in range(len(skill3_list)):
        for t2 in range(len(enemy1_list)):
            s = skill3_list[s1]
            t = enemy1_list[t2]
            if crash(s,t) == True:
                if skill4_c <= 60*4 and skill4_cc == False:
                    t.y -= (t.move - enemy1.move / 2)
                else:
                    t.y -= t.move

    for s1 in range(len(skill3_list)):
        for t2 in range(len(enemy2_list)):
            s = skill3_list[s1]
            t = enemy2_list[t2]
            if crash(s,t) == True:
                if skill4_c <= 60*4 and skill4_cc == False:
                    t.y -= (t.move - enemy2.move / 2)
                else:
                    t.y -= t.move

    ds4_list = []
    dt4_list = []
    for s1 in range(len(skill4_list)):
        for t2 in range(len(enemy1_list)):
            s = skill4_list[s1]
            t = enemy1_list[t2]
            if skill4_r >= 60*4 or wave_start == False:
                ds4_list.append(s1)
            if crash(s,t) == True and skill4_r % 60 == 0:
                t.hp -= 1
                if t.hp <= 0:
                    dt4_list.append(t2)
    ds4_list = list(set(ds4_list))
    dt4_list = list(set(dt4_list))
    ds4_list.reverse()
    dt4_list.reverse()
    for ds1 in ds4_list:
        del skill4_list[ds1]
    for dt1 in dt4_list:
        del enemy1_list[dt1]
        enemy_num[wave] -= 1
        if enemy_num[wave] == 0:
            enemy2_start = True

    dsb4_list = []
    dtb4_list = []
    for s1 in range(len(skill4_list)):
        for t2 in range(len(enemy2_list)):
            s = skill4_list[s1]
            t = enemy2_list[t2]
            if skill4_r >= 60*4 or wave_start == False:
                dsb4_list.append(s1)
            if crash(s,t) == True and skill4_r % 80 == 0:
                t.hp -= 1
                if t.hp <= 0:
                    dtb4_list.append(t2)
    dsb4_list = list(set(dsb4_list))
    dtb4_list = list(set(dtb4_list))
    dsb4_list.reverse()
    dtb4_list.reverse()
    for ds1 in dsb4_list:
        del skill4_list[ds1]
    for dt1 in dtb4_list:
        del enemy2_list[dt1]
        boss_count -= 1
        wave_count = 0
        if wave == 3:
            wave += 0
        else:
            wave += 1
        enemy2_stop = False


    if wave == 0:
        screen.blit(background1, (0, 0))
        if wave_count <= 90:
            screen.blit(wave_font.render("WAVE {}".format(wave + 1) , True, (255, 255, 255)), (150, 400))
        elif wave_count <= 180:
            screen.blit(wave_font.render("Start!!" , True, (255, 255, 255)), (170, 400))
    elif wave == 1:
        screen.blit(background2, (0, 0))
        if wave_count <= 90:
            screen.blit(wave_font.render("WAVE {}".format(wave + 1) , True, (255, 255, 255)), (150, 400))
        elif wave_count <= 180:
            screen.blit(wave_font.render("Start!!" , True, (255, 255, 255)), (170, 400))
    elif wave == 2:
        screen.blit(background3, (0, 0))
        if wave_count <= 90:
            screen.blit(wave_font.render("WAVE {}".format(wave + 1) , True, (255, 255, 255)), (150, 400))
        elif wave_count <= 180:
            screen.blit(wave_font.render("Start!!" , True, (255, 255, 255)), (170, 400))
    if boss_count != 0:
        msg = game_font2.render("\u2665 {}".format(character.hp) , True, (255, 100, 100))
        if skill1_cc == False:
            skill11 = game_font.render("{}".format(skill11_q - skill11_qc) , True, (255, 51, 51))
            screen.blit(skill11, (10, 10))
        else:
            skill11_r = game_font.render("Q", True, (255, 51, 51))
            screen.blit(skill11_r, (10, 10))
        if skill2_cc == False:
            skill22 = game_font.render("{}".format(skill22_q - skill22_qc) , True, (51, 153, 255))
            screen.blit(skill22, (55, 10))
        else:
            skill22_r = game_font.render("W", True, (51, 153, 255))
            screen.blit(skill22_r, (55, 10))
        if skill3_cc == False:
            skill33 = game_font.render("{}".format(skill33_q - skill33_qc) , True, (51, 255, 51))
            screen.blit(skill33, (105, 10))
        else:
            skill33_r = game_font.render("E", True, (51, 255, 51))
            screen.blit(skill33_r, (105, 10))
        if skill4_cc == False:
            skill44 = game_font.render("{}".format(skill44_q - skill44_qc) , True, (153, 255, 255))
            screen.blit(skill44, (145, 10))
        else:
            skill44_r = game_font.render("R", True, (153, 255, 255))
            screen.blit(skill44_r, (145, 10))
        screen.blit(msg, (435, 0))
        character.show()
    if wave_start == True and boss_count != 0:
        for attack in attack_list:
            attack.show()
        for enemy1 in enemy1_list:
            enemy1.show()
        for enemy2 in enemy2_list:
            enemy2.show()
        for skill4 in skill4_list:
            skill4.show()
        for skill2 in skill2_list:
            skill2.show()
        for skill3 in skill3_list:
            skill3.show()
        for skill1 in skill1_list:
            skill1.show()

    if boss_count == 0:
        screen.blit(background4, (0, 0))
        msg2 = game_font.render("-PRESS SPACE TO STOP-", True, (255, 255, 255))
        screen.blit(msg2, (80, 700))
        if game_stop == True:
            running = 3
    if character.hp <= 0:
        screen.blit(background5, (0, 0))
        msg3 = game_font.render("-PRESS SPACE TO STOP-", True, (255, 255, 255))
        screen.blit(msg3, (80, 700))
        if game_stop == True:
            running = 3

    pygame.display.flip()


pygame.quit()