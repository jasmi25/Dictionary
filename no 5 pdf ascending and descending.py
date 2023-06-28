#Q5.Write a Python program to sort (ascending and descending) a dictionary by value.
#Original dictionary : {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
#Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
import operator
def ascen_descen(dict1):
    sort_d=sorted(dict1.items(),key=operator.itemgetter(1))
    print(sort_d)
    sort_d=sorted(dict1.items(),key=operator.itemgetter(1),reverse=True)
    print(sort_d)
a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
ascen_descen(a)
