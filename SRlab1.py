import csv
import re
spaces = 0
punct = 0
symb = 0
w/space_symb = 0
w/puncnt_symb = 0
words = 0
predl = 0

with open('steam_description_data.csv', encoding='utf-8') as f:
    a = csv.reader(f)
    for line in a:
        symb += len(line)
        spaces += line.count(' ')
        punct += line.count('.') + line.count('?') + line.count('\"')
        punct += line.count(',') + line.count('\'') + line.count(':') + line.count('(')
        punct += line.count('!') + line.count(';') + line.count('-') + line.count(')')
        words += len(line.split())
        predl += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", line))

w/space_symb = symb - spaces
w/puncnt_symb = symb - punct

print("Cимволов: ", symb)
print ("Символов без пробелов: ", w/space_symb)
print ("Символов без пунктуации: ", w/puncnt_symb)
print ("Всего слов: ", words)
print ("Всего предложений: ", predl)




