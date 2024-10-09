from pbanque.mexception import BanqueDaoNotFoundException
from pcompte.mcompte import CompteEpargne
from pdao.mdao import BaseDao


class ClientDaoMemory(BaseDao):
    
    def __init__(self):
        super().__init__()
        self.__clients = []

    def findAll(self): # renvoie le tableau de clients
        return self.__clients
    
    def findById(self, id): # recherche le client par son email
        clientsFiltrer = filter(lambda c: c.email == id,self.__clients)
        
        try:
            return next(clientsFiltrer)
        except StopIteration:
            raise BanqueDaoNotFoundException(f"Email {id} non trouvée")
    
    def create(self, obj): # rajoute le client (obj) dans le tableau si email n'existe pas déjà (-> Exception)
        try:
            self.findById(obj.email)
        except BanqueDaoNotFoundException:       
            self.__clients.append(obj)

    def update(self, obj): # met à jour le client (obj) dans le tableau
        try:
            client = self.findById(obj.email)
            pos = self.__clients.index(client)
            self.__clients[pos] = obj
        except ValueError:
            raise BanqueDaoNotFoundException(f"Email {id} non mise à jour")
    
    def deleteById(self, id): # supprime le client en recherchant par son email
        client = self.findById(id)
        self.__clients.remove(client)

    def findAllByNom(self, nom): # renvoie le tableau de clients filtrer par nom
        clientsByNom = filter(lambda c: c.nom == nom,self.__clients)
        
        return list(clientsByNom)

class CompteDaoMemory(BaseDao):
    
    def __init__(self):
        super().__init__()
        self.__comptes = []

    def findAll(self):
        return self.__comptes
    
    def findById(self, id): 
        comptesFiltrer = filter(lambda c: c.numero == id,self.__comptes)
        
        try:
            return next(comptesFiltrer)
        except StopIteration:
            raise BanqueDaoNotFoundException(f"Numéro {id} non trouvée")
    
    def create(self, obj): 
        try:
            self.findById(obj.numero)
        except BanqueDaoNotFoundException:       
            self.__comptes.append(obj)

    def update(self, obj): 
        try:
            compte = self.findById(obj.numero)
            pos = self.__comptes.index(compte)
            self.__comptes[pos] = obj
        except ValueError:
            raise BanqueDaoNotFoundException(f"Numéro {id} non mise à jour")
    
    def deleteById(self, id): 
        compte = self.findById(id)
        self.__comptes.remove(compte)

    def findAllCompteEpargne(self):      
        return list(filter(lambda c : type(c) == CompteEpargne  , self.__comptes))



