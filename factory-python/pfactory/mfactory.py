from datetime import date
from typing import List, NoReturn

class Adresse:
    def __init__(self, rue: str = "", complement: str = "", code_postal: str = "", ville: str = ""):
        self.__rue : str = rue
        self.__complement : str = complement
        self.__code_postal : str= code_postal
        self.__ville : str = ville

    @property
    def rue(self) -> str:
        return self.__rue

    @property
    def complement(self) -> str:
        return self.__complement

    @property
    def code_postal(self) -> str:
        return self.__code_postal

    @property
    def ville(self) -> str:
        return self.__ville

    @rue.setter
    def rue(self, rue: str) -> NoReturn:
        self.__rue = rue

    @complement.setter
    def complement(self, complement: str) -> NoReturn:
        self.__complement = complement

    @code_postal.setter
    def code_postal(self, code_postal: str) -> NoReturn:
        self.__code_postal = code_postal

    @ville.setter
    def ville(self, ville: str) -> NoReturn:
        self.__ville = ville

class Personne:
    def __init__(self, email: str, nom: str = "", prenom: str = "", date_naissance: date = None):
        self.__email: str = email
        self.__nom: str = nom
        self.__prenom: str = prenom
        self.__date_naissance : date = date_naissance
        self.__adr : Adresse = None

    @property
    def email(self) -> str:
        return self.__email

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def prenom(self) -> str:
        return self.__prenom

    @property
    def date_naissance(self) -> date:
        return self.__date_naissance

    @property
    def adr(self) -> Adresse:
        return self.__adr

    @nom.setter
    def nom(self, nom: str) -> NoReturn:
        self.__nom = nom

    @prenom.setter
    def nom(self, prenom: str) -> NoReturn:
        self.__prenom = prenom

    @date_naissance.setter
    def date_naissance(self, date_naissance: date) -> NoReturn:
        self.__date_naissance = date_naissance

    @adr.setter
    def adr(self, adr: str) -> NoReturn:
        self.__adr = adr
    
class Stagiaire(Personne):
    def __init__(self, email: str, nom: str = "", prenom: str = "", date_naissance: date = None, entreprise: str = ""):
        super().__init__(email, nom, prenom, date_naissance)
        self.__entreprise : str = entreprise

    @property
    def entreprise(self) -> str:
        return self.__entreprise

    @entreprise.setter
    def entreprise(self, entreprise: str) -> NoReturn:
        self.__entreprise = entreprise

class Formateur(Personne):
    def __init__(self, email: str, nom: str = "", prenom: str = "", date_naissance: date = None, experience: int = None, interne: bool = False):
        super().__init__(email, nom, prenom, date_naissance)
        self.__experience : str = experience
        self.__interne : bool = interne

    @property
    def experience(self) -> int:
        return self.experience

    @property
    def interne(self) -> bool:
        return self.interne

    @experience.setter
    def experience(self, experience: int) -> NoReturn:
        self.__experience = experience

    @interne.setter
    def interne(self, interne: bool) -> NoReturn:
        self.__interne = interne

class Formation:
    def __init__(self, code: str, titre: str = "", date_debut: date = None, duree: int = None):
        self.__code : str = code
        self.__titre : str = titre
        self.__date_debut : date = date_debut 
        self.__duree : int = duree
        self.__lieu: Adresse = None
        self.__formateur: Formateur = None
        self.__stagiaires: List[Stagiaire] = None

    @property
    def code(self) -> str:
        return self.__code

    @property
    def titre(self) -> str:
        return self.__titre

    @property
    def date_debut(self) -> date:
        return self.__date_debut

    @property
    def duree(self) -> int:
        return self.__duree

    @property
    def lieu(self) -> Adresse:
        return self.__lieu

    @property
    def formateur(self) -> Formateur:
        return self.__formateur

    @property
    def stagiaires(self) -> List[Stagiaire]:
        return self.__stagiaires

    @code.setter
    def code(self, code: str) -> NoReturn:
        self.__code = code

    @titre.setter
    def titre(self, titre: str) -> NoReturn:
        self.__titre = titre

    @date_debut.setter
    def date_debut(self, date_debut: date) -> NoReturn:
        self.__date_debut = date_debut

    @duree.setter
    def duree(self, duree: int) -> NoReturn:
        self.__duree = duree

    @lieu.setter
    def lieu(self, lieu: Adresse) -> NoReturn:
        self.__lieu = lieu

    @lieu.setter
    def lieu(self, lieu: Adresse) -> NoReturn:
        self.__lieu = lieu

    @formateur.setter
    def formateur(self, formateur: Formateur) -> NoReturn:
        self.__formateur = formateur

    @stagiaires.setter
    def formateur(self, stagiaires: List[Stagiaire]) -> NoReturn:
        self.__stagiaires = stagiaires
    