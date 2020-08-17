car={
    'brand':'Ford',
    'model':'Mustang',
    'year': 1964
    }
print(car) #prints dictionary

#return values 
v=car.values()
print(v)

#return keys
k=car.keys()
print(k)

#adds value into the dictionary
val=car.setdefault('color','white')
print(car)

#adds value with a different syntax
car.update({'Top speed': 300})
print(car)


#copies the dictionary
copy=car.copy()
print("dictionary copied",copy)

#prints a particular value
print(car['year'])

#prints a particular value using get method
x=car.get('year')
print('Get method=',x)

#pops out the entered key
car.pop('color')
print("New dictionary is:",car)

#clears the dictionary
clear=car.clear()
print("Dictionary cleared:",clear)

