fruits = {
    'à' : 'ananas',
    'b' : 'banane',
    'c' : 'cerise',
}

print(fruits)

# accés en lecture
print(fruits['a'])
fruit = fruits['a']

# accés en écriture
fruits['a'] = 'abricot'

print(fruits)

# boucle foreach
for fruit in fruits:
    print(f"key = {fruit}")
    print(f"fruit = {fruits[key]}")

# boucle foreach pour obtenir les clés et les valeurs en même temps
for key, value in fruits.items():
    print(f"{key = }")
    print(f"{value = }")

# boucle foreach pour obtenir les valeurs en seulement
for value in fruits.items():
    print(f"{value = }")

# dictionaire avec clés de tout type
my_dict = {
    100: 'foo',
    # si une même réapparait, elle ecrase la première
    100: 'bar',
    3.14: True,
    True: 'abc',
    None: 123,
}

# ajouter une nouvelle entrée
my_dict['baz'] = 1
print(my_dict)

# suprimer une entrée existante en gardant une copie
a = my_dict.pop(101)
print(my_dict)

# suprimmer une entrée existante sans garder de copie
del my_dict['baz']
print(my_dict)
