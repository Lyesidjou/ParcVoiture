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
    def entrer_voiture(self, voiture):
        if voiture in self.liste_voitures:
            print("la voiture existe dans le parc on ne peut pas la rajouter")
        elif len(self.liste_voitures)>=self.capacite:
            print("la capacité du parc est atteinte")
        else:
            self.liste_voitures.append(voiture)




