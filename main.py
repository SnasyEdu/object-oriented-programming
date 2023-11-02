import random

class Konto():
    def __init__(self, name) -> None:
        self.name = name
        self.bankleitzahl = '52250000'
        self.kontonummer = str(random.randint(1000000000, 9999999999))
        self.cvv = random.randint(100, 999)
        self.ablaufdatum = '01/28'
        self.kontostand = 0

        step1 = self.bankleitzahl + self.kontonummer + '1314' + '00'
        step2 = int(step1) % 97
        step3 = 98 - int(step2)

        self.iban = 'DE' + str(step3) + self.bankleitzahl + self.kontonummer
    
        #(1) = Bankleitzahl + Kontonummer + 1314 + 00
        #(2) = Von (1) % 97
        #(3) = 98 - (2)
        #(4) = DE + (3) + Bankleitzahl + Kontonummer

    def __str__(self) -> str:
        return f'Name: {self.name} | IBAN: {self.iban} | Kontonummer: {self.kontonummer} | CVV: {self.cvv} | Ablaufdatum: {self.ablaufdatum} | Kontostand: {self.kontostand}€'


    def einzahlen(self, anzahl: int):
        try:
            self.kontostand += int(anzahl)
            print(f'Dein Kontostand wurde um {anzahl}€ erhöht')
        except:
            print('Benutze bitte einen Zahlenwert!')

    def abheben(self, anzahl: int):
        try:
            ergebnis = self.kontostand - int(anzahl)

            if ergebnis >= 0:
                self.kontostand -= int(anzahl)
                print(f'Du hast {anzahl}€ abgehoben')
            else:
                print('Du hast zu wenig Geld auf dem Konto, um es abzuheben')
            
        except:
            print('Benutze bitte einen Zahlenwert!')
        


konto = Konto('Hans Günther')
print(konto)