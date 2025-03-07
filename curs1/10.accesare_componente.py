
class Telefon:
    def __init__(self, anul_fabricatiei, memorie, imei):
        # atribut public
        self.memorie = memorie
        # atribut intern/protected
        self._anul_fabricatiei = anul_fabricatiei
        # atribut privat
        self.__imei = imei

telefon1 = Telefon(2020, 256, 4125312)
print(telefon1._anul_fabricatiei)

telefon1._anul_fabricatiei = "Inaintea erei noastre"
print(telefon1._anul_fabricatiei)

print(telefon1._Telefon__imei)

telefon1._Telefon__imei = "Alta valoare"
print(telefon1._Telefon__imei)