class Pokemon:
    global niveau
    global attaque
    global defense
    
    def __init__(self, nom, pv, niveau, attaque, defense):
         self.__nom = nom
         self.__pv = pv
         self.niveau = niveau
         niveau = 5
         pv = 100
         self.attaque = attaque
         attaque = 0
         self.defense = defense
         defense = 0

    def set_niveau(self):
         self.niveau = niveau
    def get_niveau(self):
         self.niveau = niveau


    def set_attaque(self):
        self.attaque = attaque
    def get_attaque(self):
        self.attaque = attaque

    def set_defense(self):
        self.defense = defense
    def get_defense(self):
        self.defense = defense

pokemon1 = Pokemon("Bulbizarre", 100, 5, 0, 0)
pokemon2 = Pokemon("Salamèche", 100, 5, 0, 0)
pokemon3 = Pokemon("Carapuce", 100, 5, 0, 0)
pokemon4 = Pokemon("Evoli", 100, 5, 0, 0 )