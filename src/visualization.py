import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

def bubble_chart(df, x, y, size_col, title):
    plt.figure(figsize=(8,6))
    plt.scatter(df[x], df[y], s=df[size_col]*2, alpha=0.5)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.show()
