from models.cercle import Cercle
from models.rectangle import Rectangle
from models.groupe_formes import GroupeFormes


def creer_rectangle():
    """Définir la fonction pour créer un rectangle"""
    print("\n====Création d'un rectangle=====")
    couleur, rempli = saisir_couleur_remplissage()
    while True:
        try:
            largeur = float(input("Entrez la largeur SVP:"))
            if largeur < 0:
                print("La largeur doit être positive")
                continue
            break
        except ValueError:
            print("Veuillez entrez un nombre valide")

    while True:
        try:
            longueur = float(input("Entrez la longueur SVP:"))
            if longueur < 0:
                print("La longueur doit être positive")
                continue
            break
        except ValueError:
            print("Veuillez entrez un nombre valide")

    return Rectangle(couleur, rempli, largeur, longueur)


def creer_cercle():
    """Définir la fonction pour créer un cercle"""
    print("\n====Création d'un Cercle=====")
    couleur, rempli = saisir_couleur_remplissage()
    while True:
        try:
            rayon = float(input("Entrez le rayon SVP:"))
            if rayon < 0:
                print("Le rayon doit être positive")
                continue
            break
        except ValueError:
            print("Veuillez entrez un nombre valide")
    return Cercle(couleur, rempli, rayon)


def saisir_couleur_remplissage():
    """Fonction pour saisir la couleur et l'etat de remplissage"""
    couleur = input("Entrez le couleur du remplissage:")
    remplir_str = input("La forme est-elle rempli? (o/n)").lower()
    rempli = remplir_str == 'o' or remplir_str == 'oui'
    return couleur, rempli


def afficher_menu():
    """Fonction pour afficher la menu"""
    print("\n====MENU PRINCIPAL====")
    print("1. Ajouter un cercle")
    print("2. Ajouter un rectangle")
    print("3. Ajouter un triangle")
    print("4. Afficher les formes")
    print("5. Calculer l'aire totale")
    print("6. Éffectuer les opérations spéciales")
    print("0. Quitter")
    return input("Choississez une option \n")


def main():
    """Programme principal interactif"""
    print("Bienvenue dans le programme de gestion de formes géométriques!")

    # Creation d'un groupe de forme
    groupe = GroupeFormes()

    # Création d'un dictionnaire de formes spéciales pour des opérations spéciales
    formes_seciales = {'cercles': [], 'rectangles': [], 'triangles': []}

    while True:
        choix = afficher_menu()
        if choix == '0':
            print("Au revoir")
            break
        elif choix == '1':
            cercle = creer_cercle()
            groupe.ajouter(cercle)
            formes_seciales['cercles'].append(cercle)
            print("Cercle ajouté au groupe.")
        elif choix == '2':
            rectangle = creer_rectangle()
            groupe.ajouter(rectangle)
            formes_seciales['rectangles'].append(rectangle)
            print("Rectangle ajouté au groupe.")
        elif choix == '3':
            """Ajouter ici le code du triangle"""
            print("Triangle ajouté au groupe.")
        elif choix == '4':
            if len(groupe.formes) == 0:
                print("Aucune form dans le groupe.")
            else:
                print("\n===Formes dans le groupe===")
                for i, forme in enumerate(groupe, 1):
                    if isinstance(forme, Cercle):
                        type_forme = "Cercle"
                        taille = f"rayon={forme.rayon}"
                    elif isinstance(forme, Rectangle):
                        type_forme = "Rectangle"
                        taille = f"largeur={forme.largeur}, longueur={forme.longueur}"
                    else:
                        type_forme = "Forme inconnue"
                        Taille = ""
                    print(f"{i}. {type_forme} {taille}" +
                          f"({'rempli' if forme.rempli else 'nonrempli'})," +
                          f"{taille},aire={forme.aire():.2f}, perimètre={forme.perimetre():.2f}")
        elif choix == '5':
            if len(groupe.formes) == 0:
                print("Aucune forme dans le groupe.")
            else:
                print(f"\nAire totale de toutes les formes:{groupe.aire_totale():.2f}")
        elif choix == '6':
            print(f"\n===Démonstration des opérations spéciales")

            # Addition de cercles
            if len(formes_seciales['cercles']) > 2:
                c1 = formes_seciales['cercles'][0]
                c2 = formes_seciales['cercles'][1]
                print(f"Addition de deux cercles:{c1 + c2:.2f}")
            else:
                print("il faut au moins 2 cercles pour cet opération")

            # Addition de rectangles
            if len(formes_seciales['rectangles']) > 2:
                r1 = formes_seciales['rectangles'][0]
                r2 = formes_seciales['rectangles'][1]
                print(f"Addition de deux rectangles:{r1 + r2:.2f}")
            else:
                print("il faut au moins 2 rectangles pour cet opération")

            # Multiplication d'un rectangle
            if len(formes_seciales['rectangles']) >= 1:
                r = formes_seciales['rectangles'][0]
                facteur_mul = 2
                r_double = r * facteur_mul
                print(f"Rectangle{r.couleur} multiplié par {facteur_mul}:" +
                      f"largeur={r_double.largeur}, longueur={r_double.longueur}" +
                      f"aire={r_double.aire():.2f}")
            else:
                print("il faut au moins 1 rectangle pour cet opération")

                # Opération d'égalité de triangles
                """À completer par l'etudiant"""


        else:
            print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()






