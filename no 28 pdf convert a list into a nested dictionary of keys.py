##Q28.Write a Python program to convert a list into a nested dictionary of keys.
##num_list = [1, 2, 3, 4]
##Sample output:{1: {2: {3: {4: {}}}}}
def nested(list):
    new_dict = empty = {}
    for name in num_list:
        empty[name] = {}
        empty = empty[name]
    print(new_dict)
num_list = [1, 2, 3, 4]
nested(num_list)
