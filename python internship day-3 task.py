Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python program to map two list into a dictionary
>>> keys=['name','age','job']
>>> values=['SHARON RAJ','22','ENGINEER']
>>> myDict=dict(zip(keys,values))
>>> print(myDict)
{'name': 'SHARON RAJ', 'age': '22', 'job': 'ENGINEER'}
>>> 
>>> #python script to merge two python dictionaries
>>> dict1={"a":10,"b":20}
>>> dict2={"c":50,"d":60}
>>> dict=dict1.copy()
>>> dict.update(dict2)
>>> print(dict)
{'a': 10, 'b': 20, 'c': 50, 'd': 60}
>>> 
>>> #python program to remove a key from a dictionary
>>> dict.pop('a')
10
>>> print(dict)
{'b': 20, 'c': 50, 'd': 60}
>>> 
>>> #python program to find a length of a set
>>> set={'1','2','3','4','5','6'}
>>> print(len(set))
6
>>> 
>>> #python program to remove the intersection of a 2nd set from the 1st set
>>> set1={'1','2','3','4','5','6'}
>>> set2={'7','8','9','1','2','4'}
>>> print(set2.intersection(set1))
{'4', '2', '1'}
>>> 
