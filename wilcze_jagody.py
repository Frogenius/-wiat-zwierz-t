from Swiat.roslina import Roslina


class WilczeJagody(Roslina):

    def __init__(self, x, y, swiat):
        super().__init__(99, x, y, swiat)
        self._color = '#2A0A22'

    def rozmnozSie(self, x, y):
        self._swiat.dodajOrganizm(WilczeJagody(x, y, self._swiat))
        print(type(self).__name__, "rozmnozyly sie")


    def kolizja(self, o):
        if getattr(o, "_niesmiertelny") is True:
            self.zabij()
            print("Czlowiek (SuperPower is ON) zjadl", type(self).__name__, "i zyje sobie dalej")
        else:
            o.zabij()
            self.zabij()
            print(type(o).__name__, "zjadl", type(self).__name__, "i umarl")

        return False
