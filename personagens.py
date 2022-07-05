import random
  
class Guerreiro:
  def __init__(self, nome):
    self.nome = nome
    self.classe = 'Guerreiro'
    self.vida = random.randint(4,6)
    self.vidaTotal = self.vida
    self.ataque = random.randint(1,3)
    self.dano = 0
    self.range = 1
    self.bag = []

class Arqueiro:
  def __init__(self, nome):
    self.nome = nome
    self.classe = 'Arqueiro'
    self.vida = random.randint(2,4)
    self.vidaTotal = self.vida
    self.ataque = random.randint(1,2)
    self.dano = 0
    self.range = 2
    self.bag = []

class Mago:
  def __init__(self, nome):
    self.nome = nome
    self.classe = 'Mago'
    self.vida = random.randint(1,3)
    self.vidaTotal = self.vida
    self.ataque = 1
    self.dano = 0
    self.range = 2
    self.bag = []


class Curandeiro:
  def __init__(self, nome):
    self.nome = nome
    self.classe = 'O Super Senhor Curandeiro'
    self.vida = random.randint(1,2)
    self.vidaTotal = self.vida
    self.ataque = random.randint(0,1)
    self.dano = 0
    self.range = 3
    self.bag = []