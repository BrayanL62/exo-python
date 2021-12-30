# exercise-06.py

import random

# Remarque 6.1
# Dans le texte, quand il est écrit Xème position, cela correspond à l'index X-1

# exo 6.1
# Créez une liste nommée `my_list` contenant un nombre entier, un nombre à virgule flottante, une chaîne de caractères et un booléen

# réponse 6.1
my_list = [123, 3.14, 'foo bar baz', False]
# exo 6.2
# Affichez l'élément qui se trouve à la troisième position de la liste
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.2
print(my_list[2])
# exo 6.3
# Ajoutez une chaîne de caractères à la fin de la liste `my_list` (sans modfier le code d'initialisation) et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.3
my_list.append('dolor')
print(my_list)
# exo 6.4
# Supprimez l'élément qui se trouve en deuxième position de la liste et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.4
my_list.pop(1)
print(my_list)
# exo 6.5
# Remplacez l'élément qui se trouve en deuxièm position de la liste par un nombre entier et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.5
my_list[1] = 26
print(my_list)
# exo 6.6
# Affichez la taille de la liste
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.6
print(len(my_list))
# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)
print()
# Remarque 6.2
# les exercices suivants nécessitent l'utilisation d'une boucle `for`

# exo 6.8
# Calculez la somme des nombres de la liste et affichez le résultat
my_list = [2.71, 42]

# réponse 6.8
somme = 0
for num in my_list:
    somme = somme + num

print(somme)
print()
# exo 6.9
# Calculez la somme des nombres de la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.9
somme = 0
for num in my_list:
    somme = somme + num

print(somme)
print()
# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10
somme = 0
num_of_note = 0
for num in my_list:
    somme = somme + num
    num_of_note += 1

print(somme)
print(num_of_note)
average = somme / num_of_note
print(round(average, 2))
print()
# exo 6.11
# Trouvez l'index de la valeur `3.14` dans la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.11
val = 3.14
i = 0
val_found = False
while i<len(my_list):
    if my_list[i] == val:
        val_found = True
        break
    i += 1
print("la valeur 3.14 est à l'index", i)
print()
# exo 6.12
# Comptez les nombres plus petits ou égaux à 10 dans la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.12
inf_egal = 0
for i in my_list:
    if(i <= 10):
        inf_egal += 1
print("il y a", inf_egal, "nombres plus petits ou égaux à 10")
print()

# exo 6.13
# Multipliez chacun des nombres dans la liste par 100, réaffactez le résultat à la place de la valeur originelle puis affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.13
my_list = [i*100 for i in my_list]

print(my_list)
print()
# exo 6.14
# Créez une deuxième liste ne contenant que les nombre entiers de la liste
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.14
my_list2 = my_list[1:4]
print(my_list2)
print()
# exo 6.15
# Ici le but est d'intervertir les éléments de la liste deux à deux
# Liste initiale :
#
#   my_list = [2.71, 42, 123, 2, 3.14, 1.61]
#
# Résultat attendu :
#
#   my_list = [42, 2.71, 2, 123, 1.61, 3.14]
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.15
my_list2 = my_list[0:2]
my_list2.reverse()
print(my_list2)
my_list3 = my_list[2:4]
my_list3.reverse()
print(my_list3)
my_list4 = my_list[4:6]
my_list4.reverse()
print(my_list4)

my_list = my_list2 + my_list3 + my_list4
print(my_list)
print()

# exo 6.16
# Triez la liste en utilisant l'algorithme du tri bulle puis affichez la liste
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.16
def tri_bulle(my_list):
    n = len(my_list)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if my_list[j] > my_list[j+1] :
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

tri_bulle(my_list)
print(my_list)
print()
# code 6.1
# Lire la valeur de la ligne `m` et de la colonne `n` d'un tableau en 2 dimensions
# print(matrix[m][n])
#
# Exemple avec la ligne 2 (index 1) et la colonne 3 (index 2)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# Cette ligne affiche `6`
print(matrix[1][2])
print()
# exo 6.17
# Affichez la valeur qui se trouve à la colonne 4, ligne 3
# Attention : il faut faire `- 1` pour obtenir les index correspondant
size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)


# réponse 6.17
print(matrix)
print(matrix[2][3])
print()
# code 6.2
# Pour afficher toutes les combinaisons possibles de deux nombres de 0 à n inclus vous pouvez utiliser deux boucles `for` imbriquées
#
# Exemple de toutes les combinaisons possibles de deux nombres de 0 à 2 inclus
for i in range(0, 3):
    for j in range(0, 3):
        print(i, j)

# exo 6.18
# Avec le même tableau en 2 dimensions, affichez toutes les valeurs plus petites ou égales à 50 ainsi que leur cordoonnées (ligne et colonne)

# réponse 6.18
matrix = []

for i in range(0, 51):
    matrix.append(i)

print(matrix)
    
