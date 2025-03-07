

class STBCard:
    def __init__(self, nume=None, calatorii_disponibile=0, credit_disponibil=0.0):
        """
        Constructor pentru cardul STB.
        :param nume: Numele detinatorului cardului, daca nu se furnizeaza, se va seta la "Nenominal".
        :param calatorii_disponibile: Numărul de călătorii disponibile pe card.
        :param credit_disponibil: Creditul disponibil pe card (în lei).
        """
        self.nume = nume if nume else "Nenominal"  # Setează numele sau "Nenominal" dacă nu este furnizat.
        self.calatorii_disponibile = calatorii_disponibile
        self.credit_disponibil = credit_disponibil

    def validare_calatorie_credit(self):
        """Validare călătorie cu credit (scade 3 lei din credit și o călătorie)."""
        cost_calatorie = 3  # Costul unei călătorii este 3 lei
        if self.credit_disponibil >= cost_calatorie:
            if self.calatorii_disponibile > 0:
                # Dacă sunt călătorii disponibile și suficient credit, se scade creditul și o călătorie
                self.credit_disponibil -= cost_calatorie
                self.calatorii_disponibile -= 1
                print("Călătoria a fost validată cu succes! 3 lei au fost scăzuți din credit și o călătorie a fost folosită.")
            else:
                # Dacă nu mai sunt călătorii, dar există credit
                print("Nu mai aveți călătorii disponibile. Folosiți creditul pentru validare.")
                self.credit_disponibil -= cost_calatorie
                print("Călătoria a fost validată cu succes doar cu credit. 3 lei au fost scăzuți din credit.")
        else:
            print("Nu aveți suficient credit pentru a valida o călătorie.")

    def validare_calatorie(self):
        """Validare călătorie fără credit (se scade o călătorie disponibilă)."""
        if self.calatorii_disponibile > 0:
            self.calatorii_disponibile -= 1
            print("Călătoria a fost validată cu succes! O călătorie a fost folosită.")
        else:
            print("Nu mai aveți călătorii disponibile pe card.")

    def reincarca_credit(self, suma):
        """Reîncarcă credit pe card."""
        if suma > 0:
            self.credit_disponibil += suma
            print(f"{suma} lei au fost adăugați pe card.")
        else:
            print("Suma trebuie să fie pozitivă.")

    def reincarca_calatorii(self, numar_calatorii):
        """Reîncarcă călătorii pe card."""
        if numar_calatorii > 0:
            self.calatorii_disponibile += numar_calatorii
            print(f"{numar_calatorii} călătorii au fost adăugate pe card.")
        else:
            print("Numărul de călătorii trebuie să fie pozitiv.")

    def verifica_sold(self):
        """Returnează un dicționar cu soldul cardului (călătorii și credit)."""
        return {
            "Călătorii disponibile": self.calatorii_disponibile,
            "Credit disponibil": self.credit_disponibil
        }

    def __str__(self):
        """Reprezentarea sub formă de text a obiectului STBCard."""
        return (f"Card STB {self.nume} - "
                f"{self.calatorii_disponibile} călătorii disponibile, "
                f"{self.credit_disponibil} lei credit disponibil.")

# Exemplu de utilizare
card1 = STBCard(nume="Ion Popescu", calatorii_disponibile=5, credit_disponibil=10.0)
print(card1)

# Reîncărcare credit
card1.reincarca_credit(20.0)
print(card1)

# Validare călătorie cu credit
card1.validare_calatorie_credit()
print(card1)

# Validare călătorie fără credit
card1.validare_calatorie()
print(card1)

# Reîncărcare călătorii
card1.reincarca_calatorii(10)
print(card1)

# Validare călătorie din nou
card1.validare_calatorie_credit()
print(card1)

# Card fără nume
card2 = STBCard(calatorii_disponibile=3, credit_disponibil=5.0)
print(card2)
card2.validare_calatorie_credit()
print(card2)
