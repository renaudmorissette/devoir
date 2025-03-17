from abc import ABC, abstractmethod


class Formes(ABC):
    def __init__(self, couleur="noire", rempli=False):
        self.couleur = couleur
        self.rempli = rempli

    @abstractmethod
    def aire(self):
        """Elle va retourner l'aire de la forme"""
        pass

    @abstractmethod
    def perimetre(self):
        pass
