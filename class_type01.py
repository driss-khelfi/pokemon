from class_pokemon01 import*

class Type(Pokemon):

    def __init__(self, nom, pv, niveau, attaque, defense, resistance, faiblesse):
        Pokemon.__init__(self, nom, pv, niveau, attaque, defense)
        self.resistance = resistance
        self.faiblesse = faiblesse

    def set_resistance(self):
         self.resistance = resistance
    def get_resistance(self):
         self.resistance = resistance

    def set_faiblesse(self):
         self.faiblesse = faiblesse
    def get_faiblesse(self):
         self.faiblesse = faiblesse

type_normal = ("Normal", "Feu")
type_plante = ("Eau", "Feu")
type_eau = ("Feu", "Plante")
type_feu = ("Plante", "Eau")

