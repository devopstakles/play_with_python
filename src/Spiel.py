Spieler = 0
Computer = 0

class Spielstand():

    def __init__(self):
        self.Spieler = 0
        self.Computer = 0

    def gewonnen(self):
        print("Du gewinnst")
        self.Spieler = self.Spieler + 1

    def verloren(self):
        print("Du verlierst")
        self.Computer = self.Computer + 1

    def __str__(self):
        return "Du: " + str(self.Spieler) + " Computer: " + str(self.Computer)

def main():
    spielstand = Spielstand()
    for i in [1, 3, 8, 9, 12, 17]:
        print(i)
        if (i%2 == 0):
            spielstand.gewonnen()
        else:
            spielstand.verloren()
        print(spielstand)

if __name__ == "__main__":
    main()
