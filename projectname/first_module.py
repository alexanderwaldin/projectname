from __future__ import print_function
from projectname.subpackageone import second_module


def read_model():
    """reads the data in model1"""
    return second_module.read_model()


def main():
    '''Entry point if run as main'''
    print(read_model() + '\n')

if __name__ == '__main__':
    main()
