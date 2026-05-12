import pytest
from data_structures_and_algorithms.stairway_to_heaven import *
from params_stairway import (
    AT_LEAST_ONE_EVEN_PARAMS,
    CHAR_OCCURENCE_PARAMS,
    COMMOM_ELEMENT_PARAM,
    COMMOM_ELEMENT_LARGE_PARAMS,
    BS_PARAMS,
)


@pytest.mark.parametrize(
    "func",
    [
        at_least_one_even,
    ],
)
@pytest.mark.parametrize("nums, expected", AT_LEAST_ONE_EVEN_PARAMS)
def test_at_least_one_even(benchmark, func, nums, expected):
    assert benchmark(func, nums) == expected


@pytest.mark.parametrize(
    "func",
    [
        count_char_occurrence,
    ],
)
@pytest.mark.parametrize("_string, char, expected", CHAR_OCCURENCE_PARAMS)
def test_count_char_occurrence(benchmark, func, _string, char, expected):
    assert benchmark(func, _string, char) == expected


@pytest.mark.parametrize(
    "func",
    [common_element, common_elementSet, common_elementSetBug],
)
@pytest.mark.parametrize("l_1, l_2, exp", COMMOM_ELEMENT_PARAM)
def test_common_element(benchmark, func, l_1, l_2, exp):
    assert benchmark(func, l_1, l_2) == exp


@pytest.mark.parametrize(
    "func",
    [common_element, common_elementSet, common_elementSetBug],
)
@pytest.mark.parametrize("l_1, l_2, exp", COMMOM_ELEMENT_LARGE_PARAMS)
def test_common_element_large(benchmark, func, l_1, l_2, exp):
    assert benchmark(func, l_1, l_2) == exp


@pytest.mark.parametrize(
    "func",
    [binary_search],
)
@pytest.mark.parametrize("search_list, value, exp", BS_PARAMS)
def test_bs(benchmark, func, search_list, value, exp):
    assert benchmark(func, search_list, value) == exp
