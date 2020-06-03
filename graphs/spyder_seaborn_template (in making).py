#dependencies
import seaborn as sns
import matplotlib.pyplot as plt

#loading the dataset
iris=sns.load_dataset('iris')

#constructing the plot
sns.swarmplot(x='species',y='petal_length',data=iris)

#for showing the plot
plt.show()