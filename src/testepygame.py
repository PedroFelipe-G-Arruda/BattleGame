from errno import ENOTEMPTY
import pygame

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Joguinho de Batalha')

bg = pygame.image.load('images/background.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

warrior = pygame.image.load('images/warrior.png').convert_alpha()
warrior = pygame.transform.scale(warrior, (100,100))
warrior = pygame.transform.flip(warrior,True,False)

warrior_enemy = pygame.image.load('images/warrior-en2.png').convert_alpha()
warrior_enemy = pygame.transform.scale(warrior_enemy, (100,100))


pos_warrior_x = 200
pos_warrior_y = 560

pos_warrioren_x = 500
pos_warrioren_y = 560



rodando = True 

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0))

    # Criar imagens
    screen.blit(warrior, (pos_warrior_x, pos_warrior_y))
    screen.blit(warrior_enemy, (pos_warrioren_x, pos_warrioren_y))

    pygame.display.update()

