import mysql.connector

request = "SELECT nom, capacite FROM salle"
request2 = "SELECT superficie FROM etage"

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Thibaultlou.13",
  database = "LaPlateforme"
)

class Employer:
    def __init__(self, nom, prenom, salaire, id_service):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service

    def add_employer(self):
        request = "INSERT INTO employer (nom, prenom, salaire, id_service) VALUES ('{nom}', '{prenom}', {salaire}, {id_service})".format(nom = self.nom, prenom = self.prenom, salaire = self.salaire, id_service = self.id_service)
        cursor = db.cursor()
        cursor.execute(request)
        db.commit()


add = Employer('Minier', 'Julie', 3500, 1)
add.add_employer()
#cursor = db.cursor()
#cursor2 = db.cursor()

#cursor.execute(request)
#cursor2.execute(request2)

#rows = cursor.fetchall()
#rows2 = cursor2.fetchall()
#for row in rows:
#    print("{0} - {1}".format(row[0], row[1]))

#cap = 0
#for row in rows2:
#    cap = cap + row[0]
    
#print(cap)

#cap = 0
#for row in rows:
#    cap = cap + row[1]
    
#print(sup)
    
db.close()