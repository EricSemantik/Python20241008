from datetime import date
from pclient.mclient import Client
from pcompte.mcompte import Compte, CompteEpargne
from pbanque.mexception import *

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

    try:
        compteD.debiter(100)
    except BanqueException as e:
        print(f"Erreur Compte : {e.message}")

    print(f"numéro : {compteD.numero} - solde : {compteD.solde} - Nom : {compteD.titulaire.nom}")

    print(f"nombre de comptes : {Compte.get_nbr_comptes()}")

    del compteM

    print(f"nombre de comptes : {Compte.get_nbr_comptes()}")

    jerome = Client("jerome@gmail.com", "SALOMON", "Jérome")

    compteP = CompteEpargne(452, 2000.0, date(2022, 1, 4), duree_blocage=4)
    compteP.titulaire = jerome

    try:
        print(compteP.debiter(3000))
    except BanqueSoldeException as ex:
        print(f"Solde insuffisant [{ex.message}]")
    except BanqueBlocageException as ex:
        print(f"Compte bloqué [{ex.message}]")

