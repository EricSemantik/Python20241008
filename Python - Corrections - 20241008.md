# Corrections

## Variables et opérateurs

### Correction 1

```python
# Les proprietes de la boite
x = int(input('Entrez la largeur entière '))
y = int(input('Entrez la longueur entière '))
h = int(input('Entrez la hauteur entière '))

# Calcul le volume
volume = x * y * h

# Affichage du resultat
print("Le volume est de", volume)
```

### Correction 2

```python
a = int(input("Entrez votre première valeur "))
b = int(input("Entrez votre deuxième valeur "))

# avec une variable temporaire
tmp = a 
a = b
b = tmp
print("a vaut",a, "et b", b)

# avec un calcul
a = a+b
b = a-b
a = a-b
print("a vaut",a, "et b", b)
```

### Correction 3

```python
# Le nombre de secondes est fourni au depart :
nsd = int(input("Entrer son nombre entier de secondes "))

# Nombre d'annees contenues dans la duree fournie :
na = nsd // (3600 * 24 * 365)
nsr = nsd % (3600 * 24 * 365)
# division <entiere>
# n. de sec. restantes
# Nombre de mois restants :
nmo = nsr // (3600 * 24 * 30)
nsr = nsr % (3600 * 24 * 30)
# division <entiere>
# n. de sec. restantes
# Nombre de jours restants :
nj = nsr // (3600 * 24)
nsr = nsr % (3600 * 24)
# division <entiere>
# n. de sec. restantes
# Nombre d'heures restantes :
nh = nsr // 3600
nsr = nsr % 3600
# division <entiere>
# n. de sec. restantes
# Nombre de minutes restantes :
nmi = nsr // 60
nsr = nsr % 60
# division <entiere>
# n. de sec. restantes
print ("Nombre de secondes a convertir :", nsd)
print ("Cette duree correspond a", na, "annees de 365 jours, plus", end=' ')
print (nmo, "mois de 30 jours,", end=' ')
print (nj, "jours,", end=' ')
print (nh, "heures,", end=' ')
print (nmi, "minutes et", end=' ')
print (nsr, "secondes.")
```

### Correction 4

```python
chaine = "Bienvenue en France. La france c'est génial, n'est-ce pas ?"
sub_string = "FRANCE"

# convert string to lowercase
temp_str = chaine.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("Comptage FRANCE:", count)
```

### Correction 5

```python
str1 = input("Veuillez rentrer une chaine de caractères quelconque: ")
print("Chaine de caractères originale:", str1)

sliceStr1 = str1[::-1]
print("Chaine de caractères inversée:", sliceStr1)

reversedStr1 = ''.join(reversed(str1))
print("Chaine de caractères inversée (reversed):", reversedStr1)
```

## Conditions et tests

### Correction 6

```python
montant = int(input("Entrez votre montant : "))

if montant > 100 :
	if montant > 500 :
		montant = montant - (montant * 0.08)
	else :
		montant = montant - (montant * 0.05)
print("Vous devez :", montant)

# ou ce type de test 

if montant > 500 :
    montant = montant - (montant * 0.08)
elif montant > 100 :
    montant = montant - (montant * 0.05)
    
# ou ce type de test par intervalle
    
if 100 < montant <= 500 :
    montant = montant - (montant * 0.05)
elif montant > 500 :
    montant = montant - (montant * 0.08)

print("Vous devez :", montant)
```

### Correction 7

```python
x = int(input("Enter un entier : "))
y = int(input("Enter un entier : "))
z = int(input("Enter un entier : "))

if x > y:
	tmp = x
	x = y
	y = tmp
if y > z :
	tmp = y
	y = z
	z = tmp
if x > y:
	tmp = x
	x = y
	y = tmp

print(x,y,z)
```

### Correction 8

```python
a = eval(input("entrer un nombre "))
b = eval(input("entrer un nombre "))

print("nulle" if a == 0 or b == 0 
      else "positif" if (a > 0 and b > 0) or (a < 0 and b < 0) 
      else "negatif")

# ou

if a == 0 or b == 0:
    print("nulle")
elif (a > 0 and b > 0) or (a < 0 and b < 0):
    print("positif")
else: 
    print("négatif")
```

### Correction 9

```python
# Années bissextiles
print("Veuillez entrer l'année à tester :", end=' ')
a = eval(input())

if a % 4 != 0:
	# a n'est pas divisible par 4 -> année non bissextile
	bs = 0
else:
	if a % 400 ==0:
		# a divisible par 400 -> année bissextile
		bs = 1
	elif a % 100 ==0:
		# a divisible par 100 -> année non bissextile
		bs = 0
	else:
		# autres cas ou a est divisible par 4 -> année bissextile
		bs = 1

if bs ==1:
	ch = "est"
else:
	ch = "n'est pas"
print("L'année", a, ch, "bissextile.")


########### Variante : ###########
a = eval(input('Veuillez entrer une année : '))
if (a%4==0) and ((a%100!=0) or (a%400==0)):
	print(a,"est une année bissextile")
else:
	print(a,"n'est pas une année bissextile")
    
########### Variante Bis: ########### 
if a%4==0 and a%100!=0 or a%400==0:
	print(a,"est une année bissextile")
else:
	print(a,"n'est pas une année bissextile")
```

## Les boucles

### Correction 10

```python
tabMul = eval(input('Veuillez choisir la table à calculer : '))

for i in range(1,21):
	t = i * tabMul
	if t % 3 == 0:
		print (t,"*")
	else:
		print (t)
```

### Correction 11

```python
a = int(input("entrer un entier ")) # 5
b = int(input("entrer un entier ")) # 3

res = 0
for i in range(b):
	res += a

print(res)
```

### Correction 12

```python
mot = ''
while mot != 'end':
	mot = input("Enter un mot")
	if mot != 'end':
		print(len(mot))
```

### Correction 13

```python
mot = input("entrer un mot ") # engage le jeu que je le gagne len(mot) // 2 == 4

items = mot.split(" ")

mot = "".join(items)

palindrome = True

for i in range(len(mot) // 2):
	if mot[i] != mot[-1-i]:
		palindrome = False
		break

if palindrome:
	print("palindrome")
else:
	print("nop")
    
# ou

motInverse = mot[::-1]

if mot == motInverse:
    print("palindrome")
else:
	print("nop")
```

## Les tableaux

### Correction 14

```python
mots=["ordinateur","cafe","chocolat","digestion","cafe","faim","formation","television"]
occurence = 0
for mot in mots :
	if mot == "cafe":
		occurence += 1
print(occurence)
# ou
print(mots.count("cafe"))
```

### Correction 15

```python
items = [32, 5, 12, 8, 3, 75, 2, 15]
somme = 0

for item in items:
	somme += item

moyenne = somme / len(items)
print("Le moyenne est de", moyenne)
```

### Correction 16

```python
mots=["ordinateur","cafe","chocolat","digestion","faim","formation","television"]
motsInverse = mots[::-1]
print(motsInverse)
```

## Les sous-programmes

### Correction 17

```python
def surfaceCercle(rayon):
	return 3.14 * rayon**2
	
# surfaceCercleLambda = lambda rayon : 3.14 * rayon**2

rayon = 4
print("La surface du cercle de rayon",rayon," est de ",surfaceCercle(rayon))
```

### Correction 18

```python
def volBoite(x1 =-1, x2 =-1, x3 =-1):
	if x3 == -1 or x2 == -1:
		return x1**3
	# aucun argument n'a été fourni
	# un seul argument -> boîte cubique
	elif x3 == -1 :
		return x1*x1*x2
	# deux arguments -> boîte prismatique
	else :
		return x1*x2*x3

# volBoiteLambda = lambda x1 =-1, x2 =-1, x3 =-1 : (x1 * x2 * x3) if (x3 != -1 and x2 != -1) 	else (x1**2*x2 if x3 == -1 and x2 !=-1 else x1**3)

if __name__ == "__main__":
    # test :
    print(volBoite())
    print(volBoite(5.2))
    print(volBoite(5.2, 3))
    print(volBoite(5.2, 3, 7.4))

    print(volBoiteLambda())
    print(volBoiteLambda(5.2))
    print(volBoiteLambda(5.2, 3))
    print(volBoiteLambda(5.2, 3, 7.4))
```

### Correction 19

```python
def eleMax(liste,debut,fin):
	if debut < len(liste) and fin<=len(liste) and debut < fin:
		return max(liste[debut:fin])
    	#ou
        max = 0
        for i in range(debut, fin+1, 1):
            if liste[i] > max:
                max = liste[i]
        return max
	else:
		raise ValueError("Pas dans la liste")

if __name__ == "__main__":
	liste = [24,74,54,11,0,4]

	print("Le max de ",liste,"est",eleMax(liste,0,3))
```

### Correction 20

```python
def nomMois(i):
	mois = ['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Nomvembre','Decembre']
	return mois[i-1]

if __name__ == "__main__":
	nomMois(6)
```

### Correction 21 

```python
def compteMots(ph):
	nb = 0
	if len(ph) > 0:
		nb +=1
	for i in range(len(ph)):
		if ph[i] == ' ' and i+1 < len(ph) and ph[i+1] != ' ':
			nb +=1
	return nb
	#ou
    mots = ph.split(" ")
    return len(mots)
	#ou
    count = 0
	if len(ph) > 0:
		count += 1
        count += ph.count(" ")
        
if __name__ == "__main__":
	print(compteMots("cette phrase compte pour six mots"))
```

### Correction 22 (en plus)

```python
def saisieJoueur(grille):
	# les valeurs par défaut de x et y ne doivent pas être bonne
	# pour pouvoir rentrer dans le voile
	x = -1
	y = -1
	triche = True
	while triche:
		print("Entrer un entier entre 0 et 2 pour x")
		x = int(input())
		print("Entrer un entier entre 0 et 2 pour y")
		y = int(input())
		if ((x > 2 or x < 0) or (y > 2 or y < 0)):
			triche = True
		# par convention, une case vide est un espace
		elif grille[x][y] != " ":
			triche = True
		else:
			triche = False
	return x,y

def initGrille():
	return [[" "," "," "],[" "," "," "],[" "," "," "]]

def afficheGrille(grille):
	for i in range(3):
		str1 = "|"
		for j in range(3):
			str1 += grille[i][j] + "|"
		print(str1)

def grillePleine(grille):
	for i in range(3):
		if grille[i].count(" ") > 0:
				return False
	return True

def winner(grille, player):
	# ligne
	for i in range(3):
		if grille[i][0] == grille[i][1] and grille[i][0] == grille[i][2] and grille[i][0] != " ":
			print(player, " a gagne")
			return True
	# colonne
	for i in range(3):
		if grille[0][i] == grille[1][i] and grille[0][i] == grille[2][i] and grille[0][i] != " ":
			print(player, " a gagne")
			return True
	# diagonale
	if grille[0][0] == grille[1][1] and grille[0][0] == grille[2][2] and grille[0][0] != " ":
		print(player, " a gagne")
		return True
	if grille[0][2] == grille[1][1] and grille[0][2] == grille[2][0] and grille[0][2] != " ":
		print(player, " a gagne")
		return True
	return False


if __name__ == "__main__":
    grille = initGrille()
    joueur = "O"
    afficheGrille(grille)
    while not grillePleine(grille) and not winner(grille, joueur) :
        # on change de joueur
        if joueur == "X":
            joueur = "O"
        else:
            joueur = "X"
        x,y = saisieJoueur(grille)
        grille[x][y] = joueur
        afficheGrille(grille)
```

### Correction 23 (en plus)

```python
def tri_bulle(tab):
    for i in range(len(tab)):
        permut = False
        for j in range(0, len(tab)-i-1):
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
                permut = True
        if not(permut):
            break

if __name__ == "__main__":
	tab = [98, 22, 15, 32, 2, 74, 63, 70]

	tri_bulle(tab)
 
	print(tab)
```

## Les fichiers 

### Correction 24

```python
def showChilds(path: Path, level: int = 0):
    for child in path.iterdir():
        line = ""
        for i in range(level):
            line += "    " 
        line += child.name
        if child.is_file():
            line += "*"
            
        print(line ) 
        
        if child.is_dir():
            showChilds(child, level + 1)

if __name__ == "__main__":
    racine = Path()
    showChilds(racine)
```

### Correction 25

```python
fichier = open("table.txt",'w')

for i in range(2,21):
	for j in (1,11):
		fichier.write(""+str(i)+" * "+str(j)+" = "+str(i*j)+"\n")

fichier.close()
```

### Correction 26

```python
name =  input("Entrer le nom de votre fichier ")
f = open(name,'r', encoding="UTF-8")

texte = f.read()

f.close()

fwrite = open('copie.txt','w')
fwrite.write(texte)
fwrite.close()
```

### Correction 27

```python
f = open('testExemple.txt','r', encoding="UTF-8")

lines = f.readlines()

f.close()

print(max(lines, key=len))
```

### Correction 28

```python
with open('personnes.csv','r', encoding="UTF-8") as f:
        first = True
        for line in f:
            if first:
                first = False
                continue
            items = line.strip().split(";")
            print(f"ID={items[0]} - NOM={items[1]} - PRENOM={items[2]} - MANAGER={items[3]=='Y'}")
```

## Les classes

### Correction 29

#### mclient dans pclient

```python
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

    def __str__(self) -> str:
        return f"{self.nom} {self.prenom} [{self.email}]"
```

#### mainBanque

```python
from pclient.mclient import Client

if __name__ == "__main__":
    marine = Client("marine@hotmail.com")
    marine.nom = "GINOUX"
    marine.prenom = "Marine"

    dorian = Client("dorian@gmail.com", "TERBAH", "Dorian")

    print(marine)
    print(dorian)
```

### Correction 30

#### mcompte dans pcompte

```python
from typing import NoReturn
from pclient.mclient import Client


class Compte:
    
    def __init__(self, numero: int, solde: float):
        self.__numero : int = numero
        self.__solde : float= solde
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

    def crediter(self, montant: float) -> NoReturn :
        self.solde += montant

    def debiter(self, montant: float) -> NoReturn :
        self.solde -= montant

    def __str__(self) -> str: 
        return f"{self.numero} {self.solde} - {self.titulaire}"
```

#### mainBanque

```python
from pclient.mclient import Client
from pcompte.mcompte import Compte

if __name__ == "__main__":
    marine = Client("marine@hotmail.com")
    marine.nom = "GINOUX"
    marine.prenom = "Marine"

    dorian = Client("dorian@gmail.com", "TERBAH", "Dorian")

    
    compteM = Compte(54515, 200.0)
    compteM.titulaire = marine

    print(compteM)

    compteD = Compte(452, 20.0)
    compteD.titulaire = dorian

    print(compteD)
```

### Correction 31

#### mcompte dans pcompte

```python
from typing import NoReturn
from pclient.mclient import Client

class Compte:
    __nbr_comptes : int = 0

    @classmethod
    def get_nbr_comptes(cls) -> int :
        return Compte.__nbr_comptes

    def __init__(self, numero: int, solde: float):
        self.__numero : int = numero
        self.__solde : float= solde
        self.__titulaire : Client = None
        Compte.__nbr_comptes += 1

    def __del__(self):
        Compte.__nbr_comptes -= 1

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

    def crediter(self, montant: float) -> NoReturn :
        self.solde += montant

    def debiter(self, montant: float) -> NoReturn :
        self.solde -= montant

    def __str__(self) -> str: 
        return f"{self.numero} {self.solde} - {self.titulaire}"
```

#### mainBanque

```python
from pclient.mclient import Client
from pcompte.mcompte import Compte

if __name__ == "__main__":
    marine = Client("marine@hotmail.com")
    marine.nom = "GINOUX"
    marine.prenom = "Marine"

    dorian = Client("dorian@gmail.com", "TERBAH", "Dorian")
    
    compteM = Compte(54515, 200.0)
    compteM.titulaire = marine

    print(compteM)

    compteD = Compte(452, 20.0)
    compteD.titulaire = dorian

    print(compteD)

    print(f"Nombre de comptes {Compte.get_nbr_comptes()}")

    del compteM

    print(f"Nombre de comptes {Compte.get_nbr_comptes()}")
```

## L'héritage

### Correction 32

#### mcompte dans pcompte

```python
from datetime import date
from typing import NoReturn
from pclient.mclient import Client

class Compte:
    __nbr_comptes : int = 0

    @classmethod
    def get_nbr_comptes(cls) -> int :
        return Compte.__nbr_comptes

    def __init__(self, numero: int, solde: float, date_ouverture: date = None):
        self.__numero : int = numero
        self.__solde : float= solde

        if date_ouverture == None :
            self.__date_ouverture = date.today()
        else :
            self.__date_ouverture = date_ouverture

        self.__titulaire : Client = None
        Compte.__nbr_comptes += 1

    def __del__(self):
        Compte.__nbr_comptes -= 1

    @property
    def numero(self) -> int:
        return self.__numero
    
    @property
    def solde(self) -> float:
        return self.__solde
    
    @property
    def date_ouverture(self) -> date:
        return self.__date_ouverture
    
    @property
    def titulaire(self) -> Client:
        return self.__titulaire
    
    @titulaire.setter
    def titulaire(self, titulaire: Client) -> NoReturn:
        self.__titulaire = titulaire

    def crediter(self, montant: float) -> NoReturn :
        self.__solde += montant

    def debiter(self, montant: float) -> bool :
        if montant <= self.solde :
            self.__solde -= montant
            return True
        
        return False
    
    def __str__(self) -> str: 
        return f"{self.numero} {self.solde}  {self.date_ouverture} - {self.titulaire}"
    
class CompteEpargne(Compte) :
    def __init__(self, numero: int, solde: float, date_ouverture: date = None, taux_interet : float = 0.2, duree_blocage: int = 5):
        super().__init__(numero, solde, date_ouverture)
        self.__taux_interet = taux_interet
        self.__duree_blocage = duree_blocage

    @property
    def taux_interet(self) -> float:
        return self.__taux_interet
    
    @property
    def duree_blocage(self) -> int:
        return self.__duree_blocage
    
    @taux_interet.setter
    def taux_interet(self, taux_interet: float) -> NoReturn:
        self.__taux_interet = taux_interet

    @duree_blocage.setter
    def duree_blocage(self, duree_blocage: int) -> NoReturn:
        self.__duree_blocage = duree_blocage

    def calcul_interet(self) -> NoReturn :
        self.crediter(self.solde * self.taux_interet)

    def debiter(self, montant: float) -> bool :
        date_courante : date = date.today()

        duree_ecoulee = date_courante.year - self.date_ouverture.year - \
        ((date_courante.month, date_courante.day) < (self.date_ouverture.month, self.date_ouverture.day))

        print(f"duree_ecoulee {duree_ecoulee}")

        if duree_ecoulee >= self.duree_blocage:
            return super().debiter(montant)
        else : 
            return False
        
    def __str__(self) -> str :
        return f"{super().__str__()} - {self.taux_interet} {self.duree_blocage}"
```

#### mainBanque

```python
from datetime import date
from pclient.mclient import Client
from pcompte.mcompte import Compte, CompteEpargne

if __name__ == "__main__":
    marine = Client("marine@hotmail.com")
    marine.nom = "GINOUX"
    marine.prenom = "Marine"

    dorian = Client("dorian@gmail.com", "TERBAH", "Dorian")
    
    compteM = Compte(54515, 200.0)
    compteM.titulaire = marine

    print(compteM)

    compteD = Compte(452, 20.0)
    compteD.titulaire = dorian

    print(compteD)

    print(f"Nombre de comptes {Compte.get_nbr_comptes()}")

    del compteM
    
    print(f"Nombre de comptes {Compte.get_nbr_comptes()}")

    pierre = Client("pierre@gmail.com", "FREBAULT", "Pierre")

    compteP = CompteEpargne(452, 2000.0, date(2020, 1, 1), duree_blocage=4)
    compteP.titulaire = pierre

    print(compteP.debiter(3000))
```

## Gestion des exceptions

### Correction 33

#### mexception dans pbanque

```python
class BanqueException(Exception) :
    def __init__(self, message: str = ""):
        super().__init__()
        self.__message = message

    @property
    def message(self) -> str :
        return self.__message
    
class BanqueSoldeException(BanqueException):
    def __init__(self, message: str = ""):
        super().__init__(message)

class BanqueBlocageException(BanqueException):
    def __init__(self, message: str = ""):
        super().__init__(message)
```

#### mcompte dans pcompte

```python
class Compte:
    # ...

    def debiter(self, montant: float)  :
        if montant > self.solde:
            raise BanqueSoldeException(f"Montant : {montant} - Solde : {self.solde}")

        self.__solde -= montant
        
class CompteEpargne(Compte):
    # ...

    def debiter(self, montant: float) :
        date_courante : date = date.today()

        duree_ecoulee = date_courante.year - self.date_ouverture.year - \
        ((date_courante.month, date_courante.day) < (self.date_ouverture.month, self.date_ouverture.day))

        if duree_ecoulee < self.duree_blocage: 
            raise BanqueBlocageException(f"Durée écoulée : {duree_ecoulee} - Durée de blocage : {self.duree_blocage}")

        super().debiter(montant)
```

#### mainbanque

```python
try:
    print(compteP.debiter(3000))
except BanqueSoldeException as ex:
    print(f"Solde insuffisant [{ex.message}]")
except BanqueBlocageException as ex:
    print(f"Compte bloqué [{ex.message}]")
except BanqueException as ex:
    print(f"Erreur applicative [{ex.message}]")
except :
    print("Autre Erreur")
```

## Les collections

### Correction 34

#### mdaomemory dans pdao

```python
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
```

#### mainbanque

```python
...
clientDao =  ClientDaoMemory()

clientDao.create(marine)
clientDao.create(dorian)
clientDao.create(pierre)

print(clientDao.findAll())

pierreFind = clientDao.findById(pierre.email)

pierreFind.nom = "FREBOLT"

clientDao.update(pierreFind)

print(clientDao.findAll())

clientDao.deleteById(pierre.email)

print(clientDao.findAll())
```

### Correction 35 (en plus)

```python
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
```

## La persistence 

### Correction 36

Dans mdaocsv, la classe ClientDaoCsv

```python
class ClientDaoCsv(BaseDao):
    def __init__(self, chemin):
        super().__init__()
        self.__path = Path(chemin)

    def findAll(self):
        return self.__readAll()
    
    def findById(self, id):
        clientsFiltrer = filter(lambda c: c.email == id,self.findAll())
        
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
```

### Correction 37

```python
if __name__ == "__main__":
    with sqlite3.connect("banque.db") as conn:
        cursor = conn.cursor() 
        cursor.execute("""CREATE TABLE IF NOT EXISTS client(
                            email TEXT PRIMARY KEY,
                            nom TEXT,
                            prenom TEXT)
                     """)
    
    with sqlite3.connect("banque.db") as conn:
        cursor = conn.cursor() 
        cursor.execute("INSERT INTO client (email, nom, prenom) VALUES (?,?,?)", ("eric@gmail.com", "SULTAN", "Eric"))

        cursorBis = conn.cursor() 
        cursorBis.execute("UPDATE client SET nom = ?, prenom = ? WHERE email = ?", ("SULTANA", "Erica", "eric@gmail.com"))
        conn.commit()

    with sqlite3.connect("banque.db") as conn:
        cursor = conn.cursor() 
        cursor.execute("SELECT email, nom, prenom FROM client") 
        for row in cursor.fetchall():
            print(row)
```

### Correction 38

Script DDL associé à l'exercice :

```sql
CREATE TABLE IF NOT EXISTS client(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            email TEXT UNIQUE NOT NULL,
                            nom TEXT,
                            prenom TEXT);
                            
CREATE TABLE IF NOT EXISTS compte(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            numero INTEGER UNIQUE NOT NULL,
                            type TEXT NOT NULL,
                            solde FLOAT,
                            date_ouverture DATE,
                            taux_interet FLOAT,
                            duree_blocage INTEGER,
                            titulaire_id INTEGER,
                            FOREIGN KEY(titulaire_id) REFERENCES client (id));
```

les Dao SQL avec une partie de la gestion de la relation Compte -> titulaire

```python
import csv
from pathlib import Path
import sqlite3
from pcompte.mcompte import Compte, CompteEpargne
from pdao.mdao import BaseDao
from pclient.mclient import Client
from pbanqque.mexception import BanqueDaoNotFoundException

class ClientDaoSql(BaseDao):
    def __init__(self, bdd):
        super().__init__()
        self.__bdd = Path(bdd)

    def findAll(self):
        liste = []
        with sqlite3.connect(self.__bdd) as conn:
            cursor = conn.cursor() 
            cursor.execute("SELECT id, email, nom, prenom FROM client") 
            
            for (id, email, nom, prenom) in cursor.fetchall():
                liste.append(Client(id, email, nom, prenom))

        return liste
    
    def findById(self, id):
        with sqlite3.connect(self.__bdd) as conn:
            cursor = conn.cursor() 
            cursor.execute("SELECT id, email, nom, prenom FROM client WHERE id = ?", (id,)) 
            (id, email, nom, prenom) = cursor.fetchone()
            return Client(id, email, nom, prenom)
    
    def create(self, obj):
        with sqlite3.connect(self.__bdd) as conn:
            cursor = conn.cursor() 
            cursor.execute("INSERT INTO client (email, nom, prenom) VALUES (?,?,?)", (obj.email, obj.nom, obj.prenom)) 
            conn.commit()

    def update(self, obj):
        with sqlite3.connect(self.__bdd) as conn:
            cursor = conn.cursor() 
            cursor.execute("UPDATE client SET email = ?, nom = ?, prenom = ? WHERE id = ?", (obj.email, obj.nom, obj.prenom, obj.id)) 
            conn.commit()

    def deleteById(self, id):
        with sqlite3.connect(self.__bdd) as conn:
            cursor = conn.cursor() 
            cursor.execute("DELETE FROM client WHERE id = ?", (id,)) 
            conn.commit()

class CompteDaoSql(BaseDao):
    def __init__(self, bdd):
        super().__init__()
        self.__bdd = Path(bdd)

    def findAll(self):
        liste = []
        with sqlite3.connect(self.__bdd) as conn:
            cursor = conn.cursor() 
            cursor.execute("SELECT id, type, numero, solde, date_ouverture, taux_interet, duree_blocage, titulaire_id FROM compte") 
            
            for (id, type, numero, solde, date_ouverture, taux_interet, duree_blocage, titulaire_id) in cursor.fetchall():
                titulaire = None
                if titulaire_id != None :
                    cursor.execute("SELECT id, email, nom, prenom FROM client WHERE id = ?", (id,)) 
                    (id, email, nom, prenom) = cursor.fetchone()
                    titulaire =  Client(id, email, nom, prenom)

                compte = None 
                if type == "CE":
                    compte = CompteEpargne(id, numero, solde, date_ouverture, taux_interet, duree_blocage)
                else :
                    compte = Compte(id, numero, solde, date_ouverture)

                if compte != None:
                    compte.titulaire = titulaire
                    liste.append(compte)

        return liste
    
    def findById(self, id):
        with sqlite3.connect(self.__bdd) as conn:
            cursor = conn.cursor() 
            cursor.execute("SELECT id, type, numero, solde, date_ouverture, taux_interet, duree_blocage FROM compte WHERE id = ?", (id,)) 
            (id, type, numero, solde, date_ouverture, taux_interet, duree_blocage) = cursor.fetchone()

            if type == "CE":
                return CompteEpargne(id, numero, solde, date_ouverture, taux_interet, duree_blocage)
            else :
                return Compte(id, numero, solde, date_ouverture)
        
    def create(self, obj):
        with sqlite3.connect(self.__bdd) as conn:
            cursor = conn.cursor() 

            titulaireId = None

            if obj.titulaire != None and obj.titulaire.id != None :
                titulaireId = obj.titulaire.id

            if isinstance(obj, CompteEpargne) :
                cursor.execute("INSERT INTO compte (type, numero, solde, date_ouverture, taux_interet, duree_blocage, titulaire_id) VALUES (?,?,?,?,?,?,?)", ("CE", obj.numero, obj.solde, obj.date_ouverture, obj.taux_interet, obj.duree_blocage, titulaireId)) 
            else :
                cursor.execute("INSERT INTO compte (type, numero, solde, date_ouverture, titulaire_id) VALUES (?,?,?,?,?)", ("C", obj.numero, obj.solde, obj.date_ouverture, titulaireId)) 
            conn.commit()

    def update(self, obj):
        with sqlite3.connect(self.__bdd) as conn:
            cursor = conn.cursor() 
            if isinstance(obj, CompteEpargne) :
                cursor.execute("UPDATE compte SET numero = ?, solde = ?, date_ouverture = ?, taux_interet = ?, duree_blocage = ? WHERE id = ?", (obj.numero, obj.solde, obj.date_ouverture, obj.taux_interet, obj.duree_blocage, obj.id)) 
            else :
                cursor.execute("UPDATE compte SET numero = ?, solde = ?, date_ouverture = ? WHERE id = ?", (obj.numero, obj.solde, obj.date_ouverture, obj.id)) 
            conn.commit()

    def deleteById(self, id):
        with sqlite3.connect(self.__bdd) as conn:
            cursor = conn.cursor() 
            cursor.execute("DELETE FROM compte WHERE id = ?", (id,)) 
            conn.commit()

```

## Les Tests

### Correction 39

```python
from unittest import TestCase
import unittest

from pclient.mclient import Client
from pdao.mdaosql import ClientDaoSql


class MonTest(TestCase):

    def test_update_client(self):
        clientDao = ClientDaoSql("banque.db")

        # ARRANGE
        client = Client(email="eric@gmail.com", nom="SULTAN", prenom="Eric")
        client = clientDao.create(client)

        # ACT
        client.email = "eric@hotmail.com"
        client.nom = "SULTANA"
        client.prenom = "Erica"

        clientDao.update(client)

        # ASSERT
        clientFind = clientDao.findById(client.id)

        self.assertEqual("eric@hotmail.com",clientFind.email)
        self.assertEqual("SULTANA",clientFind.nom)
        self.assertEqual("Erica",clientFind.prenom)



    

if __name__ == "__main__":
    unittest.main()
```

## SQLAlchemy

### Exercice 40

```python
from datetime import date
from typing import List, Optional
from sqlalchemy import Date, Float, ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship, sessionmaker


class Base(DeclarativeBase):
    pass

class Client(Base) :
    __tablename__="customer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    nom: Mapped[Optional[str]] = mapped_column(String(100), name="last_name")
    prenom: Mapped[Optional[str]] = mapped_column(String(100), name="first_name")

    comptes: Mapped[List["Compte"]] = relationship(back_populates="client")

   
    def __repr__(self) -> str:
        return f"Client(id={self.id}, email={self.email}, nom={self.nom}, prenom={self.prenom})"
    
class Compte(Base):
    __tablename__="account"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    numero: Mapped[int] = mapped_column(Integer, name="reference", unique = True)
    solde: Mapped[float] = mapped_column(Float, name="amount")
    date_ouverture: Mapped[date] = mapped_column(Date, name="start_date")
    client_id : Mapped[int] = mapped_column(Integer, ForeignKey("customer.id"), name="owner_id")

    client: Mapped[Client] = relationship(back_populates="comptes")

   
    def __repr__(self) -> str:
        return f"Compte(id={self.id}, numero={self.numero}, solde={self.solde}, date_ouverture={self.date_ouverture})"

if __name__ == "__main__" :
    engine = create_engine('sqlite:///banque.db', echo=True)

    Base.metadata.create_all(engine)    # Only for the first time
```

### Exercice 41

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from pmodel.mclient import Client

class ClientDaoSA:

    def __init__(self, engine):
        self.__engine = engine

    def findAll(self):
        with Session(self.__engine) as session:
            stmt = select(Client)

            return session.scalars(stmt).all()
        
    def findById(self, id):
        with Session(self.__engine) as session:
            return session.get(Client, id)
        
    def create(self, obj):
        with Session(self.__engine) as session:
            session.add(obj)
            session.commit()
            session.refresh(obj)

        return obj

    def update(self, obj):
        with Session(self.__engine) as session:
            obj = session.merge(obj)
            session.commit()

        return obj
    
    def deleteById(self, id):
        with Session(self.__engine) as session:
            obj = session.get(Client, id)
            session.delete(obj)
            session.commit()
```

```python
from sqlalchemy import create_engine

from pdao.mdaosa import ClientDaoSA
from pmodel.mclient import Client, Compte


if __name__ == "__main__" :
    engine = create_engine('sqlite:///banque.db', echo=True)

    
    # Base.metadata.create_all(engine)    # Only for the first time

    clientDao = ClientDaoSA(engine)

    clients = clientDao.findAll()

    print(clients)

    marine = Client(email = "marine@hotmail.com", nom="GINOUX", prenom="Marine")

    dorian = Client(email = "dorian@gmail.com", nom="TERBAH", prenom="Dorian")
    
    pierre = Client(email = "pierre@gmail.com", nom="FREBAULT", prenom="Pierre")

    marine = clientDao.create(marine)
    dorian = clientDao.create(dorian)
    pierre = clientDao.create(pierre)

    print(clientDao.findAll())

    print(pierre)

    pierreFind = clientDao.findById(pierre.id)

    pierreFind.nom = "FREBOLT"

    clientDao.update(pierreFind)

    print(clientDao.findAll())

    clientDao.deleteById(marine.id)

    print(clientDao.findAll())
```

