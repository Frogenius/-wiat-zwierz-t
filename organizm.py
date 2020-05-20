from abc import ABC, abstractmethod


class Organizm(ABC):

    def __init__(self, sila, inicjatywa, x, y, swiat):
        self._x = x
        self._y = y
        self._wiek = 0
        self._inicjatywa = inicjatywa
        self._sila = sila
        self._swiat = swiat
        self._niesmiertelny = False
        self._czyZwolnilPole = False
        self._zycie = True

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, o):
        pass

    @abstractmethod
    def rozmnozSie(self, x, y):
        pass

    def setCzyZwolnilPole (self, czy):
        self._czyZwolnilPole = czy

    def walka(self, o):
        if getattr(o, "_sila") > self._sila:
            self.zabij()
            self._czyZwolnilPole = True
            print(type(o).__name__, "zabil", type(self).__name__)
        else:
            o.zabij()
            setattr(o, "_czyZwolnilPole", True)
            print(type(self).__name__, "zabil", type(o).__name__)
            if type(o).__name__ == "Guarana":
                print("Sila", type(self).__name__, "zwiekszyla sie")

    def zabij(self):
        self._zycie = False
        self._czyZwolnilPole = True

    def zwiekszWiek(self):
        self._wiek += 1
