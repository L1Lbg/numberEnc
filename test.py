from main import *
import pprint
#TEST THE PROGRAM
to_encrypt = int(input('Input number to encrypt: \n'))

#GENERATE A LIST OF RANDOM NUMBERS WITH A MAX VALUE (RECOMMENDED 2 TIMES SMALLER THAN THE ENCRIPTED NUM)
numbers = GenerateNumbers(int(to_encrypt / 2))
print('Generated numbers :')
print(numbers)

#ASSOCIATE NUMBERS TO RANDOM LETTERS AND CREATE PATTERN
pattern = CreatePattern(numbers)
print('Generated pattern :')
pprint.pprint(pattern, sort_dicts=False)

#GENERATE KEY THAT EQUALS TO WANTED NUM WITH PATTERN
key = GenerateKey(to_encrypt, pattern)
print(f'Generated key : \n {key}')

#DECRYPT KEY WITH PATTERN
num = DecryptKey(key, pattern)
print(f'Decrypted num : \n {num}')
