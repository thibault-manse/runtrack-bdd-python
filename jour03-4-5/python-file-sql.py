from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import mysql.connector
import sys
import traceback
#from customtkinter import ctk

#def affichage avec menu deroulant pour afficher sois tout sois certains produit specifique sous forme de liste

db = None
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Thibaultlou.13",
    database = "store"
    )
curseur = db.cursor()

def add(curseur):
    fenetre2 = Toplevel(fenetre)
    fenetre2.title("Gestion stock magasin")
    fenetre2.minsize(500, 300)

    label = Label(fenetre2, text="Hello world")

    entrer = StringVar()
    nom = Entry(fenetre2, textvariable = entrer, width = 50)
    entrer2 = StringVar()
    description = Entry(fenetre2, textvariable = entrer2, width = 50)
    prix = Spinbox(fenetre2, from_=0, to=100)
    quantite = Spinbox(fenetre2, from_=0, to=50)
    test = ["Nourriture", "Vetement", "Menager"]
    categorie = ttk.Combobox(fenetre2, values = test)
    categorie.current(0)
    boutonentrer = Button(fenetre2, text = "Entrer", command = lambda: ajouter(curseur, nom.get(), description.get(), prix.get(), quantite.get(), categorie.current()))


    label.pack()
    nom.pack(pady = 5)
    description.pack(pady = 5)
    prix.pack(pady = 5)
    quantite.pack(pady = 5)
    categorie.pack(pady = 5)
    boutonentrer.pack()

def ajouter(curseur, nom, description, prix, quantite, categorie):
    fenetre2 = Toplevel(fenetre)
    fenetre2.title("Gestion stock magasin")
    fenetre2.minsize(500, 300)

    libelle = Label(fenetre2, text = '')
    label.pack()

    index = categorie + 1
    try:
        requete = 'INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)'
        curseur = db.cursor()
        curseur.execute(requete, (nom, description, prix, quantite, index))
        db.commit()
        libelle.configure(text = 'Ajoue effectué')

    except Exception as e:
        libelle.configure(text='Une erreur inattendue est survenue.')
        traceback.print_exc(file=sys.stdout)


def suppr(curseur):
    fenetre2 = Toplevel(fenetre)
    fenetre2.title("Gestion stock magasin")
    fenetre2.minsize(500, 300)

    label = Label(fenetre2, text="Hello world")

    test = ["Nourriture", "Vetement", "Menager"]
    categorie = ttk.Combobox(fenetre2, values = test)
    categorie.current(0)
    boutonentrer = Button(fenetre2, text = "Entrer")

    label.pack()
    categorie.pack(pady = 5)
    boutonentrer.pack()

def mod(curseur):
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

def afficher(curseur): #afficher la liste dans une nouvelle fenetre ?
    fenetre2 = Toplevel(fenetre)
    fenetre2.title("Gestion stock magasin")
    fenetre2.minsize(500, 300)

    label = Label(fenetre2, text="Hello world")

    test = ["Nourriture", "Vetement", "Menager"]
    categorie = ttk.Combobox(fenetre2, values = test)
    categorie.current(0)
    boutonentrer = Button(fenetre2, text = "Entrer", command = lambda: maliste(categorie.current(), fenetre2, curseur))# commande = maliste(values, fenetre2)

    label.pack()
    categorie.pack(pady = 5)
    boutonentrer.pack()

def maliste(valeur, fenetre, curseur):
    fenetre2 = Toplevel(fenetre)
    fenetre2.title("Gestion stock magasin")
    fenetre2.minsize(500, 300)

    label = Label(fenetre2, text="Hello world")
    index = valeur + 1

    tableau = Treeview(fenetre2, columns=('id', 'nom', 'description', 'prix', 'quantite', 'categorie'))
    tableau.heading('id', text='id')
    tableau.heading('nom', text='Nom')
    tableau.heading('description', text='Description')
    tableau.heading('prix', text='Prix')
    tableau.heading('quantite', text='Quantité')
    tableau.heading('categorie', text='Catégorie')
    tableau['show'] = 'headings'
    tableau.pack(padx = 10, pady = (0, 10))

    libelle = Label(fenetre2, text = 'Produit')
    libelle.pack(padx = 10, pady = 10)

    try:
        requete = 'SELECT product.id, product.name, product.description, product.price, product.quantity, category.name FROM product INNER JOIN category ON product.id_category = category.id WHERE category.id = %s'
        curseur = db.cursor()
        curseur.execute(requete, (index,))
        resultat = curseur.fetchall()

        if len(resultat):
            for enreg in resultat:
                # chaque ligne n'a pas de parent, est ajoutée à la fin de la liste, utilise le champ id comme identifiant et on fournit les valeurs pour chacune des colonnes du tableau
                tableau.insert('', 'end', iid=enreg[0], values=(enreg[0], enreg[1], enreg[2], enreg[3], enreg[4], enreg[5]))
        else:
            libelle.configure(text = 'Il n\'y a aucun produit.')
            tableau.pack_forget()

    except mysql.OperationalError as e:
        if not db:
            libelle.configure('La connexion à la base de données a échoué.')
        else:
            libelle.configure(text='Il y a une erreur dans la requête SQL.')
        traceback.print_exc(file=sys.stdout)

    except Exception as e:
        libelle.configure(text='Une erreur inattendue est survenue.')
        traceback.print_exc(file=sys.stdout)

fenetre = Tk()

fenetre.title("Gestion stock magasin")
fenetre.minsize(500, 300)

label = Label(fenetre, text="Hello world")

bouton = Button(fenetre, text = "Ajouter", command = lambda : add(curseur))
bouton2 = Button(fenetre, text = "Supprimer", command = lambda : suppr(curseur))
bouton3 = Button(fenetre, text = "Modifier", command = lambda :mod(curseur))
bouton4 = Button(fenetre, text = "Afficher", command = lambda : afficher(curseur))

label.pack()
bouton.pack(pady=5)
bouton2.pack(pady=5)
bouton3.pack(pady=5)
bouton4.pack(pady=5)

fenetre.mainloop()