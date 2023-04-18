from CNF import ChomskyNormalForm

V_N = ['S', 'A', 'B', 'C', 'D']
V_T = ['a', 'b']
P = {'S': ['aB', 'bA', 'A'],
     'A': ['B', 'Sa', 'bBA', 'b'],
     'B': ['b', 'bS', 'aD', ''],
     'D': ['AA'],
     'C': ['Ba']
}
S = 'S'

grammar = ChomskyNormalForm(V_N, V_T, P, S)

print('Productions:')
print('P =', P)

print('\nChomsky Normal Form:')
grammar.Chomsky()