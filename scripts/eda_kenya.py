

# ✅ Step 1: Import necessary modules
import os
import pandas as pd # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
from src.data_loader import load_data
from src.cleaning import clean_data
from src.eda import summarize_data, plot_correlation, plot_time_series
from src.visualization import bubble_chart

# ✅ Step 2: Define main function
def main():
    print("🔆 Starting EDA for Kenya Solar Dataset...")

    # Step 3: Load dataset
    data_path = os.path.join("data", "kenya_solar.csv")
    df = load_data(data_path)
    print(f"✅ Data loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")

    # Step 4: Clean data
    df = clean_data(df)
    print("✅ Data cleaning completed.")

    # Step 5: Summary statistics and missing value report
    summarize_data(df)

    # Step 6: Correlation heatmap
    plot_correlation(df)

    # Step 7: Time series plots
    plot_time_series(df, column="GHI", time_col="Timestamp")
    plot_time_series(df, column="Tamb", time_col="Timestamp")

    # Step 8: Bubble chart visualization
    bubble_chart(df, x="Tamb", y="GHI", size_col="RH", title="Kenya: GHI vs Tamb (Bubble = RH)")

    # Step 9: Distribution plots
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    sns.histplot(df["GHI"], bins=30, kde=True)
    plt.title("Distribution of GHI")

    plt.subplot(1,2,2)
    sns.histplot(df["WS"], bins=30, kde=True)
    plt.title("Distribution of Wind Speed (WS)")
    plt.tight_layout()
    plt.show()

    # Step 10: Save cleaned data (but don’t commit to Git)
    cleaned_path = os.path.join("data", "kenya_clean.csv")
    df.to_csv(cleaned_path, index=False)
    print(f"💾 Cleaned dataset saved at: {cleaned_path}")

    print("🎯 Kenya EDA completed successfully!")

# ✅ Run script
if __name__ == "__main__":
    main()
