from typing import Tuple
from pandas import DataFrame, Series
import pickle
from sklearn.feature_extraction import DictVectorizer

from mlops.utils.data_preparation.encoders import vectorize_features

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export(data, *args, **kwargs):
    X, y, filename = data
    
    # move file from data/train-val-test to data/archive/train-val-test/*{datetime}.csv
    # save file to disc instead of using global data product
    # save file to data/train-val-test

    return X, y
