import pytest
from data_structures_and_algorithms.book import *
from params_book import FIND_NEEDLE_PARAMS


@pytest.mark.parametrize("func", [find_needle])
@pytest.mark.parametrize("needle, haystack, expected", FIND_NEEDLE_PARAMS)
def test_find_needle(benchmark, func, needle, haystack, expected):
    assert benchmark(func, needle, haystack) == expected
