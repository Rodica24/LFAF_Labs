# Topic: Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

### Course: Formal Languages & Finite Automata
### Author: Prodan Rodica, FAF-211

----

## Theory
&ensp;&ensp;&ensp; Chomsky hierarchy is a containment hierarchy of classes of formal grammars. According to this, there are 4 types of Grammar:
* Type 0, Unrestricted 
* Type 1, Context Sensitive
* Type 2, Context Free
* Type 3, Regular Grammar

**NFA and DFA**
*  A Finite Automata(FA) is said to be deterministic `DFA` if corresponding to an input symbol, there is a single resultant state, only one transition.
*  A Finite Automata(FA) is said to be non-deterministic `NFA` if there is more than one possible transition from one state on the same input symbol.

Therefore, in my variant (20), I had this FA:
```
Q = {q0,q1,q2,q3},
∑ = {a,b,c},
F = {q3},
δ(q0,a) = q0,
δ(q0,a) = q1,
δ(q2,a) = q2,
δ(q1,b) = q2,
δ(q2,c) = q3,
δ(q3,c) = q3.
```
which is `NFA`, because, for instance, from the state `q0` with the `a` input string we can go in both `q0` and `q1`. 

## Objectives:
1. Understand what an automaton is and what it can be used for.

2. Continuing the work in the same repository and the same project, the following need to be added:
    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.
    
    d. Represent the finite automaton graphically (Optional, and can be considered as a __*bonus point*__):
      
    - You can use external libraries, tools or APIs to generate the figures/diagrams.
        
    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.

## Implementation description
In the grammar file, I implemented a function called `classify_grammar`, that classifies it based on Chomsky hierarchy. It determines whether the grammar is a regular grammar first, then whether it is a context-free grammar, and finally whether it is a context-sensitive grammar. The grammar is considered unrestricted if none of these conditions are met.

Regardless the FA tasks, I created a `fa_to_grammar` function that iterates over all possible pairs of states and symbols, gets the target state of the transition and if exists, a production is added, otherwise if the target state is a final state an empty string is added.
Also, there is the function `is_deterministic` that checks if the target state has already been seen for the input symbol.

In the function `ndfa_to_nfa`, the NDFA is converted to a DFA using the powerset construction algorithm. We have to initialize the DFA with the empty set as the initial state, use a queue to process unexplored DFA states and for each unexplored DFA state, the set of NDFA states is being computed. To use the `ndfa_to_dfa` function, it is needed to provide the input for the NDFA as a set of states `Q`, a set of input symbols `sigma`, the transition function `delta` as a dictionary, the initial state `q0`, and the set of final states `F`. The function then returns the equivalent DFA. 

Also, I've tried to implement the graphic view of the NFA, using `matplotlib` and `networkx` libraries, specialized in the representation of graphs.

## Conclusions / Screenshots / Results
First of all, I recived the classification for my grammar which is `Type 3`
![graph](https://user-images.githubusercontent.com/113309236/223562255-01ab3292-7d98-4ae9-86a5-87212b4ba354.png)
