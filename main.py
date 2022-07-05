# Bibliotecas
import personagens as pg # importas os personagens
from faker import Faker # Os dados fake para nome
from time import sleep # 
fake = Faker() 

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
    print(GREEN + 'Vida: ' + '■'*pers.vida)
    print(RED + 'Ataque: ' + '■'*pers.ataque)
    print(BLUE + 'Range: ' + '■'*pers.range + RESET)

# Batalha
def batalha(inimigos,herois):
    while (inimigos and herois):
        inimigos[0].vida -= herois[0].ataque
        inimigos[0].dano += herois[0].ataque
        herois[0].vida -= inimigos[0].ataque
        herois[0].dano += inimigos[0].ataque
        print(GREEN + f'Ataque Heroi: {herois[0].nome :<10} | {herois[0].ataque:<2} → Inimigo: {inimigos[0].nome:<9} | {inimigos[0].vida:<2}'+ '■'*(inimigos[0].vidaTotal-inimigos[0].dano)+'□'*inimigos[0].dano + RESET)
        print(RED + f'Ataque Inimigo: {inimigos[0].nome :<8} | {inimigos[0].ataque:<2} → Heroi: {herois[0].nome:<11} | {herois[0].vida:<2}'+ '■'*(herois[0].vidaTotal-herois[0].dano)+'□'*herois[0].dano+ RESET)

        if len(herois) >= 2: 
            if (herois[1].range >= 2):
                inimigos[0].vida -= herois[1].ataque
                inimigos[0].dano += herois[1].ataque
                print(GREEN + f'Ataque Heroi: {herois[1].nome :<10} | {herois[1].ataque:<2} → Inimigo: {inimigos[0].nome:<9} | {inimigos[0].vida:<2}'+ RESET)

        if len(inimigos) >= 2: 
            if (inimigos[1].range >= 2):
                herois[0].vida -= inimigos[1].ataque
                herois[0].dano += inimigos[1].ataque
                print(RED + f'Ataque Heroi: {inimigos[1].nome :<10} | {inimigos[1].ataque:<2} → Inimigo: {herois[0].nome:<9} | {herois[0].vida:<2}'+ RESET)                

        if inimigos[0].vida <= 0 :
            print('_'*60)
            print(f'INIMIGO {inimigos[0].nome} Morreu')
            inimigos.pop(0)
        if herois[0].vida <= 0 :
            print('_'*60)
            print(f'HEROI {herois[0].nome} Morreu')
            herois.pop(0)
        sleep(1)
        print('-'*60)
    
    if herois and not inimigos:
        print('Voce ganhou')
    elif inimigos and not herois:
        print('voce perdeu')
    else:
        print('empate')
    
def inicio():
    personagens = pg.Guerreiro(fake.first_name()), pg.Arqueiro(fake.first_name()), pg.Mago(fake.first_name())
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
batalha(inimigos,herois)
