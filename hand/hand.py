import random
from itertools import count


class Hand:
    def __init__(self, nome):
        self.nome = nome
        self.mano = []
        self.presa = []
        self.punteggio = 0
        self.cartaGiocata = []

    def giocaCarta(self):
        self.cartaGiocata = random.choice(self.mano)
        self.mano.remove(self.cartaGiocata)

    def giocaCartaUtente2(self):
        print("Questa è la tua mano:")
        carte = []
        for i in range(0, len(self.mano)):
            carte.append(i + 1)
            print("Carta " + str(i + 1) + ": " + str(self.mano[i][0]) + " " + str(self.mano[i][1]))

        while True:
            try:
                carta = int(input(f"Quale carta vuoi giocare? Rispondi con: " + (", ".join(map(str, carte))))) - 1
                if carta not in carte:
                    raise ValueError("Errore: devi giocare una carta.")
                break
            except ValueError as e:
                print("Errore: puoi inserire uno tra 1, 2 o 3.")

        self.cartaGiocata = self.mano[carta]
        self.mano.remove(self.cartaGiocata)

    def giocaCartaUtente(self):
        print("Questa è la tua mano:")
        for i in range(len(self.mano)):
            print(f"Carta {i + 1}: {self.mano[i][0]} {self.mano[i][1]}")

        while True:
            try:
                carta = int(input(f"Quale carta vuoi giocare? Inserisci un numero tra 1 e {len(self.mano)}: ")) - 1
                if not (0 <= carta < len(self.mano)):
                    raise ValueError("Scelta non valida. L'indice deve corrispondere a una carta disponibile.")
                break
            except ValueError as e:
                # print(e)
                print(f"Errore: puoi inserire solo un numero tra 1 e {len(self.mano)}.")

        self.cartaGiocata = self.mano[carta]
        self.mano.remove(self.cartaGiocata)


    def giocaCartaRisposta(self, seme):
        carta = []
        for i in range(0, len(self.mano)):
            if self.mano[i][0] == seme:
                carta = self.mano[i]
                print("si carta con seme")
                break
        if len(carta) == 0:
            print("no carta con seme")
            carta = random.choice(self.mano)
        self.cartaGiocata = carta
        self.mano.remove(carta)

    def stampaMano(self):
        print("Mano " + self.nome)
        mano = ", ".join(f"{carta[0]} {carta[1]}" for carta in self.mano)
        print(mano)

    def vincePresa(self, carte):
        self.presa.extend(carte)

    def calcoloPunteggio(self):
        for carta in self.presa:
            if carta[1] == 1:
                self.punteggio += 11
            elif carta[1] == 3:
                self.punteggio += 10
            elif carta[1] == 10:
                self.punteggio += 4
            elif carta[1] == 9:
                self.punteggio += 3
            elif carta[1] == 8:
                self.punteggio += 2
        print("Punteggio " + self.nome + ": " + str(self.punteggio))

