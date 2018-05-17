# Perfomance test file generator

Generate random CSV file for performance testing. Example: https://s3.eu-central-1.amazonaws.com/public.stories.bi/perf_test.csv

## parameters
- *DIM_COUNT*: Number of attribute dimensions.
- *CARDINALITY*: Number of unique elements in every dimension.
- *PERMUTATIONS_COUNT*: Number of random combinations of elements for every 
date.
- *DATE_COUNT*: Number of dates (consecutive dates starting 2018-01-01).


## setup
1. Create new python 2.7 virtualenv
2. `pip install -r requirements/requirements.txt`.

## how to run
1. `python main.py`
2. Result will be saved in `perf_test.csv`.

## setup for development
1. `pip install -r requirements/testing.txt`.
2. `py.test` in the root folder of repo.
