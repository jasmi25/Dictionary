#Q22. Write a Python program to create and display all combinations of letters, selecting each
##letter from a different key in a dictionary. Go to the editor
##Sample data : {'1':['a','b'], '2':['c','d']}
##Expected Output:
##ac
##ad
##bc
##bd
my_dict= {'1':['a', 'b'], '2':['c', 'd']}
my_list= list(my_dict.values())
for i in my_list[0]:
    for j in my_list[1]:
        print(i+j)
# anyone
dic = {'1':['a','b'], '2':['c','d']}   
for x ,y in dic.values():
    print(x,y)
