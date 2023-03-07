from collections import deque

def ndfa_to_dfa(Q, sigma, delta, q0, F):
    """
    Converts an NDFA to a DFA using the powerset construction algorithm.
    Q: set of states in the NDFA
    sigma: set of input symbols in the NDFA
    delta: transition function of the NDFA (a dictionary mapping (q, a) to a set of states)
    q0: initial state in the NDFA
    F: set of final states in the NDFA
    Returns the equivalent DFA as a tuple (Q_DFA, sigma_DFA, delta_DFA, q0_DFA, F_DFA).
    """
    # Initialize the DFA with the empty set as the initial state
    q0_DFA = frozenset([q0])
    Q_DFA = {q0_DFA}
    F_DFA = set()
    delta_DFA = {}

    # Use a queue to process unexplored DFA states
    queue = deque([q0_DFA])

    while queue:
        q_DFA = queue.popleft()
        for a in sigma:
            # Compute the set of NDFA states that the DFA state q_DFA transitions to on input a
            q_NDFA = set()
            for q in q_DFA:
                q_NDFA |= delta.get((q, a), set())
            q_NDFA = frozenset(q_NDFA)
            if q_NDFA:
                # Add the new DFA state to the set of states if it hasn't been explored yet
                if q_NDFA not in Q_DFA:
                    Q_DFA.add(q_NDFA)
                    queue.append(q_NDFA)
                # Add the DFA transition (q_DFA, a) -> q_NDFA
                delta_DFA.setdefault(q_DFA, {})[a] = q_NDFA
        # If q_DFA contains a final state in the NDFA, mark it as a final state in the DFA
        if q_DFA & F:
            F_DFA.add(q_DFA)

    # Convert the sets to tuples to remove the "frozenset" keyword from the output
    Q_DFA = tuple(tuple(q) for q in Q_DFA)
    F_DFA = tuple(tuple(q) for q in F_DFA)
    delta_DFA = {tuple(q): {a: tuple(q_NDFA) for a, q_NDFA in transitions.items()} for q, transitions in delta_DFA.items()}
    q0_DFA = tuple(q0_DFA)

    return Q_DFA, sigma, delta_DFA, q0_DFA, F_DFA

Q = {'q0', 'q1', 'q2', 'q3'}
sigma = {'a', 'b', 'c'}
delta = {('q0', 'a'): {'q0', 'q1'},
         ('q1', 'b'): {'q2'},
         ('q2', 'a'): {'q2'},
         ('q2', 'c'): {'q3'},
         ('q3', 'c'): {'q3'}}
q0 = 'q0'
F = {'q3'}

Q_DFA, sigma_DFA, delta_DFA, q0_DFA, F_DFA = ndfa_to_dfa(Q, sigma, delta, q0, F)
print("Transitions DFA =", delta_DFA)

