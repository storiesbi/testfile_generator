import pandas as pd

from performance_test_generator.generator import add_date_col


def test_generate_random_df():
    df = pd.DataFrame({
        'date': [0, 2, 1],
        'dim1': [0, 1, 2],
        'quantity': [0, 1, 2]
    })
    add_date_col(df, 3)
    assert (df.index == pd.date_range('2018-01-01', periods=3)).all()
