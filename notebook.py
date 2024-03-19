'''
This file is used to prompt a user to add noise to the iris dataset
to see how it impacts performance
'''
from load_data import load_file
import numpy as np
import pandas as pd
from testing import split_data
from apply_noise import apply_random_noise,apply_uniform_noise


def do_pipe(dataframe):
    get_noise_type = input("Which type of noise do you want?: Random Noise or Uniform Noise ")
    columns = input(
        f"Which column numbers to apply the noise: {list(enumerate(dataframe.columns[:4]))}")
    if get_noise_type.lower() == 'random':
        return apply_random_noise(dataframe, columns)
    elif get_noise_type.lower() == 'uniform':
        return apply_uniform_noise(dataframe, columns)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    get_df =load_file(file_path=None)
    start_pipe = do_pipe(get_df)
    do_split = split_data(start_pipe) 
    