
class Pokemon:
    
    def __init__(self, nom, pv, niveau, attaque, defense):
         self.__nom = nom
         self.pv = pv
         self.niveau = niveau
         niveau = 5
         pv = 100
         self.attaque = attaque
         attaque = 0
         self.defense = defense
         defense = 0

    def set_pv(self, pv):
         self.pv = pv

    def get_niveau(self):
         return self.pv


    def set_niveau(self, niveau):
         self.niveau = niveau
    def get_niveau(self):
         return self.niveau


    def set_attaque(self, attaque):
        self.attaque = attaque
    def get_attaque(self):
        return self.attaque

    def set_defense(self, defense):
        self.defense = defense
    def get_defense(self):
        return self.defense
    
   
    def bonjour(self):
        print("que le combat commence !")

    

    def offensive(self):
       print (x.nom, "utilise", x.capacite1)
       
       x.attaque = 20
       y.pv = y.pv - x.attaque
       print ("Il reste",y.pv , "PV au", y.nom, "adverse")
       check_ko(self)
       contre_offensive(self)

    def offensive2(self):
       print (x.nom, "utilise", x.capacite2)
       x.attaque = 40
       y.pv = y.pv - x.attaque
       print ("Il reste",y.pv , "PV au", y.nom, "adverse")
       check_ko(self)
       contre_offensive(self)

    
       


    def phase_attaque(self):
        mon_pokemon_adverse.y.pv -= mon_pokemon_allie.y.puissance1
        print (x.nom, x.pv)
        print (y.nom, y.pv)

    
         

    

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

#print(boite)       
for i in data['pokemon']:
    boite.append(i['nom'])
import random
#mon_pokemon = random.choice(boite)
#print(mon_pokemon)

#boite.remove(mon_pokemon)
#print(boite)

#mon_adversaire = random.choice(boite)
#print(mon_adversaire)
#boite.remove(mon_adversaire)
#print(boite)

mon_pokemon_test = random.choice(data['pokemon'])
print(mon_pokemon_test)

mon_adversaire_test = random.choice(data['pokemon'])
print(mon_adversaire_test)

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

new_datax = mon_pokemon_test
new_datax2 = json.dumps(new_datax)
new_datay = mon_adversaire_test
new_datay2 = json.dumps(new_datay)
x = json.loads(new_datax2, object_hook=lambda d: Namespace(**d))
y = json.loads(new_datay2, object_hook=lambda d: Namespace(**d))

print (x.nom, x.attaque, x.capacite2)
print (y.nom, y.attaque, y.capacite2)
mon_pokemon_allie = Pokemon(x.nom, x.niveau, x.pv, x.attaque, x.defense )
mon_pokemon_adverse = Pokemon(y.nom, y.niveau, y.pv, y.attaque, y.defense )


def contre_offensive(self):
       print (y.nom, "adverse utilise", y.capacite1)
       y.attaque = 20
       x.pv = x.pv - y.attaque
       print ("Il reste",x.pv , "PV au", x.nom)
       check_ko(self)

def check_ko(self):
        if x.pv <= 0:
         print("Le pokemon", x.nom, "est K.O.")
        elif y.pv <=0:
         print("Le pokemon", y.nom, "est K.O.")
        vainqueur(self)

def vainqueur(self):
       if x.pv <= 0:
         print ("Le pokemon", y.nom, "remporte le combat")
       elif y.pv <=0:
        print ("Le pokemon", x.nom, "remporte le combat")
