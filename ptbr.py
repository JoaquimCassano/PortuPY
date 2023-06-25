import re
import sys
codename = sys.argv[1]


patterns = {
    "se ":"if ",
    "definir":"def",
    "retorne":"return",
    'verdade':"True",
    "falso":"False",
    "imprima":"print",
    "caso contrário":"else",
    "pergunte":"input",
    "inteiro":"int",
    "enquanto":"while",
    "para cada":'for',
    " em ":" in ",
    " de ":' from ',
    'importe':"import",
    "ou então":"elif",
    "nulo":"None",
    "texto":"string",
    "tente":"try",
    "erro":"except"    
}

with open(codename, 'r+', encoding='Utf-8', errors='strict') as code:
    texto = code.read()
    new_code = re.sub("|".join(patterns.keys()), lambda x: patterns[x.group()], texto)
    exec(new_code)