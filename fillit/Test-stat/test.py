import seaborn as sns
sns.set()

x = np.linspace(0, 10, 500)
y = np.random.randn(500)
plt.plot(x,y)
sns.distplot(y, kde=True);
iris = sns.load_dataset("iris")
iris.head()
sns.pairplot(iris, hue='species', size=2.5);
with sns.axes_style('white'):
    sns.jointplot("petal_length", "petal_width", data=iris, kind='reg')
