##Q30.Write a Python program to remove spaces from dictionary keys.
##Original dictionary: {'S 001': ['Math', 'Science'], 'S 002': ['Math',
##'English']}
##New dictionary: {'S001': ['Math', 'Science'], 'S002': ['Math',
##'English']}
dictionary={'S 001': ['Math', 'Science'], 'S 002': ['Math',
'English']}
Product_list = {'P 01' : 'DBMS', 'P 02' : 'OS',
                'P 0 3 ': 'Soft Computing'};
  
# removing spaces from keys
# storing them in sam dictionary
for x, v in Product_list.items():
    Product_list ={x.replace(' ', ''): v}
  
# printing new dictionary
print (" New dictionary : ", Product_list)
