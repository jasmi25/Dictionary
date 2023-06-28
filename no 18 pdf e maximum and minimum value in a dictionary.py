#Q18.Write a Python program to get the maximum and minimum value in a dictionary.
dict={'a':7,'b':9,'c':8,'d':10}
max=max(dict.keys(),key=(lambda a:dict[a]))
min=min(dict.keys(),key=(lambda a:dict[a]))
print('the maximum value in a dictionary',dict[max])
print('the minimum value in a dictionary',dict[min])
