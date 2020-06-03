import matplotlib.pyplot as plt
x = [3,5,7] #proportions
z = ["sleeep","work","play"] #labels
plt.pie(x,labels=z,radius=1,autopct="%0.2f%%")  #autopct is for formatting the no of decimal values
plt.show()
