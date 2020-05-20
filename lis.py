from Swiat.zwierze import Zwierze
from random import randint

class Lis(Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(3, 7, x,y,swiat)
        self._color = '#FF8000'

    def rozmnozSie(self, x, y):
        self._swiat.dodajOrganizm(Lis(x,y, self._swiat))
        print(type(self).__name__, "narodzil sie")

    def akcja(self):
        przesuniecie = randint(0, 3)
        tmp_x=self._x
        tmp_y=self._y
        if przesuniecie == 0 and self._x>0:
            tmp_x-=1
        if przesuniecie == 1 and self._x < getattr(self._swiat,"_szerokosc")-1:
            tmp_x+=1
        if przesuniecie == 2 and self._y > 0:
            tmp_y-=1
        if przesuniecie == 3 and self._y <  getattr(self._swiat,"_wysokosc")-1:
            tmp_y+=1

        if tmp_x!=self._x or tmp_y!=self._y:
            o = self._swiat.czyKolizja(tmp_x, tmp_y)
            if o is None:
                self._x=tmp_x
                self._y=tmp_y
            elif getattr(o,"_sila")>self._sila:
                return
            else:
                czyWalka = o.kolizja(self)
                if czyWalka is True:
                    print(type(self).__name__, "atakuje i walczy z", type(o).__name__)
                    self.walka(o)

                if getattr(o, "_czyZwolnilPole") and self._zycie is True:
                    self._x=tmp_x
                    self._y=tmp_y




