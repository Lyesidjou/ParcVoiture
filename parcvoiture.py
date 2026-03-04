class Voiture:
    def __init__(self, matricule : str, marque : str, couleur : str):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur
    def afficher_informations(self):
        print(f"la voiture immatriculé {self.matricule} de la marque {self.marque} et couleur {self.couleur}")