#Q16.Write a Python program to map two lists into a dictionary.
#using zip method
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)
#using list

def map_list(key,values):

dict1={}
for i in range(len(key)):
    dict1[key[i]]=values[i]
print(dict1)

