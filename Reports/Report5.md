# Topic: Parser & Building an Abstract Syntax Tree

### Course: Formal Languages & Finite Automata
### Author: Prodan Rodica, FAF-211

----

## Overview
A `parser` is a software component that takes input data and builds a data structure – often some kind of parse tree, 
abstract syntax tree or other hierarchical structure, giving a structural
representation of the input while checking for correct syntax. The parser is often preceded by a separate lexical analyser, which creates tokens from the sequence of input characters; 
alternatively, these can be combined in scannerless parsing.

An abstract syntax tree `AST`, is a tree representation of the abstract syntactic structure of text written in a formal language. 
Each node of the tree denotes a construct occurring in the text.
## Objectives:
1. Get familiar with parsing, what it is and how it can be programmed [1].
2. Get familiar with the concept of AST [2].
3. In addition to what has been done in the 3rd lab work do the following:
   1. In case you didn't have a type that denotes the possible types of tokens you need to:
      1. Have a type __*TokenType*__ (like an enum) that can be used in the lexical analysis to categorize the tokens. 
      2. Please use regular expressions to identify the type of the token.
   2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
   3. Implement a simple parser program that could extract the syntactic information from the input text.


## Implementation description:
As I've implemented on the third laboratory simple mathematical expression, I continued to work on that.
I've created the `Parser` class that performs recursive descent parsing to evaluate arithmetic expressions based on a given list of tokens.

The `parse_expression` method starts by parsing the first term using the `parse_term` method. It then enters a loop to check if there are additional terms to be added or subtracted. If the current token is an "Addition" token, it advances the position, parses the next term, and constructs an AST node representing the addition operation. The same process is followed for the "Subtraction" token.
```
    def parse_expression(self):
        result = self.parse_term()
        while self.pos < len(self.tokens):
            if self.tokens[self.pos][1] == "Addition":
                self.pos += 1
                right = self.parse_term()
                result = ('OPERATOR', '+', result, right)
            elif self.tokens[self.pos][1] == "Subtraction":
                self.pos += 1
                right = self.parse_term()
                result = ('OPERATOR', '-', result, right)
            else:
                break
        return result
```

The `parse_term` function starts by parsing the first factor using the `parse_factor` method. 
It then enters a loop to check if there are additional factors to be multiplied or divided. The loop continues as long as there are tokens remaining and the current token is a multiplication or division operator.
```
    def parse_term(self):
        result = self.parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][1] in ("Multiply", "Divide"):
            if self.tokens[self.pos][1] == "Multiply":
                self.pos += 1
                right = self.parse_factor()
                result = ('OPERATOR', '*', result, right)
            else:
                self.pos += 1
                right = self.parse_factor()
                result = ('OPERATOR', '/', result, right)
        return result
```

The `parse_factor` method handles parsing factors, which can be digits, identifiers, equal sign, or expressions enclosed in parentheses.
```
    def parse_factor(self):
        current_token = self.tokens[self.pos]
        token_type = current_token[1]

        if token_type == "Digit":
            result = ('DIGIT', current_token[0])
            self.pos += 1
            return result
        elif token_type == "Identifier":
            result = ('IDENTIFIER', current_token[0])
            self.pos += 1
            return result
        elif token_type == "Operator" and current_token[0] == "=":
            result = ('OPERATOR', '=', current_token[0])
            self.pos += 1
            return result
        elif token_type == "LeftP":
            self.pos += 1
            result = self.parse_expression()
            if self.tokens[self.pos][1] != "RightP":
                raise Exception(f"Missing closing parenthesis")
            self.pos += 1
            return result
        else:
            raise Exception(f"Invalid syntax: {current_token[0]}")
```

This parser recursively analyzes the structure of the input expression, constructs an abstract syntax tree (AST) representing the expression's hierarchy, and performs error checking for invalid syntax.
Afterwards, the `print_ast` function is responsible for printing the AST in a human-readable format.
```
def print_ast(ast, indent=""):
    node_type, *node_values = ast
    print(f"{indent}{node_type} ({node_values[0]})")
    for node in node_values[1:]:
        if isinstance(node, tuple):
            print_ast(node, indent + "  ")
        else:
            print(f"{indent}  {node_type} ({node})")
```

## Results
So, for the inputted string:

```( 3 + x ) -  a / b  * 2```

I received this output:

```
OPERATOR (-)
  OPERATOR (+)
    DIGIT (3)
    IDENTIFIER (x)
  OPERATOR (*)
    OPERATOR (/)
      IDENTIFIER (a)
      IDENTIFIER (b)
    DIGIT (2)
 ```

## Conclusions
In this laboratory work I learned and implemented the parser and AST alongside the existent lexer. 
I understood their use and what role they play in the language design and implementation.


## References:
[1] [Parsing Wiki](https://en.wikipedia.org/wiki/Parsing)

[2] [Abstract Syntax Tree Wiki](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
 