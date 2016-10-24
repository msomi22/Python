

 
try:
  vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5:'u'}
  del(vowels[10])
except ValueError:
  print("Oops!  That was no valid number.  Try again...")

