import numpy as np
from functools import reduce
from multiprocessing import Pool


def test_random():
    mean = 5
    sdev = 3
    sample_size = 1000000

    sample = np.random.normal(mean, sdev, sample_size)

    np.testing.assert_almost_equal(mean, np.mean(sample), decimal=2)
    np.testing.assert_almost_equal(sdev, np.std(sample), decimal=2)


def sum_of_squares(sequence):
    floats = [float(x) for x in sequence if x[0] != '#']
    squares = [i**2 for i in floats]
    return reduce(lambda a, b: a + b, squares)


def squares(val):
    return val**2


def sum_of_squares2(sequence):
    sq = Pool(5).map(squares, sequence)
    return reduce(lambda a, b: a + b, sq)


def sum_of_squares3(sequence):
    sq = [squares(x) for x in sequence]
    return reduce(lambda a, b: a + b, sq)


def test_sum_squares(sample_size):
    #print(sum_of_squares([0]))
    #print(sum_of_squares([1]))
    #print(sum_of_squares([1, 2, 3]))
    #print(sum_of_squares([-1]))
    #print(sum_of_squares([-1, -2, -3]))
    print(sum_of_squares(['1', '2', '3']))
    print(sum_of_squares(['-1', '-2', '-3']))
    print(sum_of_squares(['1', '2', '#100', '3']))


seq = np.random.normal(0, 3, 1000000)
print(sum_of_squares3(seq))
