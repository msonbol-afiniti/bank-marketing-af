from mlops.utils.data_preparation.prepare_data import split_data


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer


@transformer
def transform(data, *args, **kwargs):
    # dynamic block
    training, validation = split_data(data['data'])
    
    return {'training': training}, {'validation': validation}