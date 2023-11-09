import random
import logging

logging.basicConfig(level=logging.INFO, filename='account.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


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
                logging.info(f'{self.name} hat {anzahl}€ eingezahlt')
            elif anzahl == 0:
                logging.error(f'{self.name} hat versucht 0€ einzuzahlen')
            else:
                logging.error(f'{self.name} hat versucht eine negative Anzahl einzuzahlen')
        except:
            logging.debug('Benutze bitte einen Zahlenwert!')

    def abheben(self, anzahl: int) -> None:
        try:
            if anzahl > 0:
                ergebnis = self.kontostand - int(anzahl)

                if ergebnis >= 0:
                    self.kontostand -= int(anzahl)
                    logging.info(f'{self.name} hat {anzahl}€ abgehoben')
                else:
                    logging.error(f'{self.name} hat versucht {anzahl}€ abzuheben, obwohl er nur {self.kontostand}€ auf dem Konto hat')
            elif anzahl == 0:
                logging.error(f'{self.name} hat versucht 0€ abzuheben')
            else:
                logging.error(f'{self.name} hat versucht eine negative Anzahl abzuheben')
            
        except:
            logging.debug('Benutze bitte einen Zahlenwert!')

    
    def  umbuchen(self, zielkonto, anzahl: int) -> None:
        try:
            if self.abheben(anzahl) == 1:
                zielkonto.einzahlen(anzahl)
            else:
                logging.error(f'{self.name} hat versucht {anzahl}€ auf das Konto von {zielkonto.name} zu überweisen, obwohl er nur {self.kontostand}€ auf dem Konto hat')

        except:
            logging.debug('Benutze bitte einen Zahlenwert!')   

#Konten

konto1 = Konto('Hans Günther')
konto2 = Konto('Otto Müller')