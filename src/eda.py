import pandas as pd # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore

def summarize_data(df: pd.DataFrame):
    print("\n📊 Summary Statistics:")
    print(df.describe())
    print("\n🔍 Missing Values:")
    print(df.isna().sum())

def plot_correlation(df: pd.DataFrame):
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

def plot_time_series(df: pd.DataFrame, column='GHI', time_col='Timestamp'):
    df[time_col] = pd.to_datetime(df[time_col])
    plt.figure(figsize=(12,4))
    plt.plot(df[time_col], df[column], label=column)
    plt.title(f"{column} Over Time")
    plt.xlabel('Time')
    plt.ylabel(column)
    plt.legend()
    plt.show()
