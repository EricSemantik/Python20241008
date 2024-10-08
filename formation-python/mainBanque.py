from pclient.mclient import Client

if __name__ == "__main__":

    pauline = Client("pauline@hotmail.com")
    pauline.nom = "POUZOU"
    pauline.prenom = "Pauline"

    julien = Client("julien@gmail.com", "CHEMLA", "Julien")

    print(julien.email)
    print(julien.nom)