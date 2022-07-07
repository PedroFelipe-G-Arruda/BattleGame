from faker import Faker # Os dados fake para nome
import random

fake = Faker()

class Personagem:
  def __init__(self, nome):
    self.nome = nome
    self.bag = []
  
class Guerreiro(Personagem):
  def __init__(self):
    super().__init__(fake.first_name())
    self.classe = 'Guerreiro'
    self.forca = random.randint(8,10)
    self.agilidade = random.randint(4,6)
    self.inteligencia = random.randint(0,1)
    self.vida = int(self.forca*1)
    self.ataque = int(self.forca/2)
    self.defesa = int(self.agilidade/2)
    self.mana = int(self.inteligencia*2)
    self.vidaTotal = self.vida
    self.dano = 0
    self.range = 1
    

class Arqueiro(Personagem):
  def __init__(self):
    super().__init__(fake.first_name())
    self.classe = 'Arqueiro'
    self.forca = random.randint(4,6)
    self.agilidade = random.randint(8,10)
    self.inteligencia = random.randint(0,2)
    self.vida = int(self.forca*1)
    self.ataque = int(self.agilidade/2)
    self.defesa = int(self.agilidade/2)
    self.mana = int(self.inteligencia*2)
    self.vidaTotal = self.vida
    self.dano = 0
    self.range = 2
    

class Mago(Personagem):
  def __init__(self):
    super().__init__(fake.first_name())
    self.classe = 'Mago'
    self.forca = random.randint(2,4)
    self.agilidade = random.randint(2,4)
    self.inteligencia = random.randint(10,12)
    self.vida = int(self.forca*1)
    self.ataque = int(self.forca/2)
    self.defesa = int(self.agilidade/2)
    self.mana = int(self.inteligencia*2)
    self.vidaTotal = self.vida
    self.dano = 0
    self.range = 2
    


class Curandeiro(Personagem):
  def __init__(self):
    super().__init__(fake.first_name())
    self.classe = 'O Super Senhor Curandeiro'
    self.vida = random.randint(1,2)
    self.vidaTotal = self.vida
    self.ataque = random.randint(0,1)
    self.dano = 0
    self.range = 3
    