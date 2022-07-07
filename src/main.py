# Bibliotecas
import personagens as pg # importas os personagens
import batalha as bt
from time import sleep # 

# Cores
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

# Mostra os atributos dos personagens 
def atributos(pers):
    print(BOLD + f'Nome: {pers.nome}')
    print(CYAN + f'Classe: {pers.classe}')
    #print(GREEN + f'Vida: {pers.vida}')
    #print(RED + f'Ataque: {pers.ataque}')
    #print(BLUE + f'Range: {pers.range}'+RESET)
    print(GREEN + f'Vida: {pers.vida} ' + '■'*pers.vida)
    print(RED + f'Ataque: {pers.ataque} ' + '■'*pers.ataque)
    print(BLUE + f'Range: {pers.range} ' + '■'*pers.range + RESET)
    
def inicio():
    personagens = pg.Guerreiro(), pg.Arqueiro(), pg.Mago()
    return list(personagens)
  
inimigos = inicio()
herois = inicio()

print('='*50)
print (RED+'INIMIGOS'+RESET)
for i in inimigos:
    atributos(i)
    print('-'*30)

print('='*50)
print (GREEN+'HEROIS'+RESET)
for i in herois:
    atributos(i)
    print('-'*30)

print('='*50)
# Batalha
bt.batalha(inimigos,herois)
