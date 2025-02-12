class Rectangle:
    def __init__(self, largeur, long):
        self.largeur = largeur
        self.long = long

    @property
    def largeur(self):
        return self.largeur

    @property
    def long(self):
        return self.long

    @long.setter
    def long(self, value):
        if value > 0:
            self.long = value
        else:
            "La longueur doit être positif"
    @largeur.setter
    def largeur(self, valeur):
        if valeur > 0:
            self.largeur = valeur
        else:
            "Le largeur doit être positif"
    @property
    def surface(self):
        return self.largeur * self.long
    @property
    def perimetre(self):
        return 2 * (self.largeur + self.long)

mon_rect = Rectangle(200, 100)
print(mon_rect.surface)
print(mon_rect.perimetre)

