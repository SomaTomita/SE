import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os


def main():
    print("Hello, docker!")
    print("Python version:", sys.version)
    print("Current working directory:", os.getcwd())

    # NumPy test
    arr = np.array([1, 2, 3, 4, 5])
    print("\nNumPy test array:", arr)
    print("NumPy version:", np.__version__)

    # Pandas test
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    print("\nPandas test DataFrame:")
    print(df)
    print("Pandas version:", pd.__version__)

    print("\nAll tests completed successfully!")


if __name__ == "__main__":
    main()
