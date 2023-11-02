import random

class Erde():
    def __init__(self) -> None:
        self.grass = False
        self.item = False

        self.koordinte_x = None
        self.koordinte_y = None
        self.koordinte_z = None


    def __str__(self) -> str:
        return f'Gras: {self.grass} | Item: {self.item} | Koordinaten: {self.koordinte_x}, {self.koordinte_y}, {self.koordinte_z}'


    def get_random_koordinate(self) -> int:
        return random.randint(-500, 500)


    def grass_wachsen(self) -> None:
        self.grass = True
    
    def grass_verschwinden(self) -> None:
        self.grass = False
    
    def abbauen(self) -> None:
        self.grass = False
        self.item = True

        self.koordinte_x = None
        self.koordinte_y = None
        self.koordinte_z = None
    
    def bauen(self, x, y, z) -> None:
        self.item = False
        self.koordinte_x = x
        self.koordinte_y = y
        self.koordinte_z = z


erde = Erde()
erde.bauen(erde.get_random_koordinate(), erde.get_random_koordinate(), erde.get_random_koordinate())