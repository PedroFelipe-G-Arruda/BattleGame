import pygame

pygame.init()

x = 1280
y = 720

pos_x = x/2
pos_y = 5*y/12

h = 200

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Joguinho de Batalha')

bg = pygame.image.load('images/bg.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

warrior = pygame.image.load('images/warrior.png').convert_alpha()

warrior = pygame.transform.scale(warrior, (h,h))
warrior = pygame.transform.flip(warrior,True,False)

warrior_enemy = pygame.image.load('images/warrior-en2.png').convert_alpha()
warrior_enemy = pygame.transform.scale(warrior_enemy, (h,h))

pos_warrior_x = pos_x - 180
pos_warrior_y = pos_y + 40

pos_warrioren_x = pos_x
pos_warrioren_y = pos_y + 40



archer = pygame.image.load('images/rodolfo.png').convert_alpha()
archer = pygame.transform.scale(archer, (h,h))
archer = pygame.transform.flip(archer,True,False)

archer_enemy = pygame.image.load('images/rodolfo-enemy.png').convert_alpha()
archer_enemy = pygame.transform.scale(archer_enemy, (h,h))


pos_archer_x = pos_x - 180 * 2
pos_archer_y = pos_y

pos_archeren_x = pos_x + 180
pos_archeren_y = pos_y


archer = pygame.image.load('images/rodolfo.png').convert_alpha()
archer = pygame.transform.scale(archer, (150,150))
archer = pygame.transform.flip(archer,True,False)


mage = pygame.image.load('images/mage.png').convert_alpha()
mage = pygame.transform.scale(mage, (h,h))
mage = pygame.transform.flip(mage,True,False)

mage_enemy = pygame.image.load('images/mage-en2.png').convert_alpha()
mage_enemy = pygame.transform.scale(mage_enemy, (h,h))


pos_mage_x = pos_x - 160 * 3
pos_mage_y = pos_y - 40 

pos_mageen_x = pos_x + 150 * 2
pos_mageen_y = pos_y - 40


rodando = True 

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0))

    # Criar imagens
    screen.blit(warrior, (pos_warrior_x, pos_warrior_y))
    screen.blit(warrior_enemy, (pos_warrioren_x, pos_warrioren_y))

    screen.blit(archer, (pos_archer_x, pos_archer_y))
    screen.blit(archer_enemy, (pos_archeren_x, pos_archeren_y))

    screen.blit(mage, (pos_mage_x, pos_mage_y))
    screen.blit(mage_enemy, (pos_mageen_x, pos_mageen_y))


    #for i in range(0,721,60):
    #    pygame.draw.line(screen, (255, 0, 0), (0, i), (x, i))
    #pygame.draw.line(screen, (255, 0, 0), (x/2,0), (x/2, y))
    #pygame.display.flip()

    pygame.display.update()


    pygame.display.update()
