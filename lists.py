users = ['foo', 'bar', 'baz']
# mix = [True, 3.14'lorem ipsum', None,[123, 42]]

mix = [
    True,
    3.14
    'lorem ipsum'
    None,
    [123, 42]
]

# 0 est l'index du premier élément
print(users[0])

# len - 1 est l'index du dernier élément
i = len(users) - 1
print(users[i])

# l'index dépasse la taille de la liste
print(users[100 + 42 - i])

# accès en écriture
users[0] = 'lorem'

# ajouter un nouvele élément
users.append('ipsum')

# ajouter un nouvele élément au début ou au millieu
users.insert(0, 'sit')
users.insert(2, 'dolores')
print(users)

 #0      #1     #2
['foo', 'bar', 'baz']

    #0    #1     #2     #3
['foo', 'bar','bar', 'baz']

    #0    #1     #2     #3
['foo', 'bar','baz', 'baz']

    #0    #1     #2     #3
['foo', 'lorem','bar', 'baz']

# retrait du dernier element
last_user = users.pop()
print(last_user)
print(users)

# retrait par index
firtst_user = users.pop(0)
print(firtst_user)

suppresion par valeur
users.remove('bar')
print(users)

# concaténation de liste

fruits = ['ananas', 'banane', 'pomme']
legumes = ['brocoli', 'artichaud', 'carotte']
ingredients = fruits + legumes
print(ingredients)

fruits += legumes
print(fruits)

numbers = ['g', 'd', 'a', 'c', 'b']
numbers = sorted(numbers)
print(numbers)
