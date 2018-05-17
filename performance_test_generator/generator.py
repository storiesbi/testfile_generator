import numpy as np
import pandas as pd


def generate_random_array(cardinality, permutation_count, dim_count,
                          date_count):
    """ Generate numpy array of random integers.

    :param cardinality: {int}
    :param permutation_count: {int}
    :param dim_count: {int}
    :param date_count: {int}
    :return: {np.Array} with size (permutation_count*date_count, dim_count + 2)
    """

    # generate elems
    elems = np.random.randint(0,
                              high=cardinality,
                              size=(permutation_count, dim_count))
    elems = np.tile(elems, (date_count, 1))

    # generate dates
    dates = np.random.randint(0,
                              high=date_count,
                              size=(permutation_count, 1))
    unique_dates = np.arange(date_count)
    dates = np.repeat(unique_dates, permutation_count)
    dates = dates[:, None]  # recast 1d array to more general array type

    # generate measure values
    row_count = permutation_count * date_count
    measure = np.round(np.random.gamma(7.5, size=(row_count, 1)))

    # merge
    dates_elems = np.concatenate((dates, elems), axis=1)
    return np.concatenate((dates_elems, measure), axis=1)


def get_column_names(dim_count):
    """ Create list of dimensons names.

    :param dim_count: {int}
    :return: {list}
    """
    cols = ['date']
    cols += ['dim{}'.format(i) for i in xrange(1, dim_count + 1)]
    cols += ['quantity']
    return cols


def add_date_col(df, date_count):
    """ Add date column to df and set it as index.

    :param df: {pd.DataFrame}
    :param date_count: {int}
    :return: {None}
    """
    dates = pd.date_range('2018-01-01', periods=date_count)
    dates_dict = {i: date for i, date in enumerate(dates)}
    df['date'] = df['date'].map(dates_dict)
    df.set_index('date', inplace=True)
    df.sort_index(inplace=True)


def generate_random_df(cardinality, permutation_count, dim_count, date_count,
                       save=True):
    """ Generate DataFrame with one measure (rounded gamma random. var.), and
    several dimensions with number of elements defined by cardinality param.
    Generate permutation_count rows for every date in date range beginning
    '2018-01-01' with number of dates defined by date_count. Generated
    permutations stay the same for every date (but measure changes).

    :param cardinality: {int} number of elements in every dimension
    :param permutation_count: {int}
    :param dim_count: {int} number of attr. dimensions
    :param date_count: {int} number of unique dates in dataset
    :param save: {bool} save to csv or return as pandas df (for testing)
    :return: {pd.DataFrame}
    """

    print("generating random numbers")
    df_values = generate_random_array(
        cardinality,
        permutation_count,
        dim_count,
        date_count)

    print("add column names")
    cols = get_column_names(dim_count)

    print("creating df")
    df = pd.DataFrame(df_values, columns=cols, dtype=int)

    print("adding date column")
    add_date_col(df, date_count)

    if save:
        print("saving file")
        df.to_csv('perf_test.csv')
        print("file saved!")
    else:
        return df
