import pickle
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_model():
    """reads the data in model1"""
    f_path = os.path.join(__location__, 'models', 'model1.pickle')
    file_handle = open(f_path)
    data = pickle.load(file_handle)
    return data
