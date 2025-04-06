import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import unittest
from pathlib import Path


def run_t9pad_tests():
    # Get the absolute path to the test directory
    test_dir = (
        Path(__file__).parent
        / "4. software_testing/testing_strategies/unit_test_activity"
    )

    # Add the test directory to Python's path
    sys.path.append(str(test_dir))

    # Import the test module
    from test_blackbox import TestT9Pad

    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestT9Pad)

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


def main():
    print("Hello, docker!")
    print("Python version:", sys.version)
    print("Current working directory:", os.getcwd())

    # Run T9Pad tests
    print("\nRunning T9Pad tests...")
    success = run_t9pad_tests()
    if success:
        print("All T9Pad tests passed successfully!")
    else:
        print("Some T9Pad tests failed!")

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
