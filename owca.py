from Swiat.zwierze import Zwierze

class Owca (Zwierze):

    def __init__(self, x, y, swiat):
        super().__init__(4, 4, x, y, swiat)
        self._color = '#819FF7'

    def rozmnozSie(self, x, y):
        self._swiat.dodajOrganizm(Owca(x, y, self._swiat))
        print(type(self).__name__, "narodzila sie")
