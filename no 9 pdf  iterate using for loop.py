#Q9.Write a Python program to iterate over dictionaries using for loops.
dict1={"name":"jasmi","age":25,"city":"agartala","state":"tripura"}
for key,value in dict1.items():
    print(key,"=",value)
for key in dict1:
    print(key,":",dict1[key])
for key in dict1.keys():
    print(key)
for i in dict1.values():
    print(i)
