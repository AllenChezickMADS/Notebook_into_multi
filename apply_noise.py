import numpy as np
import pandas as pd  # Ensure pandas is imported

print(f'')


def apply_noiseX(df,columns):
    # Add random noise to sepal_width and petal_width only
    noise_sepal_width = np.random.uniform(low=0, high=1.0, size=X.shape[0])
    noise_petal_width = np.random.uniform(low=0, high=1.0, size=X.shape[0])
    for column in columns:
        X.loc[:, column] = X[column] + noise_sepal_width
    X.loc[:, 'petal_width'] = X['petal_width'] + noise_petal_width
    return noised_df


def apply_noiseY(df,columns):
    # Add random noise to sepal_width and petal_width only
    noise_sepal_width = np.random.uniform(low=0, high=1.0, size=X.shape[0])
    noise_petal_width = np.random.uniform(low=0, high=1.0, size=X.shape[0])

    X.loc[:, 'sepal_width'] = X['sepal_width'] + noise_sepal_width
    X.loc[:, 'petal_width'] = X['petal_width'] + noise_petal_width
    return noised_df