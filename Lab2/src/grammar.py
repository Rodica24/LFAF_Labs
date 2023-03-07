import random

class Grammar:
    def __init__(self):
        self.VN = {'S', 'A', 'B', 'C'}
        self.VT = {'a', 'b', 'c', 'd'}
        self.P = {
            'S': {'dA'},
            'A': {'d', 'aB'},
            'B': {'bC'},
            'C': {'cA', 'aS'}
        }
        self.S = 'S'

    def generate_strings(self):
        # Initialization of an empty set to store the generated strings
        strings = set()
        while len(strings) < 5:
            # Begin with the start symbol
            string = self.S
            # Derivation of the string until we can no longer replace any nonterminal symbols
            while any(symbol in self.VN for symbol in string):
                # Initialization of an empty list to store the available choices
                choices = []
                # For each nonterminal symbol, finding all possible right-hand sides for the corresponding production rule
                for j, symbol in enumerate(string):
                    if symbol in self.VN:
                        for right in self.P[symbol]:
                            # Addition of each possible choice to the list of available choices.
                            choices.append((j, symbol, right))
                # Randomly chosen choice is replaced
                if choices:
                    j, symbol, right = random.choice(choices)
                    string = string[:j] + right + string[j + 1:]
                else:
                    break
            # Check if the resulting string has only terminal symbols, adding it to the set of generated strings
            if all(symbol in self.VT for symbol in string):
                strings.add(string)
        return list(strings)

    def classify_grammar(self):
        # Check if all productions are of the form A -> wB or A -> w, where w is a string of terminals and B is a nonterminal
        if all((right[0] in self.VT and right[1:] in self.VN) or (all(symbol in self.VT for symbol in right))
               for rights in self.P.values() for right in rights):
            return "Type 3"

        # Check if all productions are of the form A -> aB or A -> a, where a is a terminal and B is a nonterminal
        if all((len(right) == 2 and right[0] in self.VT and right[1] in self.VN) or (len(right) == 1 and right in self.VN)
               for rights in self.P.values() for right in rights):
            return "Type 2"

        # Check if all productions are of the form A -> BC or A -> a, where B and C are nonterminals and a is a terminal
        if all((len(right) == 2 and right[0] in self.VN and right[1] in self.VN) or (len(right) == 1 and right in self.VT)
               for rights in self.P.values() for right in rights):
            return "Type 1"

        # Check if all productions are of the form A -> w, where w is a string of terminals and nonterminals, and the start symbol does not appear on the right-hand side of any production
        if all((all(symbol in self.VT or symbol in self.VN for symbol in right)) and self.S not in right
               for rights in self.P.values() for right in rights):
            return "Type 0"


grammar = Grammar()
print(grammar.generate_strings())
print(grammar.classify_grammar())

