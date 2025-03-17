from rectangle import Rectangle


def creer_rectangle():
    """Définir la fonction pour créer un rectangle"""

    while True:
        try:
            largeur = float(input("La largeur du rectangle: "))
            if largeur < 0:
                print("La largeur du rectangle doit être positive")
                continue
            break
        except ValueError:
            print("Veuillez entrez un nombre valide")

    while True:
        try:
            longueur = float(input("La longueur du rectangle: "))
            if longueur < 0:
                print("La longueur du rectangle doit être positive")
                continue
            break
        except ValueError:
            print("Veuillez entrez un nombre valide")

    return Rectangle(largeur, longueur)
