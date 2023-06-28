#Q8.Write a Python program to check whether a given key already exists in a dictionary.
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key_present(i):
  if i in dict1:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
key_present(5)
key_present(9)
