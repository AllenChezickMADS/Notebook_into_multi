from load_data import load_file
import numpy as np
import pandas as pd  # Ensure pandas is imported
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from apply_noise import apply_noiseX,apply_noiseY


def do_pipe(df):
    # get_nose_type = #print(what type of noise do you want? : )
    columns = #Which columns do you want to apply it to
    if noise_type == 'X':
        return apply_noiseX()
    elif noise_type == 'Y':
        return apply_noiseY()
    return None 




if __name__ == "__main__":
    print('hello world')
    import argparse

    parser = argparse.ArgumentParser()
    get_df =load_file(file_path=None)
    start_pipe = do_pipe(get_df)
    print(get_df)