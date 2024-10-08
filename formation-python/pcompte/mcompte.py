from datetime import date
from pclient.mclient import Client
from typing import NoReturn

class Compte :

    __nbr_comptes : int = 0

    def __init__(self, numero: int, solde: float, date_ouverture: date = date.today()):
        self.__numero : int = numero
        self.__solde : float = solde
        self.__titulaire : Client = None
        self.__date_ouverture = date_ouverture
        Compte.__nbr_comptes += 1

    def __del__(self) :
        Compte.__nbr_comptes -= 1

    @classmethod
    def get_nbr_comptes ( cls ) :
        return cls.__nbr_comptes

    @property
    def numero(self) -> int:
        return self.__numero
    
    @property
    def solde(self) -> float:
        return self.__solde

    @property
    def titulaire(self) -> Client:
        return self.__titulaire

    @titulaire.setter
    def titulaire(self, titulaire: Client) -> NoReturn:
        self.__titulaire = titulaire

    def crediter(self, montant: float ):
        self.__solde += montant

    def debiter(self, montant: float) -> bool :
        if montant > self.solde:
            return False

        self.__solde -= montant
        return True



class CompteEpargne (Compte):
    def __init__(self, numero: int, solde: float, date_ouverture: date = date.today(), taux_interet: float = 0.2, duree_blocage : int = 5):
        super().__init__(numero, solde, date_ouverture)
        self.__taux_interet = None
        self.__duree_blocage = None

    @property
    def taux_interet(self) -> float:
        return self.__taux_interet
    
    @property
    def duree_blocage(self) -> int:
        return self.__duree_blocage
    
    @taux_interet.setter
    def taux_interet(self, taux_interet: float) -> NoReturn:
        self.__taux_interet = taux_interet

    @duree_blocage.setter
    def duree_blocage(self, duree_blocage: int) -> NoReturn:
        self.__duree_blocage = duree_blocage

    def calcul_interet(self) -> NoReturn :
        self.crediter(self.solde * self.taux_interet)

    def debiter(self, montant: float) -> bool :
        date_courante : date = date.today()

        duree_ecoulee = date_courante.year - self.date_ouverture.year - \
        ((date_courante.month, date_courante.day) < (self.date_ouverture.month, self.date_ouverture.day))

        if duree_ecoulee < self.duree_blocage: 
            return False

        return super().debiter(montant)
