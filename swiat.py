from Swiat.lis import Lis
from Swiat.antylopa import Antylopa
from Swiat.barszcz_sosnowskiego import BarszczSosnowskiego
from Swiat.czlowiek import Czlowiek
from Swiat.guarana import Guarana
from Swiat.kierunek import Kierunek
from Swiat.mlecz import Mlecz
from Swiat.owca import Owca
from Swiat.cyber_owca import CyberOwca
from Swiat.trawa import Trawa
from Swiat.wilcze_jagody import WilczeJagody
from Swiat.wilk import Wilk
from Swiat.zolw import Zolw
import pickle


class Swiat(object):

    def __init__(self):
        self._szerokosc=20
        self._wysokosc=20
        self.organizmy=[Lis(1, 2, self), Lis(17, 15, self), Wilk(4, 4, self), Wilk(17, 14, self), Wilk(19, 16, self), Antylopa(8, 7, self), Antylopa(10, 4, self), Antylopa(18, 19, self), Owca(5, 5, self), Owca(6, 9, self), Owca(16, 17, self), Zolw(9, 18, self), Zolw(19, 8, self), Zolw(19, 19, self), Czlowiek(10, 10, self), Guarana(3, 5, self), Guarana(15, 12, self), WilczeJagody(15, 10, self), BarszczSosnowskiego(3, 8, self), BarszczSosnowskiego(1, 8, self), BarszczSosnowskiego(18, 8, self), BarszczSosnowskiego(13, 1, self), Mlecz(16, 16, self), Trawa(7, 14, self), Trawa(17, 4, self), CyberOwca(7, 15, self), CyberOwca(19, 3, self)]
        self._noweorganizmy=[]
        self.kierunekCzlowieka = Kierunek.STOJ

    def wykonajTure(self):
        self.organizmy.sort(key=lambda o: (getattr(o, "_inicjatywa"), getattr(o, "_wiek"),), reverse=True)
        for o in  self.organizmy:
            if getattr(o, "_zycie") is True:
                o.zwiekszWiek()
                o.akcja()

        self.organizmy = [o for o in self.organizmy if getattr(o, "_zycie") is True]
        self.organizmy.extend(self._noweorganizmy)
        self._noweorganizmy.clear()
        self.kierunekCzlowieka = Kierunek.STOJ

    def dodajOrganizm(self, o):
        self._noweorganizmy.append(o)


    def czyKolizja(self, x, y):
        for o in self.organizmy:
            if getattr(o, "_x")==x and getattr(o, "_y")==y:
                return o
        return None

    # żeby nie razmnozały się poza planszą
    def sprawdzPole(self, x, y):
        if x >= 0 and x < self._szerokosc and y >= 0 and y < self._wysokosc:
            return True
        else:
            return False


    def zapiszStan(self):
        plik = open ("save.txt", "wb")
        for o in self.organizmy:
            o._swiat = None
        pickle.dump(self.organizmy, plik)
        print("Stan swiata zostal zapisany")
        for o in self.organizmy:
            o._swiat = self


    def wczytajStan(self):
        plik = open("save.txt", "rb")
        self.organizmy = pickle.load(plik)
        for o in self.organizmy:
            o._swiat = self
        print("Stan swiata zostal wczytany")


