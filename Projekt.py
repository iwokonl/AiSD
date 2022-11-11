class Matrix:
    # Pola klasy
    Dane: list[list[float]]
    wys: int
    szer: int

    # Inicjalizowanie tablicy 2D
    def __init__(self, m: int) -> None:
        Matrix.wys = 0
        Matrix.szer = 0
        self.matrix = []
        for y in range(m):
            self.matrix.append([float(0) for x in range(m)])
        Matrix.aktualizacja(self)

    # Mnożenie macierzy
    def __mul__(self, other) -> list[list[float]]:
        # Ustalanie nowych pomocniczych macierzy
        matrixx = []
        # Tworzenie nowej macierzy jako obiekt "Matrix"
        matrix = Matrix(len(self.matrix))
        # Mnożonko ale trickiem
        for y in range(len(self.matrix)):
            matrixx.append([float(0) for x in range(len(self.matrix))])
        for i in range(len(self.matrix)):
            # iterate through columns of Y
            for j in range(other.szerokosc_macierzy()):
                # iterate through rows of Y
                for k in range(other.wysokosc_macierzy()):
                    matrixx[i][j] += self.matrix[i][k] * other.pobierz(k, j)
        # Wrzucanie wartości do właściwej macierzy
        for x in range(len(matrixx)):
            for y in range(len(matrixx[0])):
                matrix.ustal(x, y, matrixx[x][y])
        Matrix.aktualizacja(self)
        return matrix

    # Sumowanie
    def __add__(self, other):
        # Tworzenie nowej macierzy jako obiekt "Matrix"
        matrix = Matrix(len(self.matrix))
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                matrix.ustal(x, y, self.matrix[x][y] + other.pobierz(x, y))
        Matrix.aktualizacja(self)
        return matrix

    # Odejmowanie
    def __sub__(self, other):
        matrix = Matrix(len(self.matrix))
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                matrix.ustal(x, y, self.matrix[x][y] - other.pobierz(x, y))
        Matrix.aktualizacja(self)
        return matrix

    # Tak jak nazwa metody mówi
    def wysokosc_macierzy(self) -> int:
        return len(self.matrix)

    # Tak jak nazwa metody mówi
    def szerokosc_macierzy(self) -> int:
        return len(self.matrix[0])

    def aktualizacja(self) -> None:
        Matrix.wys = len(self.matrix) -1
        Matrix.szer = len(self.matrix[0]) -1
        Matrix.Dane = self.matrix

    # Ustawia zadaną wartość na dany idex
    def ustal(self,index_poz:int,index_pion:int,wartosc:float) -> None:
        # # Zmienne, żeby łatwiej ogarnąć
        xx = index_poz
        yy = index_pion
        matrix = []
        maxv = max(index_pion,index_pion)
        print(maxv)
        dodanie_dlugosci_w_poziomie = maxv - len(self.matrix)
        dodanie_dlugosci_w_pionie = maxv - len(self.matrix)
        dodawanie_wartosci_poziom = [float(0) for x in range(len(self.matrix[0]))]
        dodawanie_wartosci_ost_wartosci_w_tablicy = float(0)
        if len(self.matrix[0]) < index_poz or len(self.matrix) < index_pion :
            # Bebechy
            for y in range(dodanie_dlugosci_w_pionie+1):
                self.matrix.append(dodawanie_wartosci_poziom)
            for y in range(dodanie_dlugosci_w_poziomie+1):
                for x in range(index_pion+1):
                    self.matrix[x].append(dodawanie_wartosci_ost_wartosci_w_tablicy)
            # Dodawanie zadanej wartości
            for y in range(len(self.matrix[0])):
                matrix.append([float(0) for x in range(len(self.matrix))])
            for y in range(len(self.matrix)):
                for x in range(len(self.matrix[0])):
                    matrix[y][x] = self.matrix[y][x]
            matrix[index_poz][index_pion] = float(wartosc)
            self.matrix = matrix

        else:
            # Dodawanie zadanej wartości
            self.matrix[index_poz][index_pion] = float(wartosc)

    # Pobiera daną wartość po indexie
    def pobierz(self, index_1: int, index_2: int) -> float:
        try:
            return float(self.matrix[index_1][index_2])
        except IndexError:
            return 0
        except:
            return f"Coś zjebałeś"

    # Transponuje daną macierz
    def transponuj(self):
        # Tworzenie nowej macierzy jako obiekt "Matrix"
        matrix = Matrix(len(self.matrix))
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                matrix.ustal(x, y, self.matrix[y][x])
        Matrix.aktualizacja(self)
        return matrix

    # Drukuje całą macierz
    def print(self) -> str:
        i = 0
        if self.matrix == []:
            print("Pusta []")
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                print(str(self.matrix[x][y]) + " ", end=" ")
            print()
        print("\n")

    # Uproszczanie macierzy
    def uprosc(self) -> None:
        a = 0
        # Na wypdaek jakby cała maceirz była zerami
        for x in range(len(self.matrix[0])):
            for y in range(len(self.matrix)):
                if self.matrix[x][y] == 0:
                    a = a + 1
        if a == len(self.matrix[0]) * len(self.matrix):
            self.matrix = []
            Matrix.aktualizacja(self)
            return 0
        i = 0
        pomoc = 0
        # Reverse dlatego żeby nie operowało na nie istniejącym idexie
        # A matrix [x] żeby wywalało cały wiersz
        for x in reversed(range(len(self.matrix))):
            for y in reversed(range(len(self.matrix[0]))):
                # Służy do sprawdzania czy są same 0 w wierszu
                if self.matrix[x][y] == 0:
                    i = i + 1
                # usuwa wiersz jezeli jest równy długości załego wiersza
                if i == len(self.matrix[0]):
                    del self.matrix[x]
            if i < len(self.matrix[0]):
                break
            i = 0
        # Zrobione jest to w taki sposób, aby nie wymyślać jak to zrobić na raz tylko transpozycja
        # 3 krotna i wykorzystanie tego co wcześniej
        matrix = []
        # transpozycja
        for y in range(len(self.matrix[0])):
            matrix.append([float(1) for x in range(len(self.matrix))])
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                matrix[x][y] = self.matrix[y][x]
        self.matrix = matrix
        i = 0
        for x in reversed(range(len(self.matrix))):
            for y in reversed(range(len(self.matrix[0]))):
                # Służy do sprawdzania czy są same 0 w wierszu
                if self.matrix[x][y] == 0:
                    i = i + 1
                # usuwa wiersz jezeli jest równy długości załego wiersza
                if i == len(self.matrix[0]):
                    del self.matrix[x]
            if i < len(self.matrix[0]):
                break
            i = 0
        matrix = []
        for y in range(len(self.matrix[0])):
            matrix.append([float(1) for x in range(len(self.matrix))])
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                matrix[x][y] = self.matrix[y][x]
        self.matrix = matrix
        Matrix.aktualizacja(self)
