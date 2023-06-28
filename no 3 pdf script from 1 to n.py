#Q3.Write a Python script to generate and print a dictionary that contains a number (between 1
#and n) in the form (x, x*x).
#Sample input ( n = 5) :
#Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.
def num(n):
    i=1
    b=dict()
    while i<=n:
        b[i]=i*i
        i=i+1
    print(b)
a=int(input("enter number"))        
num(a)
