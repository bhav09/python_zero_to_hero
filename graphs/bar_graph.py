import matplotlib.pyplot as plt
x1=[1,3,5]
y1=[2,4,6]
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.bar(x1,y1,color='green',label="A")      #for horizontal graph write plt.barh()
x2=[4,6,8]
y2=[2,1,4]
plt.bar(x2,y2,color='blue',label="B")
plt.legend()
plt.show()
