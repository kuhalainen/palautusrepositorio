class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._prev = None

    def miinus(self, operandi):
        self._prev = self._arvo
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._prev = self._arvo
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._prev = self._arvo
        self._arvo = 0

    def kumoa(self):
        self._arvo = self._prev

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
