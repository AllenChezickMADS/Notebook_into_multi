'''
This file is used to prompt a user to add noise to the iris dataset
to see how it impacts performance
'''
from load_data import load_file
from testing import split_data
from apply_noise import apply_random_noise,apply_uniform_noise


def do_pipe(dataframe):
    '''
    Input: dataframe
    Action: promps user for information, calls modification function
    Output: noised dataframe
    '''
    get_noise_type = ''
    while get_noise_type not in ['random', 'uniform']:
        get_noise_type = input("Which type of noise do you want?: Random Noise or Uniform Noise ")
    column_range = list(enumerate(dataframe.columns[:-1]))
    columns = input(
        f"Which column numbers to apply noise | example 023 for columns 0,2 & 3: {column_range} ")
    if get_noise_type.lower() == 'random':
        return apply_random_noise(dataframe, columns)
    if get_noise_type.lower() == 'uniform':
        return apply_uniform_noise(dataframe, columns)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    get_df =load_file(file_path=None)
    start_pipe = do_pipe(get_df)
    split_data(start_pipe)