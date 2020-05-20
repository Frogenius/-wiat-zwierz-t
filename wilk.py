from Swiat.zwierze import Zwierze


class Wilk (Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(9, 5, x, y, swiat)
        self._color = '#585858'

    def rozmnozSie(self, x, y):
        self._swiat.dodajOrganizm(Wilk(x, y, self._swiat))
        print(type(self).__name__, "narodzil sie")