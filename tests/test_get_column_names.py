from performance_test_generator.generator import get_column_names


def test_generate_random_df():
    cols = get_column_names(2)
    assert cols == ['date', 'dim1', 'dim2', 'quantity']
