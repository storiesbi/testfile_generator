from performance_test_generator.generator import generate_random_array


def test_generate_random_array():
    arr = generate_random_array(2, 2, 3, 2)
    assert arr.shape == (4, 5)
