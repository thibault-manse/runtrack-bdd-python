from tkinter import *
from tkinter import ttk
#from customtkinter import ctk

#def affichage avec menu deroulant pour afficher sois tout sois certains produit specifique sous forme de liste

def add():
    fenetre2 = Toplevel(fenetre)
    fenetre2.title("Gestion stock magasin")
    fenetre2.minsize(500, 300)

    label = Label(fenetre2, text="Hello world")

    entrer = StringVar()
    entrer = Entry(fenetre2, textvariable = entrer, width = 50)
    entrer2 = StringVar()
    entrer2 = Entry(fenetre2, textvariable = entrer2, width = 50)
    prix = Spinbox(fenetre2, from_=0, to=100)
    quantite = Spinbox(fenetre2, from_=0, to=50)
    test = ["Bille", "Boule", "Ballon"]
    categorie = ttk.Combobox(fenetre2, values = test)
    categorie.current(0)
    boutonentrer = Button(fenetre2, text = "Entrer")


    label.pack()
    entrer.pack(pady = 5)
    entrer2.pack(pady = 5)
    prix.pack(pady = 5)
    quantite.pack(pady = 5)
    categorie.pack(pady = 5)
    boutonentrer.pack()

def suppr():
    fenetre2 = Toplevel(fenetre)
    fenetre2.title("Gestion stock magasin")
    fenetre2.minsize(500, 300)

    label = Label(fenetre2, text="Hello world")

    test = ["Bille", "Boule", "Ballon"]
    categorie = ttk.Combobox(fenetre2, values = test)
    categorie.current(0)
    boutonentrer = Button(fenetre2, text = "Entrer")

    label.pack()
    categorie.pack(pady = 5)
    boutonentrer.pack()

def mod():
    fenetre2 = Toplevel(fenetre)
    fenetre2.title("Gestion stock magasin")
    fenetre2.minsize(500, 300)

    label = Label(fenetre2, text="Hello world")

    test = ["Bibi", "Bobo", "Baba"]
    categorie = ttk.Combobox(fenetre2, values = test)
    categorie.current(0)
    entrer = StringVar()
    entrer = Entry(fenetre2, textvariable = entrer, width = 50)
    entrer2 = StringVar()
    entrer2 = Entry(fenetre2, textvariable = entrer2, width = 50)
    prix = Spinbox(fenetre2, from_=0, to=100)
    quantite = Spinbox(fenetre2, from_=0, to=50)
    test = ["Bille", "Boule", "Ballon"]
    categorie2 = ttk.Combobox(fenetre2, values = test)
    categorie2.current(0)
    boutonentrer = Button(fenetre2, text = "Entrer")


    label.pack()
    categorie2.pack(pady = 5)
    entrer.pack(pady = 5)
    entrer2.pack(pady = 5)
    prix.pack(pady = 5)
    quantite.pack(pady = 5)
    categorie.pack(pady = 5)
    boutonentrer.pack()

def afficher(): #afficher la liste dans une nouvelle fenetre ?
    fenetre2 = Toplevel(fenetre)
    fenetre2.title("Gestion stock magasin")
    fenetre2.minsize(500, 300)

    label = Label(fenetre2, text="Hello world")

    test = ["Bille", "Boule", "Ballon"]
    categorie = ttk.Combobox(fenetre2, values = test)
    categorie.current(0)
    boutonentrer = Button(fenetre2, text = "Entrer")

    label.pack()
    categorie.pack(pady = 5)
    boutonentrer.pack()

fenetre = Tk()

fenetre.title("Gestion stock magasin")
fenetre.minsize(500, 300)

label = Label(fenetre, text="Hello world")

bouton = Button(fenetre, text = "Ajouter", command = add)
bouton2 = Button(fenetre, text = "Supprimer", command = suppr)
bouton3 = Button(fenetre, text = "Modifier", command = mod)
bouton4 = Button(fenetre, text = "Afficher", command = afficher)

label.pack()
bouton.pack(pady=5)
bouton2.pack(pady=5)
bouton3.pack(pady=5)
bouton4.pack(pady=5)

fenetre.mainloop()