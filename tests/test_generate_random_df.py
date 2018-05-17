from performance_test_generator.generator import generate_random_df


def test_generate_random_df():
    df = generate_random_df(2, 2, 2, 2, save=False)
    assert len(df.index) == 4
    assert len(df.columns) == 3
