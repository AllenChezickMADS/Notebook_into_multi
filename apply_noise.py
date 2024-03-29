'''
This file loads data from different data sources for pipelines
'''
import re
import numpy as np

def get_columns(data,columns):
    '''
    Input:dataframe and list of columns
    Action: creates list of indexes based on user input
    Output: list of indexes
    '''
    col_numbers = list(range(0-len(data)-1,1))
    matches = re.findall(rf'{col_numbers}', columns)
    colsz = [int(i) for i in matches]

    return colsz

def apply_random_noise(data,columns_):
    '''
    Input:dataframe and list of columns
    Action: applies random noise to specific columns
    Output:returns noised dataframe
    '''
    columns = get_columns(data,columns_)
    for index in columns:
        noise = np.random.uniform(low=0, high=1.0, size=data.shape[0])
        data.iloc[:, index] = data.iloc[:, index] + noise
    return data


def apply_uniform_noise(data,columns_):
    '''
    Input: dataframe and list of columns
    Action: applies uniform noise to specific columns
    Output: returns noised dataframe
    '''
    columns = get_columns(data,columns_)
    for index in columns:
        mean = data.iloc[:, index].mean()
        std_dev = data.iloc[:, index].std()
        noise = np.random.normal(mean, std_dev, len(data))
        data.iloc[:, index] =data.iloc[:, index] + noise
    return data
