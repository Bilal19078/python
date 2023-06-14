import random

if True:
    print("Ce message s'affichera toujours")

if False:
    print("Ce message ne s'affichera jamais")

number1 = random.randint(0,10)
number2 = random.randint(0,10)

print(f'{number1}')
print(f'{number2}')

if number1 <  number2:
    print("number1 est plus petite de number2")

else: # number1 >= number2
    print("La variable number1 est plus grande ou égale à number2")
    
if number1 <  number2:
    print("number1 est plus petite de number2")

elif number1 > number2:
   print("La variable number1 est plus grande que number2")
else:
    print("Les deux variables number1 et number2 sont égales")

    # elif = else if

    # réecriture du block if3 avec des if imbriqués
    if number1 < number2:
        print("La variable number1 est plus grande que number2")
    else:
        print("Les deux variables number1 et number2 sont égales")

# opérateurs booléens

# négation
print(not True)
print(not False)

# table de vérité de l'operateur de négation
# A     not A
# True False
# False True


# OU logique
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# table de vérité del'operateur OU logique
# A      B       A or B
# True   True      True
# True   False    True
# False  True     True
# False  False    False

# pour retrouver la table, remplacez:
# - A par "j'ai du cash"
# - B par "j'ai ma cb"
# - "A or B" par "puis-je faire mes courses?"


# ET logique 
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# table de vérité del'operateur OU logique
# A      B       A or B
# True   True      True
# True   False    False
# False  True     False
# False  False    False

# table de vérité del'operateur NAND (not and)
# A      B       A or B     not (A and B)
# True   True      True      False
# True   False    True      True
# False  True     True      True
# False  False    False     True


# OU EXLUSIF (xor)
print(True ^True)
print(True ^False)
print(False ^ True)
print(False ^ False)

# table de vérité de l'operateur XOR
# A      B        A xor B
# True   True      False
# True   False     True
# False  True      True
# False  False     False

# exo course (opérateur OU logique)
# affichez : 
# - "je peux aller faire les courses" si on a au moins un moyen de paiement
# - "je ne peux pas aller faire les courses" si je n'ai aucun moyen de paiement
has_cash = bool (random.randint(0, 1))
has_cb = bool (random.randint(0, 1))

print(f'{has_cash = }')
print(f'{has_cb = }')

if has_cash or has_cb:
    print("je peux aller faire les courses")
else:
    print("je ne peux pas aller faire les courses")

    # exo courses (opérateur ET logique)
    # remplissez le même cahier des charges mais avec l'opérateur ET 
    







# exo carte de réduction
# déterminez la carte de réduction auquelle le voyageur a droit : 
# - entre 0 et 11 and (inclus), le voyageur a droit à la gratuité
# - entre 12 et 25 ans (inclus), le voyageur a droit à une réduction de 50%
# - entre 26 et 64 and (inclus), le voyageur a droit une réduction de 10% 
# - au delà de 65 ans (inclus), le voyageur a droit à une réduction de 50%

age = random.randint(0, 99)

