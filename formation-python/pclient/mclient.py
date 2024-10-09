from typing import NoReturn

class Client :

    def __init__(self, id: int = None ,email: str, nom : str = "", prenom : str = ""):
        self.__id = id
        self.__email = email
        self.__nom = nom
        self.__prenom = prenom

    @property
    def id(self) -> str:
        return self.__id

    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def prenom(self) -> str:
        return self.__prenom

    @id.setter
    def id(self, id: int) -> NoReturn:
        self.__id = id

    @email.setter
    def email(self, email: str) -> NoReturn:
        self.__email = email

    @nom.setter
    def nom(self, nom: str) -> NoReturn:
        self.__nom = nom

    @prenom.setter
    def prenom(self, prenom: str) -> NoReturn:
        self.__prenom = prenom

    def __str__(self) -> str:
        return f"{self.id} {self.nom} {self.prenom} [{self.email}]"
    
    def __repr__(self) -> str:
        return self.__str__()