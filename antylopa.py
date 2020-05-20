from Swiat.zwierze import Zwierze
from random import randint


class Antylopa (Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(4, 4, x, y, swiat)
        self._color = '#F7D358'

    def rozmnozSie(self, x, y):
        self._swiat.dodajOrganizm(Antylopa(x, y, self._swiat))
        print(type(self).__name__, "narodzila sie")


    def akcja(self):
        przesuniecie = randint(0, 3)
        tmp_x = self._x
        tmp_y = self._y
        if przesuniecie == 0 and self._swiat.sprawdzPole(self._x-2, self._y) == True:
            tmp_x -= 2
        if przesuniecie == 1 and self._swiat.sprawdzPole(self._x+2, self._y) == True:
            tmp_x += 2
        if przesuniecie == 2 and self._swiat.sprawdzPole(self._x, self._y-2) == True:
            tmp_y -= 2
        if przesuniecie == 3 and self._swiat.sprawdzPole(self._x, self._y+2) == True:
            tmp_y += 2

        if tmp_x != self._x or tmp_y != self._y:
            o = self._swiat.czyKolizja(tmp_x, tmp_y)
            if o is None:
                self._x = tmp_x
                self._y = tmp_y

            else:
                czyWalka = o.kolizja(self)
                if czyWalka is True:
                    print(type(self).__name__, "atakuje i walczy z", type(o).__name__)
                    self.walka(o)

                if getattr(o, "_czyZwolnilPole") is True and self._zycie is True:
                    self._x = tmp_x
                    self._y = tmp_y


    def kolizja(self, o):
        if super().kolizja(0) is False: #rozmnazanie
            return False
        else:
            if randint(0, 1) == 0:
                if self._swiat.czyKolizja(self._x-1, self._y) is None:
                    self._x -= 1
                    self._czyZwolnilPole = True
                    return False
                elif self._swiat.czyKolizja(self._x+1, self._y) is None:
                    self._x += 1
                    self._czyZwolnilPole = True
                    return False
                elif self._swiat.czyKolizja(self._x, self._y-1) is None:
                    self._y -= 1
                    self._czyZwolnilPole = True
                    return False
                elif self._swiat.czyKolizja(self._x, self._y+1) is None:
                    self._y += 1
                    self._czyZwolnilPole = True
                    return False
        return True
