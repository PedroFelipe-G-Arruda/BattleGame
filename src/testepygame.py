import pygame

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Joguinho de Batalha')

bg = pygame.image.load('images/background.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

warrior = pygame.image.load('images/warrior.png').convert_alpha()
warrior = pygame.transform.scale(warrior, (150,150))
warrior = pygame.transform.flip(warrior,True,False)

warrior_enemy = pygame.image.load('images/warrior-en2.png').convert_alpha()
warrior_enemy = pygame.transform.scale(warrior_enemy, (150,150))


pos_warrior_x = 250
pos_warrior_y = 530

pos_warrioren_x = 450
pos_warrioren_y = 530

archer = pygame.image.load('images/rodolfo.png').convert_alpha()
archer = pygame.transform.scale(archer, (150,150))
archer = pygame.transform.flip(archer,True,False)

archer_enemy = pygame.image.load('images/rodolfo-enemy.png').convert_alpha()
archer_enemy = pygame.transform.scale(archer_enemy, (150,150))


pos_archer_x = 200
pos_archer_y = 450

pos_archeren_x = 600
pos_archeren_y = 450


mage = pygame.image.load('images/mage.png').convert_alpha()
mage = pygame.transform.scale(mage, (150,150))
mage = pygame.transform.flip(mage,True,False)

mage_enemy = pygame.image.load('images/mage-en2.png').convert_alpha()
mage_enemy = pygame.transform.scale(mage_enemy, (150,150))


pos_mage_x = 100
pos_mage_y = 300

pos_mageen_x = 700
pos_mageen_y = 300

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

    pygame.display.update()
