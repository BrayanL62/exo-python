# exercise-02.py

# exo 2.1
# Affectez :
# - le nombre 42 à une variable
# - le nombre d'or 1,61 à une variable
# - votre nom et prénom à une variable
# - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux, à une variable
# - la valeur null `None` à une variable
# Affichez ces variables

# réponse 2.1
my_int = 42
my_float = 1.61
my_name = 'Loucher Brayan'
is_morning = True
is_afternoon = False
my_null = None

print(my_int)
print(my_float)
print(my_name)
print(is_morning)
print(is_afternoon)
print(my_null)
# code 2.1
# la fonction `round()` permet d'arrondir un float en un integer
# 0,1 est arrondi à la valeur inférieur
print(round(0.1))
# 0,9 est arrondi à la valeur supérieur
print(round(0.9))
# la fonction `round()` permet aussi d'arrondir en précisant le nombre de chiffres après la virgule
# arrondir à un nombre décimal à 4 chiffres après la virgule
print(round(1 / 3, 4))
print()

# exo 2.2
# Stockez le valeurs suivantes dans une variable et transtypez-les :
# - integer 2 en un float
# - float 1,62 en un integer
# - float 1,62 en un float arrondi en un integer
# - float 1,62 en un float arrondi en un float à un chiffre après la virgule
# À chaque fois stockez le résultat dans une variable et affichez le résultat.

# réponse 2.2
my_num = float(2)
my_integer = (int(1.62))
my_coma = round(1.62)
my_last = round(1.62, 1)


print(my_num)
print(my_integer)
print(my_coma)
print(my_last)