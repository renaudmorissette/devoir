import math
import unittest


class Cercle:
    def __init__(self, rayon):
        if rayon <= 0:
            raise ValueError("Le rayon doit être positif.")
        self.__rayon = rayon

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter
    def rayon(self, rayon):
        if rayon <= 0:
            raise ValueError("Le rayon doit être positif.")
        self.__rayon = rayon

    def changer_rayon(self, nouveau_rayon):
        if nouveau_rayon <= 0:
            raise ValueError("Le rayon doit être positif.")
        self.__rayon = nouveau_rayon

    def perimetre(self):
        return self.__rayon * math.pi * 2

    def aire(self):
        return self.__rayon ** 2 * math.pi


class TestCercle(unittest.TestCase):
    def setUp(self):
        self.cercle = Cercle(3)

    def tearDown(self):
        pass

    def test_creation_cercle(self):
        self.assertEqual(self.cercle.rayon, 3)

    def test_creation_cercle_invalide_rayon(self):
        with self.assertRaises(ValueError):
            Cercle(-9)

    def test_perimetre(self):
        perimetre_attendu = 2 * math.pi * 3
        self.assertAlmostEqual(self.cercle.perimetre(), perimetre_attendu)

    def test_aire(self):
        aire = 9 * math.pi
        self.assertAlmostEqual(self.cercle.aire(), aire)
