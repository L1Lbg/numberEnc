import secrets
import string  

def GenerateNumbers(max):  
  numbers = [1,5]
  num_gen = 1
  # ADD 1,5 AND 10eN NUMBERS TO PREVENT TOO LONG KEYS
  while num_gen < max:
    num_gen = num_gen * 10
    if num_gen < max:
      numbers.append(num_gen)
  # APPEND OTHER RANDOM NUMBERS
  # IF MAX IS BIGGER THAN 10, CREATE A LIST WITH 10 NUMBERS
  if max > 10:
    for i in range(10): 
      rand = secrets.randbelow(max)
      if rand not in numbers and rand != 0:
        numbers.append(rand)
  else:
    raise Exception('Number has to be > 10')
  return numbers

#PICK NUMBER WHILE MAKING SURE THEY ARE DIFFERENT
def PickNumber(numbers,pattern):
  #UPDATE USED_NUMBERS
  used_numbers = []
  if len(list(pattern.items())) != 0:
    for i in range(len(list(pattern.items()))):
      used_numbers.append(list(pattern.items())[i][1])  
  pick = int(numbers[secrets.randbelow(len(numbers))])
  while pick in used_numbers:
    pick = int(numbers[secrets.randbelow(len(numbers))])
  return int(pick)

#CREATE THE DICT THAT ASSOCIATES LETTERS TO NUMBERS
def CreatePattern(numbers):
  alphabet = list(string.ascii_letters)
  pattern = {}
  for i in range(len(numbers)):
    pick = PickNumber(numbers, pattern)
    pattern[alphabet[i]] = pick

  #SORT PATTERN IN KEY VALUE BIG TO SMALL
  pattern = dict(sorted(pattern.items(), key=lambda x :int(x[1]), reverse=True))
  return pattern

def GenerateKey(num, pattern):
  key = str()
  current_num = 0 #WHAT THE KEY BEING GENERATED CURRENTLY IS
  while current_num != num:
    for i in range(len(pattern.items())):
      #REUSE THE BIGGEST POSSIBLE NUMBER IN THE DICT, TO MAKE SURE KEY ISN'T LONG
      while num - current_num >= list(pattern.items())[i][1]:
        key += list(pattern.items())[i][0]
        current_num = current_num + list(pattern.items())[i][1]
  return str(key)
  
def DecryptKey(key, pattern):
  num = 0
  for i in key:
    num += int(pattern[i])
  return num