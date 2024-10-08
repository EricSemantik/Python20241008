from pclient.mclient import Client
from typing import NoReturn

class Compte :

    def __init__(self, numero: int, solde: float):
        self.__numero : int = numero
        self.__solde : float = solde
        self.__titulaire : Client = None

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