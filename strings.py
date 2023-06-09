text1 = "lorem"
text2 = "ipsum"

#concaténation
text3 = text1 + " " + text2
print(text3)

# interpolation avec ue f-string
text3 = f"{text1} {text2} César"
print(text3)

# attention : la concaténation ne fonctionne qu'avec des str
# solution : convertir les autres types en str
mails = 52
text4 = "Vous avez " + str(mails) + "non lus"
print(text4)

# répétition de texte
text5 = "foo" * 3
print(text5)

# affiche de valeurs arrondies
number1 = 10 / 3
text6 = f"10 / 3 est à peu près {number1}"
text6 = f"10 / 3 est à peu près {number1:.2f}"
print(text6)

# les fonctions associés aux strings
text7 = "Foo bar baz foo"

# longueur (length)
print(len(text7))

# compter des mots
print(text7.count('Foo'))

# retrouve l'emplacement d'un mot
position = text7.find('foo')
print(position)

print(text7.find('foo', position + 1))

# pour trouver l'occurence suivante, il faut chercher une position plus loin
print(text7.find('foo',position + 1))

# si le mot est absent, la fonction renvoie - 1
position = text7.find('lorem')
print(position)

# remplacement de mots
print(text7.replace('foo', 'lorem'))
print(text7)

# split & join
list1 = text7.split(' ')
print(list1)

text8 = "+".join(list1)
print(text8)

# documenter une fonction


def ouiNon(value):
    """cette fonction renvoie :
    - "oui" si la première passé est True
    - "non" si la première passé est False
    - "" dans les autres cas 

    value bool valeur qui sera transformée en "oui" return str
    """
    if value == True:
        return "oui"
    elif value == False:
        return "non"

    return ""

# print(ouiNon.__doc__)
help(ouiNon)
