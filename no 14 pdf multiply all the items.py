#Q14.Write a Python program to multiply all the items in a dictionary
def mulofdict(dict1):
    mul=1
    for i in dict1.values():
        mul=mul*i
    print(mul)
a={'a':70,'b':80,'d':30}
mulofdict(a)
#anyone
def mulofdict(dict1):
    mul=1
    for i in dict1:
        mul=mul*dict1[i]
    print(mul)
a={'a':70,'b':80,'d':30}
mulofdict(a)
