##Q27.Write a Python program to count the values associated with key in a dictionary.
##student = [{'id': 1, 'success': True, 'name': 'Lary'},
##{'id': 2, 'success': False, 'name': 'Rabi'},
##{'id': 3, 'success': True, 'name': 'Alex'}]
a=[{'id': 1, 'success': True, 'name': 'Lary'},
        {'id': 2, 'success': False, 'name': 'Rabi'}, 
        {'id': 3, 'success': True, 'name': 'Alex'}]
count=0
for i in a:
    if a[i]=='id':
        count+=a[i]
    print(count)
