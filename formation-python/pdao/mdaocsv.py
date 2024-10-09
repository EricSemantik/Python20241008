import csv
from pathlib import Path
from pdao.mdao import BaseDao
from pclient.mclient import Client
from pbanque.mexception import BanqueDaoNotFoundException

class ClientDaoCsv(BaseDao):
    def __init__(self, chemin):
        super().__init__()
        self.__path = Path(chemin)

    def findAll(self):
        return self.__readAll()
    
    def findById(self, id):
        clientsFiltrer = filter(lambda c: c.email == id, self.findAll())
        
        try:
            return next(clientsFiltrer)
        except StopIteration:
            raise BanqueDaoNotFoundException(f"Email {id} non trouvée")
    
    def create(self, obj):
        clients = self.findAll()
        clientsFiltrer = filter(lambda c: c.email == id, clients)
        
        try:
            return next(clientsFiltrer)
        except StopIteration:
            clients.append(obj)
            
            self.__writeAll(clients)

    def update(self, obj):
        try:
            clients = self.findAll()
            clientsFiltrer = filter(lambda c: c.email == obj.email, clients)
            client = next(clientsFiltrer)
            pos = clients.index(client)
            clients[pos] = obj
           
            self.__writeAll(clients)
        except ValueError:
            raise BanqueDaoNotFoundException(f"Email {id} non mise à jour")
        except StopIteration:
            raise BanqueDaoNotFoundException(f"Email {id} non mise à jour")
            
    def deleteById(self, id):
        try:
            clients = self.findAll()
            clientsFiltrer = filter(lambda c: c.email == id, clients)
            client = next(clientsFiltrer)
            clients.remove(client)
            
            self.__writeAll(clients)
        except ValueError:
            raise BanqueDaoNotFoundException(f"Email {id} non mise à jour")
        except StopIteration:
            raise BanqueDaoNotFoundException(f"Email {id} non mise à jour")

    def __readAll(self): # lire le fichier et renvoyer client[]
        liste = []

        if self.__path.exists() :
            with open(self.__path, "r") as f:
                reader = csv.DictReader(f, dialect=csv.unix_dialect)
                data = list(reader)
                for item in data :
                    liste.append(Client(item["EMAIL"], item["NOM"], item["PRENOM"]))

        return liste

    def __writeAll(self, liste): # ecrire le fichier à partir du tableau
        with open(self.__path, "w") as f:
            writer = csv.DictWriter(f, dialect=csv.unix_dialect, fieldnames=["EMAIL","NOM","PRENOM"])
            writer.writeheader()
            data = []
            for item in liste :
                data.append({"EMAIL":item.email, "NOM":item.nom, "PRENOM" : item.prenom})
                
            writer.writerows(data)