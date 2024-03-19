'''
This file loads iris data and is expandable to load data from different data sources
'''
import pandas as pd
from sklearn.datasets import load_iris

def check_type(input_file):
    '''
    Input: file path
    Action: determines type of file
    Output:  pipeline object
    '''
    match = re.search(r'\.[^.\\/:*?"<>|\r\n]+$', input_file)
    if match:
        file = match.group(0)
        # You can add more file types as needed
        if file == '.csv':
            return '.csv'
        if file in ['.xlsx', '.txt', '.json']:
            return 'Data File'
        elif file  in ['.jpg', '.png', '.gif', '.bmp']:
            return 'Image File'
        elif file  in ['.mp3', '.wav', '.flac']:
            return 'Audio File'
        elif fil in ['.mp4', '.avi', '.mkv']:
            return 'Video File'
        else:
            return 'Other File'
    else:
        return 'No File Type Detected'

    return  

def load_file(file_path=None):
    '''
    Input: 
    Action: Creates pipeline object
    Output:  pipeline object
    '''
    if file_path != None:
        file_type = check_type(file_path)
        if file_type != '.csv':
            print(f'Currently this service only supports .csv file types | Please reformat and try again')
            return None 
        if file_type == 'csv':
            dataframe = pd.read_csv(file_path)
        return dataframe
    else:
        print('Using Iris')
        dataframe = pd.read_csv('/home/labsuser/Notebook_into_multi/iris.csv')
        return  dataframe