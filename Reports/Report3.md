# Topic: Lexer & Scanner

### Course: Formal Languages & Finite Automata
### Author: Prodan Rodica, FAF-211

----

## Objectives:
1. Understand what lexical analysis is.
2. Get familiar with the inner workings of a lexer/scanner/tokenizer.
3. Implement a sample lexer and show how it works.

## Implementation description:
I implemented a lexer that has the purpose to take an input string that represents a simple programming language expression and break it down into a sequence of tokens, where each token represents a distinct element of the expression (such as `identifiers`, `literals`, `operators`, `separators` and `parantheses`). These tokens can then be used by a parser to analyze and interpret the expression.

First of all, I've created a list of tuples that define regular expressions for different types of tokens.
```
TOKEN = [
    ('Identifier', r'[a-zA-Z]\w*'),
    ('Literal', r'\d+'),
    ('Operator', r'[+\-*\/=]'),
    ('Separator', r';'),
    ('Lparen', r'\('),
    ('Rparen', r'\)')
]
```

Then I have the `lexer` function, which takes an input string and produces a list of tokens. The function uses a while loop to iterate over the input string until all characters have been tokenized. In each iteration of the loop, the function tries to match the input string to one of the regular 
expressions in `TOKEN` using Python's `re.match` function. If a match is found, the function appends a tuple to the tokens list. The function then updates the input string to remove the matched token and any leading whitespace.

```
def lexer(input_string):
    tokens = []
    while input_string:
        match = None
        for token_type, regex_pattern in TOKEN:
            regex = re.compile(regex_pattern)
            match = regex.match(input_string)
            if match:
                tokens.append((token_type, match.group(0)))
                input_string = input_string[match.end():].lstrip()
                break
        if not match:
            raise ValueError(f"Invalid input at position {len(input_string)}: {input_string}")
    return tokens
```

## Results
So, for this inputted string:

```x = ( a + b ) * 2;```

I received this output:

```
('Identifier', 'x')
('Operator', '=')
('Lparen', '(')
('Identifier', 'a')
('Operator', '+')
('Identifier', 'b')
('Rparen', ')')
('Operator', '*')
('Literal', '2')
('Separator', ';')
```

## Conclusions
In this laboratory work I learned and implemented the lexer for simple mathematical calculations.
I understood what lexical analysis is and got familiar with the inner workings of a tokenizer.