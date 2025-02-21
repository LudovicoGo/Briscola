import random


class Mazzo():
    def __init__(self):
        self.semi = ["bastoni", "coppe", "denari", "spade"]
        self.valori = [1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10]
        self.carte = []

    def creaMazzo(self):
        for seme in self.semi:
            for valore in self.valori:
                self.carte.append([seme, valore])
        print("ho generato un mazzo di " + str(len(self.carte)) + " carte")

    def rigeneraMazzo(self):
        self.carte = []
        self.creaMazzo()

    def pescaMano(self):
        pesca = random.sample(self.carte, 3)
        print("Pescate 3 carte: " + str(pesca))
        return pesca

    def pescaUnaCarta(self):
        pesca = random.choice(self.carte)
        return pesca

