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
            print(f"le nombre de places maintenant est de {self.CalculerNbrPlacesLibres()}")
    def sortir_voiture(self, voiture):
        if voiture in self.liste_voitures:
            self.liste_voitures.remove(voiture)
            print("la voiture est sortie du parc")
            print(f"le nombre de places maintenant est de {self.CalculerNbrPlacesLibres()}")
        else:
            print("la voiture n'existe pas dans le parc")
    def CalculerNbrPlacesLibres(self):
        return self.capacite - len(self.liste_voitures)
parc01=Parc("TO2026","2450 Rue Yonge",3)
v1=Voiture("GVHE234","TOYOTA","NOIRE")
v2=Voiture("Gsft543","HONDA","BLAMCHE")
v3=Voiture("XWX089","NISSAN","ROUGE")
parc01.entrer_voiture(v1)
parc01.entrer_voiture(v2)
parc01.entrer_voiture(v3)
parc01.sortir_voiture(v1)







