from __future__ import print_function
from class_pokemon01 import Pokemon
from class_type01 import Type
from random import*
from types import SimpleNamespace



global niveau
global attaque
global defense


class Combat:
      
    def __init__(self, nom, pv, niveau, attaque, defense, resistance, faiblesse  ):
        Pokemon.__init__(self, nom, pv, niveau, attaque, defense)
        Type.__init__(self, resistance, faiblesse)

    def ko(self):
        if self.pv <= 0:
         print("Le pokemon", self.nom, "est K.O.")
         vainqueur()
         

    def vainqueur(self):
       if self.pv >= 0:
         print ("Le pokemon", self.nom, "remporte le combat")

    def check_type(self):
       print (mon_pokemon.get_type())
       puissance = mon_pokemon.get_type()
       if coefficient == "Normal":
          print("ce pokemon est de type normal")
       elif coefficient == "Plante":
          print("ce pokemon est de type plante")
       elif coefficient == "Feu":
          print("ce pokemon est de type feu")
       elif coefficient == "Eau":  
          print("ce pokemon est de type eau")

    def degats(self):
       coup = (attaque + puissance)*coefficient - defense
       if coup <= 0:
          coup == 1
    
    def perdant(self):
       print ("Le pokemon", self.nom, "perd le combat")

    def combat(self):
       print("que le combat commence !")
boite = []

import json
with open('pokedex02.json') as json_file:
	data = json.load(json_file)
#print(data['pokemon'][0])

for i in data['pokemon']:
	print("nom:", i['nom'])
	print("niveau:", i['niveau'])
	print("pv:", i['pv'])
	print("attaque:", i['attaque'])
	print("defense:", i['defense'])
	print("resistance:", i['resistance'])
	print("faiblesse:", i['faiblesse'])
	print("capacite1", i['capacite1'])

print(boite)       
for i in data['pokemon']:
    boite.append(i['nom'])
import random
mon_pokemon = random.choice(boite)
print(mon_pokemon)



boite.remove(mon_pokemon)
print(boite)

mon_adversaire = random.choice(boite)
print(mon_adversaire)
boite.remove(mon_adversaire)
print(boite)

mon_pokemon_test = random.choice(data['pokemon'])
print(mon_pokemon_test)



try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

new_data = mon_pokemon_test
new_data2 = json.dumps(new_data)
x = json.loads(new_data2, object_hook=lambda d: Namespace(**d))

print (x.nom, x.attaque, x.capacite2)
mon_pokemon_favori = Pokemon(x.nom, x.niveau, x.pv, x.attaque, x.defense )





		
	
  




       