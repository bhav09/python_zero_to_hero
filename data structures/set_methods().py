#creating a set
#set dont have duplicates
s={1,2,3}
print(s)

#add() and update()
s.add(4)   #adding a single value
print("after adding single values:",s)

s.update([4,5,6]) #adding multiple values into the set
print("after adding multiple values",s)

#remove() and discard()
 
s.remove(6) #if the entered element isnt there, it would show error
print("after removing",s)

s.discard(5) #if the entered element isnt there if wont show any error
print("after discarding:",s)

#pop() and clear()

s1={10,20,30}
print("Clearing the set:",s1.clear())

s.pop()
print("element is popped:",s)

#operators:union,intersection,difference,symmetric difference

a={1,2,3,4,5,6}
print("Set of natural numbers:",a)
b={2,4,6}
print("Set of even natural numbers:",b)

#union operator '|'
print("Union using operator:",a|b)
#union method()
a.union(b)
print("Union Using method:",a)

#intersection operator '&'
print("Intersection using operator:",a&b)
#intersection method()
a.intersection(b)
print("Intersection using method:",a)

#differnence operator'-'
print("Set difference using operator:",a-b)
#difference method() a-b=a.difference(b)
print("Set difference using method:",a.difference(b))

 
#symmetric difference operator '^'
print("Symmeteric difference using operator:",a^b)
#symmetric difference using method()
print("Symmetric difference using method:",a.symmetric_difference(b))


#isdisjoint()-returns true if two sets have null intersection
#issubset()-returns true if another set contains this set
#issuper()-returns true if this set contains another set
