from models.formes import Formes

class Rectangle(Formes):
    def __init__(self, couleur="rouge",rempli=False, largeur=1.0, longueur=2.0):
        super().__init__(couleur, rempli)
        self.largeur = largeur
        self.longueur = longueur

    def aire(self):
        return self.largeur * self.longueur

    def perimetre(self):
        return 2*(self.largeur + self.longueur)

    def __add__(self, autre):
        if isinstance(autre, Rectangle):
            return self.aire() + autre.aire()
        else:
            raise TypeError("")

    def __mul__(self, nb):
        if isinstance(nb, (int, float)):
            return Rectangle(
                self.couleur,
                self.rempli,
                self.largeur*nb,
                self.longueur*nb)
        else:
            raise TypeError("")

