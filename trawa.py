from Swiat.roslina import Roslina


class Trawa(Roslina):

    def __init__(self, x, y, swiat):
        super().__init__(0, x, y, swiat)
        self._color = '#01DF01'

    def rozmnozSie(self, x, y):
        self._swiat.dodajOrganizm(Trawa(x, y, self._swiat))
        print(type(self).__name__, "rozmnozyla sie")

