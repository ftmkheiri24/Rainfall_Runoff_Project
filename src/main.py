import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import calculate_runoff

def load_data(filepath):
    """
    Load rainfall data from a CSV file.
    """
    return pd.read_csv(filepath)

if __name__ == "__main__":
    # Load data
    data = load_data("../data/rainfall_data.csv")

    # Define Curve Number (CN)
    curve_number = 75

    # Calculate runoff
    data['Runoff'] = data['Rainfall'].apply(lambda x: calculate_runoff(x, curve_number))

    # Print the data
    print(data)

    # Plot results
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Rainfall'], label="Rainfall (mm)", marker='o')
    plt.plot(data['Date'], data['Runoff'], label="Runoff (mm)", marker='s')
    plt.xlabel("Date")
    plt.ylabel("Value (mm)")
    plt.title("Rainfall and Runoff")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
