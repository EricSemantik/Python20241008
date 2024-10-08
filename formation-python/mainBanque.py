from pclient.mclient import Client
from pcompte.mcompte import Compte

if __name__ == "__main__":

    pauline = Client("pauline@hotmail.com")
    pauline.nom = "POUZOU"
    pauline.prenom = "Pauline"

    julien = Client("julien@gmail.com", "CHEMLA", "Julien")

    print(julien.email)
    print(julien.nom)

    compteM = Compte(54515, 200.0)
    compteM.titulaire = pauline

    print(f"numéro : {compteM.numero} - solde : {compteM.solde} - Nom : {compteM.titulaire.nom}")

    compteM.crediter(10000)

    print(f"numéro : {compteM.numero} - solde : {compteM.solde} - Nom : {compteM.titulaire.nom}")

    compteD = Compte(452, 20.0)
    compteD.titulaire = julien

    print(f"numéro : {compteD.numero} - solde : {compteD.solde} - Nom : {compteD.titulaire.nom}")

    compteD.debiter(100)

    print(f"numéro : {compteD.numero} - solde : {compteD.solde} - Nom : {compteD.titulaire.nom}")


