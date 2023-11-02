def rechner(zahl1: int, operator: str, zahl2: int):
    if operator == "+":
        return zahl1 + zahl2
    elif operator == "-":
        return zahl1 - zahl2
    elif operator == "*":
        return zahl1 * zahl2
    elif operator == "*":
        return zahl1 * zahl2
    else:
        return 'Ungültiger Operator'

rechnen = input('Was möchstest du rechnen? ')
benutzereingabe= rechnen.split()

ergebnis = rechner(int(benutzereingabe[0]), benutzereingabe[1], int(benutzereingabe[2]))



print(f'Dein Ergebnis ist {ergebnis}')