if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom

@custom
def transform_custom(data, *args, **kwargs):
    """
    args: data: The output from the parent block. Is a dataframe.

    """

    # Specify your custom logic here
    print("Datetime of last extraction: "+str(data["max_date"][0]))


