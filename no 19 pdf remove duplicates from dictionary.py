#Q19.Write a Python program to remove duplicates from Dictionary.
a = {'id1':
{'name': ['Sara'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id2':
{'name': ['David'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id3':
{'name': ['Sara'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id4':
{'name': ['Surya'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
}
def rem(dict1):
    dict={}
    for key,value in dict1.items():
        if value not in dict.values():
            dict[key]=value
    print(dict)
rem(a)
