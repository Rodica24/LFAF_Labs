def fa_to_grammar(Q, sigma, delta, q0, F):
    productions = {}

    for f in F:
        productions[f] = []

    for q in Q:
        for a in sigma:
            # get the target state of the transition
            target = delta.get((q, a))

            # target state exists - a production added
            if target is not None:
                # target state is final - an empty string added
                if target in F:
                    productions[q] = productions.get(q, []) + [a + target, a]
                else:
                    productions[q] = productions.get(q, []) + [a + target]

    # add productions for the starting state
    productions[q0] = [s for s in productions.get(q0, []) if s != '']

    return productions

def is_deterministic(Q, sigma, delta):
    # initialize a set of seen states for each input symbol
    seen_states = {a: set() for a in sigma}

    for q, a in delta:
        target = delta[(q, a)]

        # check if the target state has already been seen for the input symbol
        if target in seen_states[a]:
            return False
        else:
            seen_states[a].add(target)

        # check if the target state exists
        if target not in Q:
            return False

    # if all transitions are valid and unique, the automaton is deterministic
    return True


Q = {'q0', 'q1', 'q2', 'q3'}
sigma = {'a', 'b', 'c'}
delta = {('q0', 'a'): 'q0', ('q0', 'b'): 'q1', ('q2', 'a'): 'q2', ('q1', 'b'): 'q2', ('q2', 'c'): 'q3', ('q3', 'c'): 'q3'}
q0 = 'q0'
F = {'q3'}


grammar = fa_to_grammar(Q, sigma, delta, q0, F)
#grammar
for nonterminal in grammar:
    productions = ' | '.join(grammar[nonterminal])
    print(nonterminal + ' -> ' + productions)

if is_deterministic(Q, sigma, delta):
    print("The FA is deterministic")
else:
    print("The FA is non-deterministic")


