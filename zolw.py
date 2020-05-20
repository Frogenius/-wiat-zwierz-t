from Swiat.zwierze import Zwierze
from random import randint


class Zolw (Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(2, 1, x, y, swiat)
        self._color = '#61380B'

    def rozmnozSie(self, x, y):
        self._swiat.dodajOrganizm(Zolw(x, y, self._swiat))
        print(type(self).__name__, "narodzil sie")

    def kolizja(self, o):
        if super().kolizja(o) is False: #rozmnazanie
            return False
        elif getattr(o, "_sila") < 5:
            self._czyZwolnilPole = False
            return False
        else:
            return True

    def akcja(self):
        if randint(0, 3) == 0:
            super().akcja()
