from Swiat.zwierze import Zwierze
from Swiat.kierunek import Kierunek


class Czlowiek(Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(5, 4, x, y, swiat)
        self._licznik_umiejetnosci = 0
        self._color = '#DF013A'

    def rozmnozSie(self, x, y):
        return

    def kolizja(self, o):
        if self._niesmiertelny is True:
            super().akcja()
            self._czyZwolnilPole = True
            return False
        else:
            return True

    def obsluga_umiejetnosci(self):
        if self._licznik_umiejetnosci > 0: #kiedy licznik==0, moze byc ponownie wlaczona
            self._licznik_umiejetnosci -= 1

        if self._licznik_umiejetnosci == 5:
            self._niesmiertelny = False
            print("NIESMIERTELNOSC C zostala wylaczona")


    def walka(self, o):
        #if niesm-ny==true, walka nie odbedzie sie
        if self._niesmiertelny is False:
            if getattr(o, "_sila") > self._sila:
                self.zabij()
                self._czyZwolnilPole = True
            else:
                o.zabij()


    def akcja(self):
        self.obsluga_umiejetnosci()

        przesuniecie = getattr(self._swiat, "kierunekCzlowieka")
        if przesuniecie == Kierunek.STOJ:
            return
        elif przesuniecie == Kierunek.NIESMIERTELNOSC and self._licznik_umiejetnosci == 0:
            self._niesmiertelny = True
            self._licznik_umiejetnosci = 10
            print("NIESMIERTELNOSC C jest wlaczona")
        else:
            tmp_x = self._x
            tmp_y = self._y
            if przesuniecie == Kierunek.LEWO and self._x > 0:
                tmp_x -= 1
            if przesuniecie == Kierunek.PRAWO and self._x < getattr(self._swiat, "_szerokosc")-1:
                tmp_x += 1
            if przesuniecie == Kierunek.GORA and self._y > 0:
                tmp_y -= 1
            if przesuniecie == Kierunek.DOL and self._y < getattr(self._swiat, "_wysokosc")-1:
                tmp_y += 1

            if tmp_x != self._x or tmp_y != self._y:
                # czy jest wolne dla przesuniecia
                o = self._swiat.czyKolizja(tmp_x, tmp_y)
                if o is None:
                    self._x = tmp_x
                    self._y = tmp_y
                else:
                    czyWalka = o.kolizja(self)
                    if czyWalka is True:
                        self.walka(o)
                    if getattr(o, "_czyZwolnilPole") is True and self._zycie is True:
                        self._x = tmp_x
                        self._y = tmp_y



