# Laboratory Work Nr.1

### Course: Formal Languages & Finite Automata
### Author: Prodan Rodica

----

## Objectives:

* Understand what a language is and what it needs to have in order to be considered a formal one.

* Provide the initial setup for the evolving project that you will work on during this semester. I said project because usually at lab works, I encourage/impose students to treat all the labs like stages of development of a whole project. Basically you need to do the following:

    a. Create a local && remote repository of a VCS hosting service (let us all use Github to avoid unnecessary headaches);
    
    b. Choose a programming language, and my suggestion would be to choose one that supports all the main paradigms;
    
    c. Create a separate folder where you will be keeping the report. This semester I wish I won't see reports alongside source code files, fingers crossed;

* According to my variant number (by universal convention it is register ID), get the grammar definition and do the following tasks:

    a. Implement a type/class for your grammar;
    
    b. Add one function that would generate 5 valid strings from the language expressed by your given grammar;
    
    c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;
    
    d. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;


## Implementation description

* Grammar Code snippets

I had the variant 20
```
VN={S, A, B, C},
VT={a, b, c, d}, 
P={ 
    S → dA     
    A → d    
    A → aB   
    B → bC    
    C → cA
    C → aS
}
```

To generate 5 valid random strings from the grammar I made a `generate_strings()` function, that begins trom the strat symbol `S`, derives it and stores the choices in a list, then randomly choosing from it. 
```
    def generate_strings(self):
        strings = set()
        while len(strings) < 5:
            string = self.S
            while any(symbol in self.VN for symbol in string):
                choices = []
               for j, symbol in enumerate(string):
                    if symbol in self.VN:
                        for right in self.P[symbol]:
                            choices.append((j, symbol, right))
                if choices:
                    j, symbol, right = random.choice(choices)
                    string = string[:j] + right + string[j+1:]
                else:
                    break
            if all(symbol in self.VT for symbol in string):
                strings.add(string)
        return list(strings)
```
* Finite Automaton Code snippets

To check if a string belongs to the language, I created a method `accepts()`, that iterates over each symbolk in the input string, updating the current state of the FA based on the transition function.
```
    def accepts(self, n):
        current_state = self.start_state
        for symbol in n:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
        return current_state in self.accepting_states
```


## Conclusions / Screenshots / Results

After performing this laboratory work I studied what is a language, what it needs to have in order to be considered a formal one and what is a Finite automaton.