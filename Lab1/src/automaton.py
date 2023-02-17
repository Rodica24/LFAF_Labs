class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accepting_states = accepting_states

    # The method iterates over each symbol in the input string, updating the current state
    # of the finite automaton based on the transition function.
    # If there is no valid transition for the current state and input symbol, the method returns False.
    # If the entire input string is processed and the final state is an accepting state, the method returns True.
    # Otherwise, it returns False.
    def accepts(self, n):
        current_state = self.start_state
        for symbol in n:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
        return current_state in self.accepting_states

def convert_grammar_to_fa():
    states = {'S', 'A', 'B', 'C'}
    alphabet = {'a', 'b', 'c', 'd'}
    transitions = {('S', 'd'): 'A', ('A', 'd'): 'A', ('A', 'a'): 'B', ('B', 'b'): 'C', ('C', 'c'): 'A',
                       ('C', 'a'): 'S'}
    start_state = 'S'
    accept_states = {'A', 'B', 'C'}
    return FiniteAutomaton(states, alphabet, transitions, start_state, accept_states)


fa = convert_grammar_to_fa()
print(fa.accepts("dabcd"))
print(fa.accepts("daabc"))



