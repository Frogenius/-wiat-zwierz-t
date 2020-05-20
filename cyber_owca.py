from Swiat.owca import Owca
from operator import itemgetter


class CyberOwca(Owca):

    def __init__(self, x, y, swiat):
        super().__init__(x, y, swiat)
        self._sila = 11
        self._cele = []
        self._color = '#01DFD7'

    def rozmnozSie(self, x, y):
        self._swiat.dodajOrganizm(CyberOwca(x, y, self._swiat))
        print(type(self).__name__, "narodzila sie")


    #specyfika kolizji jest w Barszczu
    #PS PO ODDANIU: a lepiej tu zrobic

    def akcja(self):
        for o in self._swiat.organizmy:
            if type(o).__name__ == "BarszczSosnowskiego":
                odleglosc = abs(getattr(o, "_x") - self._x) + abs(getattr(o, "_y") - self._y)
                cel = getattr(o, "_x"), getattr(o, "_y"), odleglosc     #tuple
                self._cele.append(cel)

        if not self._cele:  #empty list
            Owca.akcja(self)
        else:
            self._cele.sort(key=itemgetter(2)) #najmniejsza odleglosc
            #print("CELE OWCY", self._x, self._y)
            #print(self._cele)
            wKierunku = self._cele[0]
            tmp_x = self._x
            tmp_y = self._y
            if self._x < wKierunku[0]:
                tmp_x += 1
            elif self._x > wKierunku[0]:
                tmp_x -= 1
            elif self._y > wKierunku[1]:
                tmp_y -= 1
            elif self._y < wKierunku[1]:
                tmp_y += 1

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

        self._cele.clear()



