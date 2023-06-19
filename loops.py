import random
# while : c'est comme un "if" mais qui est répété
while False:
    print("ce message ne s'affiche pas")

# exit()

# # ctrl+c pour arrêter le programme
# while True:
# # continue permet de reprendre au début de la boucle suivante
#     continue
#     print()
    
#   print("ce message est affiché en boucle")
# # break permet de sortir d'une boucle
# break

# # premier tirage
dice = random.randint(1,6)

while dice != 6:
    print(f"Je n'ai pas tiré un 6, mais un {dice}")
    print("Je recommence un nouveau tirage")
    dice = random.randint(1,6)

print("J'ai tiré un 6")

# recréation de la boucle fpr classique avec une boucle while
i = 0
while i < 10:
    print(f'{i = }')
    i += 1

# boucle for classique en python
# 0 est inclus mais 10 est exclu

# boucle à rebours
for i in range(10, 0, -1):
    print(f'{i = }')

# boucle for each
users = ['jdy', 'foo', 'bar', 'baz']

for user in users:
    print(user)

# enumerate permet de récupérer l'index de chaque élément
for user in enumerate(users):
    print(f"{i = }, {user = }")

# boucle for
for i in range(0, len(users)):
    user = users[i]
    print(f"{i = },{user = }")

# accumulateur
accumulateur = 0
for i in range(1, 11):
    accumulateur += i
    print(f"{i = }")
    print(f"{accumulateur = }")

print(f"{accumulateur = }")
