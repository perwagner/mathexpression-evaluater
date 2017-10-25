import unittest
from .Nom import Nom


class TestNom(unittest.TestCase):
    def test_init_1(self):
        nom = Nom(4)
        self.assertEqual(nom.nominator, 4)

    def test_add_1(self):
        nom = Nom(4)
        nom.add(Nom(5))
        self.assertEqual(nom.nominator, 9)

    def test_div(self):
        nom = Nom(4)
        nom.div(Nom(4))
        self.assertEqual(nom.nominator, 4)
        self.assertEqual(nom.denominator, 4)
