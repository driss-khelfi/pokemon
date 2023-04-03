from class_pokemon03 import*

import tkinter as tk
from tkinter import*
from tkinter import messagebox
from random import*
from time import*
game = tk.Tk()
game.resizable(False, False)
game.title("Pokemon")
game.iconbitmap("pokeball.ico")

tk.Label(game, text="Pokemon", font=('Ariel', 25)).pack()
status_label = tk.Label(game, text="Lancer un combat !", font=('Ariel', 15), bg='red', fg='ivory')
status_label_adverse = tk.Label(game, text="Lancer un combat !", font=('Ariel', 15), bg='red', fg='ivory')
status_label_adverse.place(relx = 1,rely = 0.7,anchor ='ne')

pv_checker_allie = tk.Label(game,text=(x.nom, x.pv, "/100"), font=('Ariel', 10), bg='ivory', fg='black')
pv_checker_allie.place(relx = 0.95,rely = 0.9,anchor ='ne')
pv_checker_adverse = tk.Label(game,text=(y.nom, y.pv, "/100"), font=('Ariel', 10), bg='ivory', fg='black')
pv_checker_adverse.place(relx = 0.95,rely = 0.95,anchor ='ne')

status_label.pack(fill=tk.X)
game.geometry("500x600")


canvas = Canvas(game, width=300, height=300, background='white')
photo_bulbasaur = PhotoImage(file="bulbasaur.png")
photo_bulbasaur_back = PhotoImage(file="bulbasaur_back.png")
photo_charmander = PhotoImage(file="charmander.png")
photo_charmander_back = PhotoImage(file="charmander_back.png")
photo_squirtle = PhotoImage(file="squirtle.png")
photo_squirtle_back = PhotoImage(file="squirtle_back.png")
photo_eevee = PhotoImage(file="eevee.png")
photo_eevee_back = PhotoImage(file="eevee_back.png")
def display():
 if y.nom == "Bulbizarre":
  canvas.create_image(200, 50, anchor=NW, image=photo_bulbasaur)
  canvas.pack()
 if y.nom == "Salameche":
  canvas.create_image(200, 50, anchor=NW, image=photo_charmander)
  canvas.pack()
 if y.nom == "Carapuce":
  canvas.create_image(200, 50, anchor=NW, image=photo_squirtle)
  canvas.pack()
 if y.nom == "Evoli":
  canvas.create_image(200, 50, anchor=NW, image=photo_eevee)
  canvas.pack()

 if x.nom == "Bulbizarre":
  canvas.create_image(50, 250, anchor=NW, image=photo_bulbasaur_back)
  canvas.pack()
 if x.nom == "Salameche":
  canvas.create_image(50, 250, anchor=NW, image=photo_charmander_back)
  canvas.pack()
 if x.nom == "Carapuce":
  canvas.create_image(50, 250, anchor=NW, image=photo_squirtle_back)
  canvas.pack()
 if x.nom == "Evoli":
  canvas.create_image(50, 250, anchor=NW, image=photo_eevee_back)
  canvas.pack()


  

display()
mon_pokemon_allie.bonjour()
#mon_pokemon_allie.offensive()
#mon_pokemon_allie.contre_offensive()
#mon_pokemon_allie.offensive()
#mon_pokemon_allie.contre_offensive()
#mon_pokemon_allie.offensive()
#mon_pokemon_allie.contre_offensive()
#mon_pokemon_allie.offensive()
#mon_pokemon_allie.contre_offensive()
def text_offensive():
 
 status_label.configure(text=(x.nom, "utilise", x.capacite1), bg='blue', fg='ivory')
 pv_checker_adverse.configure(text=(y.nom, y.pv, "/100"),font=('Ariel', 10), bg='red', fg='ivory')
 pv_checker_allie.configure(text=(x.nom, x.pv, "/100"),font=('Ariel', 10), bg='blue', fg='ivory')
 status_label_adverse.configure(text=(y.nom, "adverse utilise", y.capacite2), bg='red', fg='ivory')
 text_ko()

def text_offensive2():
 import time
 status_label.configure(text=(x.nom, "utilise", x.capacite2), bg='blue', fg='ivory')
 pv_checker_adverse.configure(text=(y.nom, y.pv, "/100"),font=('Ariel', 10), bg='red', fg='ivory')
 pv_checker_allie.configure(text=(x.nom, x.pv, "/100"),font=('Ariel', 10), bg='blue', fg='ivory')
 status_label_adverse.configure(text=(y.nom, "adverse utilise", y.capacite2), bg='red', fg='ivory')
 text_ko()

def text_ko():
 if y.pv <=0:
  y.pv == 0
  status_label.configure(text=("Le pokémon", x.nom, "remporte le combat !"), bg='green', fg='ivory')
  status_label_adverse.configure(text=("Le pokémon", y.nom, "adverse est K.O. !"), bg='red', fg='ivory')
 elif x.pv <=0:
  x.pv == 0
  status_label.configure(text=("Le pokémon", x.nom, " est K.O. !"), bg='red', fg='ivory')
  status_label_adverse.configure(text=("Le pokémon", y.nom, "adverse remporte le combat !"), bg='red', fg='ivory')

button0 = tk.Button(game, text =x.capacite1,fg="black", bg='ivory', width=10, height=5  ,command=lambda:[mon_pokemon_allie.offensive(), text_offensive()])
button0.place(x=50, y=480)

button1 = tk.Button(game, text = x.capacite2,fg="black", bg='ivory', width=10, height=5, command=lambda:[mon_pokemon_allie.offensive2(), text_offensive2()] )
button1.place(x=150, y=480)


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