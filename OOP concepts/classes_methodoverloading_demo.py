#method overloading
class mul:
    def two(self,a,b):
        p=a*b
        print('Product of',a,b,end=':')
        print(p)
    def two(self,a,b,c):            
        p=a*b*c
        print('Product of',a,b,c,end=':')
        print(p)
m=mul()
m.two(2,3,4)

#overloading is not possible in python bcz the function gets over written. And thus shows errror 
