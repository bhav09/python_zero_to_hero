class rect:
    def getdata(self,l,b):
        self.len=l
        self.br=b
        print('length is:',l)
        print('breadth is:',b)
    def cal(self):
        
        p=2*self.len*self.br
        print('Perimeter is:',p)
x=int(input('Enter length:'))
y=int(input('Enter breadth:'))
r=rect()
r.getdata(x,y)
r.cal()
