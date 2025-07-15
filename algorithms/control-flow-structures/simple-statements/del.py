# del

"""
The del statement removes references to variables, list items, or dict keys.
It unbinds names from scope or deletes parts of containers.
Objects are only destroyed if no references remain.
"""

del_1 = 40
del del_1
print(del_1) # This will raise a NameError because del_1 has been deleted.

del_2 = {'name': 'sam', 'lastname': 'miranda'}
del del_2['lastname']
print(del_2)
