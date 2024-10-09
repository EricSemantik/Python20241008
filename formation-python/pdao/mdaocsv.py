import csv
from pathlib import Path
from pdao.mdao import BaseDao
from pclient.mclient import Client
from pbanqque.mexception import BanqueDaoNotFoundException

class ClientDaoCsv(BaseDao):
    def __init__(self, chemin):
        super().__init__()
        self.__path = Path(chemin)

    def findAll(self):
        pass
    
    def findById(self, id):
        pass
    
    def create(self, obj):
        pass

    def update(self, obj):
        pass

    def deleteById(self, id):
       pass

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