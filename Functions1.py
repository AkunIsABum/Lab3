from itertools import permutations

def grams2ounces(grams):
  return grams * 28.3495231

def Fahr2Cels(F):
  print((5 / 9) * (F – 32))

def puzzle(heads, legs):
  rabbits = (legs - 2 * heads) / 2
  chickens = heads - rabbits
  if rabbits >= 0 and chickens >= 0 and rabbits == int(rabbits) and chickens == int(chickens):
    return int(chickens), int(rabbits) 
  else:
    return "No solution"

#TASK 4 Is a copy of the task 6 from Classes.

def strpermutations(str):
    perm_list = permutations(str)

    for perm in perm_list:
        print(''.join(perm))

input5 = input("Enter a string: ")
strpermutations(input5)

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

input6 = input("Enter a sentence: ")

result = reverse_words(input6)

print("Reversed sentence:", result)


def has_33(nums):
  buf = False
  for x in nums:
    if x == 3 and buf == False:
      buf = True
      continue
    if x == 3 and buf == True:
      return True
    buf = False
  return False

def spy_game(nums):
  buf1 = False
  buf2 = False
  for x in nums:
    if x == 0 and buf1 == False:
      buf1 = True
      continue
    if x == 0 and buf1 == True:
      buf2 = True
      continue
    if x == 7 and buf2 == True:
      return True
    if x == 7 and buf2 == False:
      buf1 = False
      continue
  return False

def sphereArea(rad):
  return 4*rad*rad*3.1415

def unique_elements(input_list):
    unique_list = []

    for i in input_list:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


def histogram(list):
  for x in list:
    print('*' * x)
