from Swiat.roslina import Roslina


class Mlecz(Roslina):

    def __init__(self, x, y, swiat):
        super().__init__(0, x, y, swiat)
        self._color = '#FFFF00'

    def rozmnozSie(self, x, y):
        self._swiat.dodajOrganizm(Mlecz(x, y, self._swiat))
        print(type(self).__name__, "rozmnozyl sie")


    def akcja(self):
        for i in range(1, 3):
            super().akcja()
