#Q17.Write a Python program to sort a dictionary by key
def sorted_key(dict1):
    a=sorted(dict1.keys())
    print(a)
    b=list()
    for i in a:
        b.append(dict1[i])
    c=dict(zip(a,b))
    print(c)
dic={'a':89,'b':80,'c':75,'c':99}
sorted_key(dic
           )
