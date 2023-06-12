# import du module random (pour les nombres aléatoires)
import random 

# arithmétique
a = 123 + 42
a = 123 - 42
a = 123 * 42
a = 123 / 42

# division entière, integer division
a = 123 // 42
print(a)

# modulo ou reste de la division (euclidienne)
a = 53
#s'il y a u reste, le nombre n'est pas divisible par deux, il n'est pas pair
print(a % 2)

a = 74
#s'il y a u reste, le nombre n'est pas divisible par deux, il n'est pas pair
print(a % 2)

# puissance, expponentiation
# deux puissance trois
# opérateurs de comparaison
a = 2 ** 3


# opérateurs de comparaison
# d'égalité
result = 123 == 42
print(result)

# différent de
print(123 != 42)


# (strictement) plus grand que
print(123 > 42)

# plus grand ou egal à
print(123 >= 42)

# (strictement) plus grand que
print(123 < 42)

# plus grand ou egal à
print(123 <= 42)


# opérateur composés
b = 0

# incrémentation

# b = b + 1
b += 1
b += 1
print(b)

# incrémentation

# b = b - 1
b -= 1
print(b)

# multiplication
c = 3
#c = c * 2
c *= 2
print(c)

# division
d = 12
# d = d / 3
d /= 12
print(d)

# division entière
d = 10
# d = d // 3
d //= 3
print(d)

# opérateur d'inclusion
text1 = "lorem ipsum"

result = "e" in text1
print(result)
print("e" in text1)
print("lorem" in text1)

list1 = ['Lorem','ipsum']
print("e" in list1)
print("ipsum" in list1)

# comparaison avec des nombres aléatoires
e = random.randint(0, 100)
f = random.randint(0, 100)

print(e)
print(f'{e = }')
print(f'{f = }')

result = e ==f
print(result)

result = e < f
print(result)

# expression
# 1 + 1 -> 2
# (100 + 2) * 3 -> 102 * 3 -> 306
# 1 + 1 > (100 + 2) * 3 -> 2 > 306 -> False
# random.randit(0, 100) -> 100
# print(100) ->
