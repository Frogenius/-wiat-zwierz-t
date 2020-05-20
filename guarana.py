from Swiat.roslina import Roslina


class Guarana(Roslina):

    def __init__(self, x, y, swiat):
        super().__init__(0, x, y, swiat)
        self._color = '#0B6121'

    def rozmnozSie(self, x, y):
        self._swiat.dodajOrganizm(Guarana(x, y, self._swiat))
        print(type(self).__name__, "rozmnozyla sie")

    def kolizja(self, o):
        setattr(o, "_sila", (getattr(o, "_sila")+3))
        return True




