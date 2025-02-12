class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.__solde = solde_initial

    def deposer(self, montant_depot):
        """déposer montant au solde"""
        if montant_depot>0:
            self.__solde += montant_depot
        else:
            print("Montant à déposer doit être positif")

    def retirer(self, montant_retire):
        if 0 <= montant_retire < self.__solde:
            self.__solde -= montant_retire
        elif montant_retire>self.__solde:
            print("Fonds insuffisant")
        else:
            print("Le montant doit être positif")

    def afficher_solde(self):
        print(f"Solde actuel : {self.__solde}$")

compteBanc1 = CompteBancaire(1200)
compteBanc1.retirer(500)
compteBanc1.deposer(300)
compteBanc1.afficher_solde()
compteBanc1.retirer(200)
compteBanc1.afficher_solde()
