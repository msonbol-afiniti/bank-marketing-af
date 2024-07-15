from mlops.utils.data_preparation.transform_data import transform_data
from mlops.utils.data_preparation.prepare_data import drop_target


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(data, *args, **kwargs):
    X, y = drop_target(data['data'])

    # transform data 
    X = transform_data(X)

    # save the file
    if data.key == 'training':
        filename = ... # where to save the file
    elif data.key == 'validation':
        filename = ... # where to save the file
    else:
        filename = ... # where to save the file

    return X, y, filename