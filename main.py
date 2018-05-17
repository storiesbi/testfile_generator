from performance_test_generator.generator import generate_random_df


DIM_COUNT = 10
CARDINALITY = 100
PERMUTATIONS_COUNT = int(1e6)
DATE_COUNT = 20


generate_random_df(CARDINALITY, PERMUTATIONS_COUNT, DIM_COUNT, DATE_COUNT)
