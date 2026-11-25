#write a program to fill in a letter template given below with name and date.

# Program: Letter template using replace() function
# Author: Pooja😄
# Description: This program replaces placeholders with a name and date

letter='''
dear <|name|>,
you are selected!
<|date|>
'''

# Replacing <|name|> and <|date|> with actual values
print(letter.replace("<|name|>","pooja").replace("<|date|>","18|2|2027"))