from random import randint
from Swiat.organizm import Organizm


class Zwierze(Organizm):

    def __init__(self, sila, inicjatywa, x, y, swiat):
        super().__init__(sila,inicjatywa,x,y,swiat)

    def akcja(self):
        przesuniecie = randint(0, 3)
        tmp_x = self._x
        tmp_y = self._y
        if przesuniecie == 0 and self._x > 0:
            tmp_x-=1
        if przesuniecie == 1 and self._x < getattr(self._swiat, "_szerokosc")-1:
            tmp_x+=1
        if przesuniecie == 2 and self._y > 0:
            tmp_y-=1
        if przesuniecie == 3 and self._y <  getattr(self._swiat, "_wysokosc")-1:
            tmp_y+=1

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

                if getattr(o, "_czyZwolnilPole") and self._zycie is True:
                    self._x = tmp_x
                    self._y = tmp_y


    #false - nie mozna walczyc
    def kolizja(self, o):
        if type(self).__name__ == type(o).__name__:
            if self._swiat.sprawdzPole(self._x-1,self._y) is True and self._swiat.czyKolizja(self._x-1, self._y) is None:
                self.rozmnozSie(self._x-1, self._y)
            elif self._swiat.sprawdzPole(self._x-1,self._y-1) is True and self._swiat.czyKolizja(self._x-1, self._y-1) is None:
                self.rozmnozSie(self._x-1, self._y-1)
            elif self._swiat.sprawdzPole(self._x+1,self._y) is True and self._swiat.czyKolizja(self._x+1, self._y) is None:
                self.rozmnozSie(self._x+1, self._y)
            elif self._swiat.sprawdzPole(self._x+1,self._y+1) is True and self._swiat.czyKolizja(self._x+1, self._y+1) is None:
                self.rozmnozSie(self._x+1, self._y+1)
            elif self._swiat.sprawdzPole(self._x,self._y) is True and self._swiat.czyKolizja(self._x, self._y) is None:
                self.rozmnozSie(self._x, self._y)
            elif self._swiat.sprawdzPole(self._x,self._y-1) is True and self._swiat.czyKolizja(self._x, self._y-1) is None:
                self.rozmnozSie(self._x, self._y-1)
            elif self._swiat.sprawdzPole(self._x+1,self._y-1) is True and self._swiat.czyKolizja(self._x+1, self._y-1) is None:
                self.rozmnozSie(self._x+1, self._y-1)
            elif self._swiat.sprawdzPole(self._x-1,self._y+1) is True and self._swiat.czyKolizja(self._x-1, self._y+1) is None:
                self.rozmnozSie(self._x-1, self._y+1)

            self._czyZwolnilPole = False
            return False
        else:
            return True
