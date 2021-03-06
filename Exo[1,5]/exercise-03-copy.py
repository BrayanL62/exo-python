# exercise-03.py

# exo 3.1
# Calculez la moyenne des nombres suivants : 1, 1, 2, 3, 5, 8, 13.
# Affectez le résultat à une variable et affichez le résultat.

# réponse 3.1
note_1 = 1
note_2 = 1
note_3 = 2
note_4 = 3
note_5 = 5
note_6 = 8
note_7 = 13

nb_notes = 7
my_moy = (note_1 + note_2 + note_3 + note_4 + note_5 + note_6 + note_7) / nb_notes

print(round(my_moy, 2))
print()
# exo 3.2
# On est en vacance et on veut suivre ses dépenses quotidiennes.
# Stockez le montant de chacune des dépenses quotidiennes dans une variable différente :
# - day1 : 26,82
# - day2 : 42,00
# - day3 : 31,41
# - day4 : 63,7
# - day5 : 32
# Stockez le nombre de jours dans une variable.
# Calculez le montant total des dépenses.
# Calculez la moyenne des dépenses quotidiennes en utilisant la variable contenant le nombre de jours et le total.
# Affichez le nombre jours, le montant total et la moyenne des dépenses.

# réponse 3.2
day_1 = 26.82
day_2 = 42.00
day_3 = 31.41
day_4 = 63.7
day_5 = 32

nb_days = 5 

total_expenses = day_1 + day_2 + day_3 + day_4 + day_5
moy_expenses = (day_1 + day_2 + day_3 + day_4 + day_5) / nb_days

print(nb_days)
print(total_expenses)
print(round(moy_expenses, 2))
print()
# exo 3.3
# La formule suivante permet de convertir des mètres en miles :
# miles = meters / 1609.344
# Je dois marcher 2371 m pour aller jusqu'à la plus proche boulangerie.
# Combien cela fait-il en miles ?
# Affichez un résultat arrondi

# réponse 3.3

meters = 2371
miles = meters / 1609.344

print(round(miles, 2))
print()

# exo 3.4
# La formule suivante permet de calculer le montant de la TVA à partir d'un prix « hors TVA » (HTVA) et du taux de la TVA en pourcentage
#
# tax_fee = price * tax_rate / 100
#
# La variable price contient le prix HTVA
# La variable tax_rate contient le taux de la TVA en pourcentage (c-à-d le nombre 20 si la TVA est de 20 %)
# Affichez le montant de la TVA à partir du prix HTVA et du taux de TVA

price = 314
tax_rate = 20

# réponse 3.4
tax_fee = price * tax_rate /100
print(tax_fee)

# exo 3.5
# La formule suivante permet de calculer un prix TVA inlcuse à partir du prix HTVA et du taux de TVA en pourcentage
#
# tax_included_price = price + price * tax_rate / 100
#
# ou encore
#
# tax_included_price = price * (1 + tax_rate / 100)
#
# La variable price contient le prix HTVA
# La variable tax_rate contient le taux de la TVA en pourcentage (c-à-d le nombre 20 si la TVA est de 20 %)
# Affichez le prix TVA incluse à partir du prix HTVA et du taux de TVA

price = 271
tax_rate = 20

# réponse 3.5
tax_included_price = price * (1 + tax_rate / 100)
print(tax_included_price)