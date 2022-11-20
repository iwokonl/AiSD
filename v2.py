class Mac_2d_k():
    dane: list[list[float]]
    wys: int
    szer: int

    # Inicjalizer klasy
    def __init__(self):
        self.dane = []
        Mac_2d_k.aktualizacja(self)

    def aktualizacja(self):
        if self.dane == []:
            Mac_2d_k.wys = 0
            Mac_2d_k.szer = 0
        else:
            Mac_2d_k.szer = len(self.dane)
            Mac_2d_k.wys = len(self.dane[0])
        Mac_2d_k.dane = self.dane

    def ustal(self, nr_wiersza: int, nr_kolumny: int, wartosc: float) -> None:
        dane = self.dane
        stara_szerokosc = Mac_2d_k.wys
        Mac_2d_k.aktualizacja(self)
        for x in range(nr_kolumny - Mac_2d_k.szer + 1):
            dane.append([float(0) for x in range(nr_wiersza + 1)])
        for x in range(Mac_2d_k.szer):
            for y in range(nr_wiersza-Mac_2d_k.wys+1):
                dane[x].append(float(0))
        for x in range(len(dane)):
            if len(dane[0]) != len(dane[x]):
                for y in range(Mac_2d_k.wys - stara_szerokosc):
                    dane[x].append(float(0))
        dane[nr_kolumny][nr_wiersza] = float(wartosc)
        self.dane = dane
        Mac_2d_k.aktualizacja(self)

    def pobierz(self, nr_wiersza: int,nr_kolumny: int) -> float:
        return float(self.dane[nr_kolumny][nr_wiersza])

    def print(self) -> str:
        Mac_2d_k.aktualizacja(self)
        if self.dane == []:
            print("Macierz jest pusta []")
            return
        for x in range(Mac_2d_k.wys):
            for y in range(Mac_2d_k.szer):
                print(str(self.dane[y][x]) + " ", end="")
            print()
        print("\n")

    def transponuj(self) -> 'Mac_2d_k':
        Mac_2d_k.aktualizacja(self)
        szer = Mac_2d_k.szer
        wys = Mac_2d_k.wys
        matrix = Mac_2d_k()
        matrix.ustal(szer-1,wys-1,0)
        for x in range(wys):
            for y in range(szer):
                matrix.ustal(y, x, self.dane[y][x])
        return matrix

a = Mac_2d_k()
a.ustal(0,1,1)
a.ustal(1,0,3)
a.ustal(1,1,4)
a.ustal(2,3,-0.5)
a.print()
c = a.transponuj()
c.print()
print(c.dane)