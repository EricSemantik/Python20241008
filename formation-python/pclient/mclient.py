from typing import NoReturn

class Client :

    def __init__(self, email: str, nom : str = "", prenom : str = ""):
        self.__email = email
        self.__nom = nom
        self.__prenom = prenom

    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def prenom(self) -> str:
        return self.__prenom

    @nom.setter
    def nom(self, nom: str) -> NoReturn:
        self.__nom = nom

    @prenom.setter
    def prenom(self, prenom: str) -> NoReturn:
        self.__prenom = prenom