#Q15.Write a Python program to remove a key from a dictionary.
def rem(dict1):
    if 'c' in dict1:
        del dict1['c']
    print(dict1)
a={'a':4,'b':8,'c':6}
rem(a)
