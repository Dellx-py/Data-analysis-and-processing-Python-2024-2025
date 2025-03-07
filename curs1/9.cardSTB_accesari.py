

class CardSTB:
    VALOARE_CALATORIE = 3
    def __init__(self, nume = "Nenominal", calatorii = 0, credit = 0):
        self.nume = nume
        self.calatorii = calatorii
        self.credit = credit
    def __str__(self):
        return f"{self.nume} are {self.calatorii} calatorii si {self.credit} lei credit"

    def validare_calatorie (self):
        if self.calatorii:
            self.calatorii -= 1
        elif self.credit >= CardSTB.VALOARE_CALATORIE:
            self.credit -= CardSTB.VALOARE_CALATORIE
        else:
            print("Esti pe blat!!!")

    def reincarcare_calatorii(self, calatorii_noi):
        self.calatorii += calatorii_noi

    def reincarcare_credit(self, credit):
        self.credit += credit

card = CardSTB
print(card)
card.validare_calatorie()

card.calatorii = 3
print(card)
card.validare_calatorie()
print(card)



