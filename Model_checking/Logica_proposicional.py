import string

from logic import *

# Cuatro diferentes casas
Gryffindorf = "pertenece a Gryffindorf"
Hufflepuff = "pertenece a Hufflepuff"
Ravenclaw = "pertenece a Ravenclaw"
Slytherin = "pertenece a Slytherin"
casas = [Gryffindorf, Hufflepuff, Ravenclaw, Slytherin]

# Cuatro diferentes habitantes
Gilderoy = "Gilderoy"
Pomona = "Pomona"
Minerva = "Minerva"
Horace = "Horace"
personajes = [Gilderoy, Pomona, Minerva, Horace]

# Funcion que arroja SI si la función model_check pudo
# encontrar una implicación. De lo contrario TAL VEZ
def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"{symbol}: SI")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: TAL VEZ")


letras_mayusculas = list(string.ascii_uppercase) #Lista con abecedario en mayusculas
symbols = []
z = 0
#Se concatena los strings y se nombran con las letras mayusculas de la lista letras_mayusculas respectivamente
for i in range(len(personajes)):
    for j in range(len(casas)):
        globals()[letras_mayusculas[z]] = Symbol(personajes[i] + ' ' + casas[j] + ' - (' + str((letras_mayusculas[z])) + ')')
        symbols.append(globals()[letras_mayusculas[z]])
        z += 1

#Tiene que haber un personaje en cada casa
knowledge = And(
    Or(A, B, C, D),
    Or(E, F, G, H),
    Or(I, J, K, L),
    Or(M, N, O, P)
)

#Si un personaje ya tiene casa, se quitan las demas casas para el
knowledge.add(And(
    Implication(A,And(Not(B), Not(C), Not(D))),
    Implication(B,And(Not(A), Not(C), Not(D))),
    Implication(C,And(Not(A), Not(B), Not(D))),
    Implication(D,And(Not(A), Not(B), Not(C))),
    Implication(E,And(Not(F), Not(G), Not(H))),
    Implication(F,And(Not(E), Not(G), Not(H))),
    Implication(G,And(Not(E), Not(F), Not(H))),
    Implication(H,And(Not(E), Not(F), Not(G))),
    Implication(I,And(Not(J), Not(K), Not(L))),
    Implication(J,And(Not(I), Not(K), Not(L))),
    Implication(K,And(Not(I), Not(J), Not(L))),
    Implication(L,And(Not(I), Not(J), Not(K))),
    Implication(M,And(Not(N), Not(O), Not(P))),
    Implication(N,And(Not(M), Not(O), Not(P))),
    Implication(O,And(Not(N), Not(N), Not(P))),
    Implication(P,And(Not(M), Not(N), Not(O))),
    ))

#Si una casa ya tiene personaje, se le quitan los demas personajes para ella
knowledge.add(And(
    Implication(A,And(Not(E), Not(I), Not(M))),
    Implication(B,And(Not(F), Not(J), Not(N))),
    Implication(C,And(Not(G), Not(K), Not(O))),
    Implication(D,And(Not(H), Not(L), Not(P))),
    Implication(E,And(Not(A), Not(I), Not(M))),
    Implication(F,And(Not(B), Not(J), Not(N))),
    Implication(G,And(Not(C), Not(K), Not(O))),
    Implication(H,And(Not(D), Not(L), Not(P))),
    Implication(I,And(Not(A), Not(E), Not(M))),
    Implication(J,And(Not(B), Not(F), Not(N))),
    Implication(K,And(Not(C), Not(G), Not(O))),
    Implication(L,And(Not(D), Not(H), Not(P))),
    Implication(M,And(Not(A), Not(E), Not(I))),
    Implication(N,And(Not(B), Not(F), Not(J))),
    Implication(O,And(Not(C), Not(G), Not(K))),
    Implication(P,And(Not(D), Not(H), Not(L))),
    ))

#Gilderoy pertence a Gryffindorf o a ravenclaw
knowledge.add(And(
    Or(A,C),
    Not(And(A,C)),
    ))

#Pomona no pertenece a Slytheri
knowledge.add(
    Not(H)
)

#Minerva pertence a Gryffindorf
knowledge.add(
    (I)
    )

#print(KB.formula())
check_knowledge(knowledge)