# nombre entier, integer
number1 = 123
number1 = 42
print(number1)

#nomnre à virgule flottante, float
number2 = 3.14
print(number2)

#chaîne de caractères, string
text1 = "foo bar baz"
print(text1)

text2 = "foo bar baz"
print(text2)

#booléen, boolean
python_is_cool = True
print(python_is_cool)

python_is_boring = False
print(python_is_boring)

#null
accepted_terms = None
print(None)


# types de données
print (type (number1))
print (type(number2))
print (type(text1))
print (type(text2))
print (type(python_is_cool))
print (type(python_is_boring))
print (type(user_accepted_terms))

#vérification du type de données
print(type(number1) is int)
print(type(number1) is str)

#todo: interroger le type des autres variables...

# transtypage
print(type(str(number1)))
print(bool(number1))





# les fonctions de transtypage
#srt() convertit vers un string
#int() convertit vers un integer
#float() convertit vers float
#bool() convertit vert booléan
















#chaîne de caractères, string
text4 = """<div>
    <h1>Titre de premier niveau</h1>
 </div>
 """


print(text4)


# \n est équivalent à un saut de ligne
# \t est équivalent à une tabulation

 text5 = "<div>\n\t<h1>Titre de premier niveau</h1>\n</div>\n"

 print (text5)

# la backslash seul est le caractère d'échappement
# \" est équivalent à une guillemet
# \\ est équivalent à un back slash \

# \" est équivalent à un saut de ligne
text6 = "Foo \"Bar\" Baz"
print(text6)

text7 = "C:\\Program Files\\Foo"
print(text7)

#permutez les deux variables a et b en utilisant l'operateur d'affectation et le nom des variables.
a =123
b =42

# pemutation des valeurs à l'aide d'une variable temporaire
c = b
b = a
a = c


print(a)
print(b)




# addition le float
#affiche
print(0.1 + 0.1 + 0.1)



#affiche correctement 0.3
print(Decimal("0.1") +Decimal("0.1") +Decimal("0.1"))

import decimal
from decimal



#affiche  correctement 0.3










#arrondi des floats
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
Decimal("0.05").quantize(Decimal("1"))
Decimal("0.15").quantize(Decimal("0.1"))

