class Voiture:
    def __init__(self, matricule : str, marque : str, couleur : str):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur
    def afficher_informations(self):
        print(f"la voiture immatriculé {self.matricule} de la marque {self.marque} et couleur {self.couleur}")
class Parc:
    def __init__(self, id:int , adresse : str, capacite : int):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.liste_voitures=[]

