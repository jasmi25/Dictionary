#Q13.Write a Python program to sum all the items in a dictionary
def num_sum(dict1):
    sum=0
    for i in dict1:
        sum+=dict1[i]
    #return sum
    print(sum)
a={'a':12,'b':30,'c':90,'d':70}
num_sum(a)
