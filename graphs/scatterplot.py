import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[7,6,4,3,8]
plt.title('Scatter plot',color='green')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.scatter(x,y,color='red',marker='+')
plt.show()
