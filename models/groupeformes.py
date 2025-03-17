from models.formes import Formes

class GroupeFormes:
    def __init__(self, malisteformes=None):
        self.formes = []

        if malisteformes is not None:
            for forme in malisteformes:
                self.ajouter(forme)
    def ajouter(self, forme):

        if not isinstance(forme, Formes):
            raise TypeError("L'objet doit être une instance de la forme")
        self.formes.append(forme)

    def aire_totale(self):
        return sum(forme.aire() for forme in self.formes)

    def __iter__(self):
        return iter(self.formes)
