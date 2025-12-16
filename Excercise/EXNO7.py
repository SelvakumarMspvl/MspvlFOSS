import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

setosa = iris[iris['species'] == 'setosa']

avg_values = setosa.mean(numeric_only=True)


avg_values.plot(kind='bar', color='skyblue', edgecolor='black',
linewidth=2)

plt.title('Average Feature Values - Iris Setosa')
plt.xlabel('Features')
plt.ylabel('Average Value')
plt.show()