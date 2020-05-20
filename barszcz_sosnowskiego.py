from Swiat.roslina import Roslina
from random import randint


class BarszczSosnowskiego(Roslina):

    def __init__(self, x, y, swiat):
        super().__init__(10, x, y, swiat)
        self._color = '#50026A'

    def rozmnozSie(self, x, y):
        self._swiat.dodajOrganizm(BarszczSosnowskiego(x, y, self._swiat))
        print(type(self).__name__, "rozmnozyl sie")

    def kolizja(self, o):
        if getattr(o, "_niesmiertelny") is True:
            self.zabij()
            print("Czlowiek (SuperPower is ON) zjadl", type(self).__name__, "i zyje sobie dalej")
        elif type(o).__name__ == "CyberOwca":
            self.zabij()
            print(type(o).__name__, "zjadla", type(self).__name__, "^_^")
        else:
            o.zabij()
            self.zabij()
            print(type(o).__name__, "zjadl", type(self).__name__, "i umarl")
        return False

    def akcja(self):

        sasiad = self._swiat.czyKolizja(self._x + 1, self._y)
        if sasiad is not None and type(sasiad).__name__ != "CyberOwca" and getattr(sasiad, "_niesmiertelny") is False:
            sasiad.zabij()
            print(type(self).__name__, "zabil", type(sasiad).__name__)

        sasiad = self._swiat.czyKolizja(self._x + 1, self._y + 1)
        if sasiad is not None and type(sasiad).__name__ != "CyberOwca" and getattr(sasiad, "_niesmiertelny") is False:
            sasiad.zabij()
            print(type(self).__name__, "zabil", type(sasiad).__name__)

        sasiad = self._swiat.czyKolizja(self._x, self._y + 1)
        if sasiad is not None and type(sasiad).__name__ != "CyberOwca" and getattr(sasiad, "_niesmiertelny") is False:
            sasiad.zabij()
            print(type(self).__name__, "zabil", type(sasiad).__name__)

        sasiad = self._swiat.czyKolizja(self._x + 1, self._y - 1)
        if sasiad is not None and type(sasiad).__name__ != "CyberOwca" and getattr(sasiad, "_niesmiertelny") is False:
            sasiad.zabij()
            print(type(self).__name__, "zabil", type(sasiad).__name__)

        sasiad = self._swiat.czyKolizja(self._x - 1, self._y - 1)
        if sasiad is not None and type(sasiad).__name__ != "CyberOwca" and getattr(sasiad, "_niesmiertelny") is False:
            sasiad.zabij()
            print(type(self).__name__, "zabil", type(sasiad).__name__)

        sasiad = self._swiat.czyKolizja(self._x - 1, self._y)
        if sasiad is not None and type(sasiad).__name__ != "CyberOwca" and getattr(sasiad, "_niesmiertelny") is False:
            sasiad.zabij()
            print(type(self).__name__, "zabil", type(sasiad).__name__)

        sasiad = self._swiat.czyKolizja(self._x - 1, self._y + 1)
        if sasiad is not None and type(sasiad).__name__ != "CyberOwca" and getattr(sasiad, "_niesmiertelny") is False:
            sasiad.zabij()
            print(type(self).__name__, "zabil", type(sasiad).__name__)

        sasiad = self._swiat.czyKolizja(self._x, self._y - 1)
        if sasiad is not None and type(sasiad).__name__ != "CyberOwca" and getattr(sasiad, "_niesmiertelny") is False:
            sasiad.zabij()
            print(type(self).__name__, "zabil", type(sasiad).__name__)


