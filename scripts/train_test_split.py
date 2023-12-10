import random
import pandas as pd

def get_train_test_split(train, val, test, dataset, seed=3):
    '''
    Gets the train, validation, and test split for a given dataset represented as
    a pd dataframe. train + val + test should add up to 100.
    '''
    assert(train+val+test == 100)
    random.seed(seed)
    indices = list(dataset.index)
    random.shuffle(list(dataset.index))
    length = len(indices)
    train_indices = indices[:(length*train)//100]
    val_indices = indices[(length*train)//100: (length*(train+val))//100]
    test_indices = indices[(length*(train+val))//100:]
    return (dataset.loc[train_indices, :], 
            dataset.loc[val_indices, :], 
            dataset.loc[test_indices, :])