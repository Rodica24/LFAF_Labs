# Topic: Chomsky Normal Form

### Course: Formal Languages & Finite Automata

### Author: Prodan Rodica, FAF-211

### Variant: 20

---

## Theory

A grammar is in Chomsky Normal Form if all its production rules are of the form:
`A → BC or A → a` ,
meaning that there are either two non-terminal symbols or one terminal symbol.

To obtain grammar in CNF we have to follow these 5 steps:
1. Eliminate ε productions.
2. Eliminate unit productions.
3. Eliminate inaccessible symbols.
4. Eliminate the non productive symbols.
5. Obtain the Chomsky Normal Form.

## Objectives:

1. Learn about Chomsky Normal Form (CNF).
2. Get familiar with the approaches of normalizing a grammar.
3. Implement a method for normalizing an input grammar by the rules of CNF.
   1. The implementation needs to be encapsulated in a method with an appropriate signature (also ideally in an appropriate class/type).
   2. The implemented functionality needs executed and tested.
   3. A BONUS point will be given for the student who will have unit tests that validate the functionality of the project.
   4. Also, another BONUS point would be given if the student will make the aforementioned function to accept any grammar, not only the one from the student's variant.

## Implementation description

First of all, I had to remove the epsilon productions. For this I have the `eliminate_epsilon` and `combine_epsilon.`
The `eliminate_epsilon()` method takes a set of productions and removes all epsilon productions from them.
It first makes a copy of the productions, finding all symbols that have an epsilon production, and creating a new dictionary. Then, iterates over each symbol in the new dictionary and for each occurrence of a symbol that can derive epsilon, it adds new productions to the new dictionary that combine the original production with all possible 
combinations of the epsilon productions for that symbol.
```
    def eliminate_epsilon(self):
        P = self.P.copy()
        eps_productions = [sym for sym in P if '' in P[sym]]
        new_productions = {}
        for sym in P:
            new_productions[sym] = [p for p in P[sym] if p != '']
            for i, p in enumerate(new_productions[sym]):
                for j in range(len(p)):
                    if p[j] in eps_productions:
                        for eps_prod in self.combine_epsilon(P[p[j]]):
                            new_productions.setdefault(sym, []).append(p[:j] + eps_prod + p[j + 1:])
        self.P = new_productions
```
Then, we have to remove unit productions. The `eliminate_unit` method iterates through each production and it checks if the symbol is a non-terminal symbol. If it is, the method removes the non-terminal symbol and replaces it with all the productions that can be derived from it.
```
    def eliminate_unit(self):
        for production in self.P:
            for symbol in self.P[production]:
                if symbol in self.VN:
                    self.P[production].remove(symbol)
                    self.P[production].extend(self.P[symbol])
```
Then, we have to remove the non productive and inaccessible symbols. The `eliminate_nonproductive_inaccessible` method is responsible for this.
It initializes two sets: reached, which contains all the symbols that can be derived from the start symbol and unreached, 
which initially contains all the non-terminal symbols in the grammar. For each production, the method checks if all symbols on the right-hand side are either in reached or are terminal symbols. 
If so, the non-terminal symbol is added to reached and removed from unreached. At last, the method identifies all the non-terminal symbols in unreached as being nonproductive and eliminates them from the grammar.
```
    def eliminate_nonproductive_inaccessible(self):
        reached = set()
        unreached = self.VN.copy()
        reached.add(self.S)
        while True:
            changed = False
            for sym in self.P:
                if sym in unreached:
                    for prod in self.P[sym]:
                        if all(s in reached or s in self.VT for s in prod):
                            unreached.remove(sym)
                            reached.add(sym)
                            changed = True
                            break
                if changed:
                    break
            if not changed:
                break

        nused = unreached
        for sym in nused:
            del self.P[sym]
            self.VN.remove(sym)
            if sym == self.S:
                self.S = None
        self.VT = set(t for prod in self.P.values() for s in prod for t in s if t not in self.VN)
```
After all, we have to convert the resulting CFG to CNF. It first adds a new starting symbol to the CFG and adds a new production that derives the old starting symbol to this new starting symbol.
```
self.VN.append('S0')
        dict = {'S0': ['S']}
        self.P = {**dict, **self.P}
```
To keep track of all new non-terminal symbols and their corresponding productions, it builds a dictionary. The process then repeats for each production that has more than two symbols across all of the products.
```
final = {}
        dict = {}
        flag = 0
        for production in self.P:
            for symbol in self.P[production]:
                if len(symbol) > 1:
                    for char in symbol:
                        if char in self.VT and char not in final.values():
                            final[chr(70 + flag)] = char
                            dict[char] = chr(70 + flag)
                            flag += 1

        for item in dict.keys():
            for production in self.P:
                for i in range(len(self.P[production])):
                    if len(self.P[production][i]) > 1:
                        self.P[production][i] = self.P[production][i].replace(item, dict[item])
```

## Conclusions / Screenshots / Results

After completing this laboratory work, I learnt how to convert CFG into CNF. In order to complete all the necessary steps and observe the immediate results, I implemented different functions.

After running the project I got the following results:
```
Productions:
P = {'S': ['aB', 'bA', 'A'], 'A': ['B', 'Sa', 'bBA', 'b'], 'B': ['b', 'bS', 'aD', ''], 'D': ['AA'], 'C': ['Ba']}

Chomsky Normal Form:
P = {'S0': ['S'], 'S': ['FB', 'GA', 'A', 'a', 'b', 'SF'], 'A': ['B', 'SF', 'b', 'YZ', 'a', 'YA', 'YB'], 'B': ['b', 'GS', 'FD', 'a'], 'D': ['AA', 'SF', 'GA', 'GB', 'a', 'b'], 'F': 'a', 'G': 'b'}
```

## References
1. https://www.geeksforgeeks.org/converting-context-free-grammar-chomsky-normal-form/
