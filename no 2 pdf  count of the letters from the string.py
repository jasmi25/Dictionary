#Q2. Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string : 'w3resource'
#Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
def str_word(dict):
    counter={}
    for letter in dict:
        if letter not in counter:
            counter[letter]=0
        counter[letter]+=1
    print(counter)
str_word('w3resource')
