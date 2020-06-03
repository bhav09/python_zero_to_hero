#method overriding
class parent(object):
    def __init__(self):
        self.value=4
    def get_value(self):
        print(self.value)
class child(parent):
    def get_value(self):
        print(self.value +1)

c=child()
c.get_value()

    
