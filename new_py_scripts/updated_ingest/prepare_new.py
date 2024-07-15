from mlops.utils.data_preparation.transform_data import transform_data
from mlops.utils.data_preparation.prepare_data import split_data, drop_target


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(data, *args, **kwargs):
    training, validation = split_data(data)

    X_train, y_train, X_val, y_val = drop_target(training), drop_target(validation)

    # transform data 
    X_train, X_val = transform_data(X_train), transform_data(X_val)
    
    return X_train, X_val, y_train, y_val