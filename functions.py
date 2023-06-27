import library

# définition
def hello():
    print('Hello Python!')

# appel ou exécution
hello()

def hello2(name):
    print(f"Hello {name}!")

hello2('Foo')


# paramètres + retour de valeur
def addition(a, b):
    return a + b

resulat = addition(42, 123)
print(resulat)

# appel d'une fonction stockée dans un autre module
resulat = library.oui_non(False)
print(resulat)
print(library)

# reverse lookup
my_list = [42, 123, 3.14]

def reverse_lookup(my_list, value):
    """Cette fonction prend en paramètre une liste et une valeur à rechercher.
    Elle renvoie l'index de la valeur si elle est trouvée, ou None si la valeur n'est pas trouvée.

    my_list list la liste dans laquelle il fait chercher value any la valeur à rechercher return
    int si la valeur ou None si la valeur n'est pas trouvée.
    """

    for i in range(len(my_list)):
        if my_list[i] == value:
            # @dev
            # print(f'{i = }')
            return i

    return None

result = reverse_lookup(my_list, 0)
print(result)

