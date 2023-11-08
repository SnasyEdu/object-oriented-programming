import random

class Konto():
    def __init__(self, name) -> None:
        self.name = name
        self.kontostand = 0
        #IBAN
        self.country_code = 'DE'
        self.country_code_in_int = '1314'
        self.bankleitzahl = '52250000'
        self.kontonummer = str(random.randint(1000000000, 9999999999))
        self.prüfziffer = str(self.get_prüfziffer())
        self.iban = self.country_code + self.prüfziffer + self.bankleitzahl + self.kontonummer
        #Online-Zahlung
        self.cvv = random.randint(100, 999)
        self.ablaufdatum = '01/28'

    def get_prüfziffer(self) -> int:
        step1 = self.bankleitzahl + self.kontonummer + self.country_code_in_int + '00'
        step2 = int(step1) % 97
        step3 = 98 - int(step2)

        return step3

    def __str__(self) -> str:
        return f'Name: {self.name} | Kontostand: {self.kontostand}€ | IBAN: {self.iban} | CVV: {self.cvv} | Ablaufdatum: {self.ablaufdatum}'


    def einzahlen(self, anzahl: int) -> None:
        try:
            if anzahl > 0:
                self.kontostand += int(anzahl)
                print(f'Dein Kontostand wurde um {anzahl}€ erhöht')
            elif anzahl == 0:
                print('Du kannst nicht 0€ einzahlen')
            else:
                print('Du kannst keine negativen Beträge einzahlen')
        except:
            print('Benutze bitte einen Zahlenwert!')

    def abheben(self, anzahl: int) -> None:
        try:
            if anzahl > 0:
                ergebnis = self.kontostand - int(anzahl)

                if ergebnis >= 0:
                    self.kontostand -= int(anzahl)
                    print(f'Du hast {anzahl}€ abgehoben')
                    return 1 #Erfolgreich
                else:
                    print('Du hast zu wenig Geld auf dem Konto, um es abzuheben')
            elif anzahl == 0:
                print('Du kannst nicht 0€ abheben')
            else:
                print('Du kannst keine negativen Beträge abheben')
            
        except:
            print('Benutze bitte einen Zahlenwert!')

    
    def  umbuchen(self, zielkonto, anzahl: int) -> None:
        try:
            if self.abheben(anzahl) == 1:
                zielkonto.einzahlen(anzahl)
            else:
                print('Die Umbuchung war nicht erfolgreich')

        except:
            print('Benutze bitte einen Zahlenwert!')        

#Konten

konto1 = Konto('Hans Günther')
konto2 = Konto('Otto Müller')