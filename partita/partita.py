import random

from hand.hand import Hand
from mazzo.mazzo import Mazzo

class Partita():
    def __init__(self, nome):
        self.cpu = Hand("CPU")
        self.utente = Hand(nome)
        self.mazzo = Mazzo()
        self.mazzo.creaMazzo()
        self.turno = random.choice(["cpu", "utente"])
        self.briscola = ["briscola", 0]
        self.seme = "nessunoSeme"

    def pescaCarta(self):
        carta = random.choice(self.mazzo.carte)
        while (carta == self.briscola) or (carta in self.utente.mano) or (carta in self.cpu.mano):
            carta = self.mazzo.pescaUnaCarta()
        else:
            self.mazzo.carte.remove(carta)
            return carta

    def manoIniziale(self):
        for i in range(0, 3):
            cartaUtente = self.pescaCarta()
            self.utente.mano.append(cartaUtente)
            cartaCPU = self.pescaCarta()
            self.cpu.mano.append(cartaCPU)
        self.briscola = self.pescaCarta()
        print("carte nel mazzo: " + str(len(self.mazzo.carte)))
        print("La briscola sarà: " + str(self.briscola[0]) + " " + str(self.briscola[1]))

    def giocaTurno(self):
        if self.turno == "cpu":
            self.cpu.giocaCarta()
            self.seme = self.cpu.cartaGiocata[0]
            print("carta giocata da cpu: " + str(self.cpu.cartaGiocata[0]) + " " + str(self.cpu.cartaGiocata[1])  )
            self.utente.giocaCartaUtente()
            print("carta giocata da utente: " + str(self.utente.cartaGiocata[0]) + " " + str(self.utente.cartaGiocata[1])  )
        elif self.turno == "utente":
            self.utente.giocaCartaUtente()
            self.seme = self.utente.cartaGiocata[0]
            print("carta giocata da utente: " + str(self.utente.cartaGiocata[0]) + " " + str(self.utente.cartaGiocata[1])  )
            self.cpu.giocaCarta()
            print("carta giocata da cpu: " + str(self.cpu.cartaGiocata[0]) + " " + str(self.cpu.cartaGiocata[1])  )

        self.effettuaPresa(self.utente.cartaGiocata, self.cpu.cartaGiocata)

    def effettuaPresa(self, cartaUtente, cartaCPU):
        # giocano stesso seme
        if cartaUtente[0] == cartaCPU[0]:
            if cartaUtente[1] == 1: #1 prende tutto
                self.turno = "utente"
            elif cartaCPU[1] == 1:
                self.turno = "cpu"
            elif cartaUtente[1] == 3: #se non c'è l'1 il 3 prende tutto
                self.turno = "utente"
            elif cartaCPU[1] == 3:
                self.turno = "cpu"
            elif cartaUtente[1] > cartaCPU[1]:
                self.turno = "utente"
            elif cartaUtente[1] < cartaCPU[1]:
                self.turno = "cpu"
        # uno solo dei due gioca briscola
        elif cartaUtente[0] == self.briscola[0] or cartaCPU[0] == self.briscola[0]:
            if cartaUtente[0] == self.briscola[0]:
                self.turno = "utente"
            elif cartaCPU[0] == self.briscola[0]:
                self.turno = "cpu"
        # diverso seme giocato
        # elif self.turno == "utente":
        #     print("prende utente")
        # elif self.turno == "cpu":
        #     print("prende cpu")

        presa = [cartaUtente, cartaCPU]
        if self.turno == "utente":
            print("prende utente")
            self.utente.vincePresa(presa)
        elif self.turno == "cpu":
            print("prende cpu")
            self.cpu.vincePresa(presa)


        self.pescaInizioTurno()

    def pescaInizioTurno(self):
        if len(self.mazzo.carte) > 1:
            if self.turno == "utente":
                pescaUtente = self.pescaCarta()
                # print("Utente ha pescato: " + str(pescaUtente[0]) + " " + str(pescaUtente[1]))
                self.utente.mano.append(pescaUtente)
                pescaCPU = self.pescaCarta()
                # print("CPU ha pescato: " + str(pescaCPU[0]) + " " + str(pescaCPU[1]))
                self.cpu.mano.append(pescaCPU)
            elif self.turno == "cpu":
                pescaCPU = self.pescaCarta()
                # print("CPU ha pescato: " + str(pescaCPU[0]) + " " + str(pescaCPU[1]))
                self.cpu.mano.append(pescaCPU)
                pescaUtente = self.pescaCarta()
                # print("Utente ha pescato: " + str(pescaUtente[0]) + " " + str(pescaUtente[1]))
                self.utente.mano.append(pescaUtente)
            print("Carte rimaste nel mazzo: " + str(len(self.mazzo.carte)))

        elif len(self.mazzo.carte) == 1:
            # Entrambi effettuano la loro ultima pescata
            if self.turno == "utente":
                pescaUtente = self.pescaCarta()
                self.utente.mano.append(pescaUtente)
                print("Utente ha pescato: " + str(pescaUtente[0]) + " " + str(pescaUtente[1]))
                self.cpu.mano.append(self.briscola)  # CPU prende la BRISCOLA
                print("CPU ha preso la briscola: " + str(self.briscola[0]) + " " + str(self.briscola[1]))
            elif self.turno == "cpu":
                pescaCPU = self.pescaCarta()
                self.cpu.mano.append(pescaCPU)
                print("CPU ha pescato: " + str(pescaCPU[0]) + " " + str(pescaCPU[1]))
                self.utente.mano.append(self.briscola)  # Utente prende la BRISCOLA
                print("Utente ha preso la briscola: " + str(self.briscola[0]) + " " + str(self.briscola[1]))

    def iniziaPartita(self):
        print("Inizierà: " + str(self.turno).upper())
        self.manoIniziale()
        self.utente.stampaMano()
        self.cpu.stampaMano()

        counter = 1
        while len(self.utente.mano) != 0:
            print("Turno " + str(counter) + ":")
            counter += 1
            self.giocaTurno()

        print("Sono finite le carte nel mazzo!")
        print("Numero carte in mano utente: " + str(len(self.utente.mano)))
        print("Numero carte in mano cpu: " + str(len(self.cpu.mano)))

        self.utente.calcoloPunteggio()
        self.cpu.calcoloPunteggio()
        if self.utente.punteggio > self.cpu.punteggio:
            print(f"Utente vince con {self.utente.punteggio} punti!")
        elif self.cpu.punteggio == self.utente.punteggio:
            print(f"PAREGGIO! Con {self.cpu.punteggio} punti a testa!")
        else:
            print(f"CPU vince con {self.cpu.punteggio} punti!")