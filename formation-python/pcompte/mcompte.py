from pclient.mclient import Client
from typing import NoReturn

class Compte :

    __nbr_comptes : int = 0

    def __init__(self, numero: int, solde: float):
        self.__numero : int = numero
        self.__solde : float = solde
        self.__titulaire : Client = None
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

    def debiter(self, montant: float):
        self.__solde -= montant