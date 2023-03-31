import tkinter as tk
from tkinter import*
from tkinter import messagebox

game = tk.Tk()
game.resizable(False, False)
game.title("Pokemon")
game.iconbitmap("pokeball.ico")


tk.Label(game, text="Pokemon", font=('Ariel', 25)).pack()
status_label = tk.Label(game, text="Lancer un combat !", font=('Ariel', 15), bg='red', fg='ivory')
status_label.pack(fill=tk.X)
game.geometry("500x500")


# canvas
canvas = Canvas(game, width=300, height=300, background='white')
photo = PhotoImage(file="charmander.png")
photo2 = PhotoImage(file="squirtle.png")
canvas.create_image(200, 50, anchor=NW, image=photo)
canvas.create_image(50, 250, anchor=NW, image=photo2)
canvas.pack()
canvas.pack()

player = 1
puissance = 0
def attack0():
      global puissance
      puissance = 20
      my_pokemon.phase_attaque()
def attack1():
     global puissance
     puissance = 40
     my_pokemon.phase_attaque()
def attack2():
     global puissance
     puissance = 90
     my_pokemon.phase_attaque()
def attack3():
     global puissance
     puissance = 120
     my_pokemon.phase_attaque()
class Combat:
    def __init__(self, pokemon):
        self.pokemon = pokemon

class Pokemon(Combat):
     global pv
     global niveau
     global attaque
     global defense
     global puissance
     global player
     def __init__(self,pokemon, type, pv,niveau, attaque, defense):
         Combat.__init__(self, pokemon)

         
         self.type = type
         self.pv = pv
         self.niveau = niveau
         niveau = 5
         pv = 100
         self.attaque = attaque
         self.defense = defense
        
     def set_pv(self):
        self.pv = pv
     def get_pv(self):
        self.pv = pv
    
     def set_niveau(self):
        self.niveau = niveau
     def get_niveau(self):
        self.niveau = niveau


     def set_attaque(self):
        self.attaque = attaque
     def get_attaque(self):
        self.attaque = attaque

     def set_attaque(self):
        self.defense = defense
     def get_defense(self):
        self.defense = defense

     def point_de_vie(self):
         if self.pv <= 0:
             print("le pokemon est ko")
             vainqueur()

     def vainqueur(self):
          print("fin du combat")
    
     def phase_attaque(self):
         global player
         global puissance
         if player == 1:
          my_pokemon.pv -= puissance
          status_label.configure(text="Votre pokemon attaque", bg='blue', fg='ivory')
          print("il reste", self.pv,"PV au", my_opponent.pokemon)
          if self.pv<=0:
              print("le pokemon est ko")
              
          player = 2
          phase_contre_attaque()
         
        
     def phase_contre_attaque(self):
         if player == 2:
          my_opponent.pv -=20
          status_label.configure(text="Le pokemon adverse attaque", bg='red', fg='ivory')
          print("il reste", self.pv,"PV au", my_pokemon.pokemon)
          
          if self.pv<=0:
              print("le pokemon est ko")
          player = 1
           
     def cri_de_guerre(self):
         print("A l'attaque !")
     

class Pouvoir(Combat):
    def __init__(self, puissance, type):
        self.puissance = puissance
        self.type = type 
    
    def charge(self):
        self.puissance = 40
        self.type = "Normal"
    def griffe(self):
        self.puissance = 40
        self.type = "Normal"
    def pistolet_a_O(self):
        self.puissance = 40
        self.type = "Eau"
    def flammeche(self):
        self.puissance = 40
        self.type = "Feu"



my_pokemon = Pokemon( "Carapuce", "Eau", 100, 5, 0, 0)   
my_opponent = Pokemon("Salamèche", "Feu", 100, 5, 0, 0)  
my_pokemon.cri_de_guerre()

button0 = tk.Button(game, text ="Charge",fg="black", bg='ivory', width=10, height=5,  command=attack0)
button0.place(x=50, y=380)

button1 = tk.Button(game, text ="Pistolet à Eau",fg="black", bg='skyblue', width=10, height=5,  command=attack1)
button1.place(x=150, y=380)

button2 = tk.Button(game, text ="Surf",fg="black", bg='skyblue', width=10, height=5,  command=attack2)
button2.place(x=250, y=380)

button3 = tk.Button(game, text ="Hydrocanon",fg="black", bg='skyblue', width=10, height=5,  command=attack3)
button3.place(x=350, y=380)

menubar = Menu(game)
game.config(menu=menubar)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Jouer contre un autre joueur")
menu1.add_command(label="Jouer contre l'ordinateur")
menu1.add_command(label="Niveau de l'ordinateur")
menu1.add_command(label="Recommencer")
menu1.add_separator()
menu1.add_command(label="Quitter", command=game.quit)
menubar.add_cascade(label="Options", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Score")
menu2.add_command(label="Historique")
menubar.add_cascade(label="Historique", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Règles du jeu")
menubar.add_cascade(label="Aide", menu=menu3)
game.mainloop()