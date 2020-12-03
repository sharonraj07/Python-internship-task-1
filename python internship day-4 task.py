Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #write a program to create a list of n integer values and do the following
>>> L1=['2','3','4','5','6']
>>> # a) add an item into the list (using function)
>>> L1.append('7')
>>> print(L1)
['2', '3', '4', '5', '6', '7']
>>> # b) delete(using functin)
>>> L1.remove('3')
>>> print(L1)
['2', '4', '5', '6', '7']
>>> # c) store the largest number from the list to a variable
>>> print(max(L1))
7
>>> # d) store the smallest number from the list to a variable
>>> print(min(L1))
2
>>> #create a tuple and point the reverse of the created tuple
>>> tuple = ('1','2','3','home','3.14')
>>> reversedtuples = tuple[::-1]
>>> print(reversedtuples)
('3.14', 'home', '3', '2', '1')
>>> #create a tuple and convert tuple into list
>>> tuple = ('45','56','67','3.45','home')
>>> list = list(tuple)
>>> print(type(list))
<class 'list'>
>>> print(list)
['45', '56', '67', '3.45', 'home']
>>> 
