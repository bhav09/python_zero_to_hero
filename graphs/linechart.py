import matplotlib.pyplot as plt
x1=[3,4,5]  #x co ordinates
y1=[1,2,6] # y co ordinates
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line chart") #title
plt.plot(x1,y1,color='red',marker='+',markersize=20) #marker is for choosing marker
x2=[4,5,6]
y2=[6,1,9]
plt.plot(x2,y2,color='black',marker='+',markersize=20)
plt.show()
