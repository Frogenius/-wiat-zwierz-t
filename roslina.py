from random import randint
from Swiat.organizm import Organizm


class Roslina(Organizm):

    def __init__(self, sila, x, y, swiat):
        super().__init__(sila, 0, x, y, swiat)
        self._inicjatywa = 0


    def akcja(self):
        if randint(0, 9) == 0:
            mozliweMiejsce = randint(0, 7)
            if mozliweMiejsce == 0 and self._swiat.sprawdzPole(self._x+1, self._y) is True and self._swiat.czyKolizja(self._x+1, self._y) is None:
                self.rozmnozSie(self._x+1, self._y)
            if mozliweMiejsce == 1 and self._swiat.sprawdzPole(self._x+1, self._y+1) is True and self._swiat.czyKolizja(self._x+1, self._y+1) is None:
                self.rozmnozSie(self._x+1, self._y+1)
            if mozliweMiejsce == 2 and self._swiat.sprawdzPole(self._x, self._y+1) is True and self._swiat.czyKolizja(self._x, self._y+1) is None:
                self.rozmnozSie(self._x, self._y+1)
            if mozliweMiejsce == 3 and self._swiat.sprawdzPole(self._x+1, self._y-1) is True and self._swiat.czyKolizja(self._x+1, self._y-1) is None:
                self.rozmnozSie(self._x+1, self._y-1)
            if mozliweMiejsce == 4 and self._swiat.sprawdzPole(self._x, self._y-1) is True and self._swiat.czyKolizja(self._x, self._y-1) is None:
                self.rozmnozSie(self._x, self._y-1)
            if mozliweMiejsce == 5 and self._swiat.sprawdzPole(self._x-1, self._y-1) is True and self._swiat.czyKolizja(self._x-1, self._y-1) is None:
                self.rozmnozSie(self._x-1, self._y-1)
            if mozliweMiejsce == 6 and self._swiat.sprawdzPole(self._x-1, self._y) is True and self._swiat.czyKolizja(self._x-1, self._y) is None:
                self.rozmnozSie(self._x-1, self._y)
            if mozliweMiejsce == 7 and self._swiat.sprawdzPole(self._x-1, self._y+1) is True and self._swiat.czyKolizja(self._x-1, self._y+1) is None:
                self.rozmnozSie(self._x-1, self._y+1)


    def kolizja(self, o):
        return True




