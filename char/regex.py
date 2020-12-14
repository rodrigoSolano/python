import re

texto = """ bar foo bar
foo barbarfoo
foofoo foo bar
"""

patron = re.compile('\bfoo\b')

print(patron.match(texto))