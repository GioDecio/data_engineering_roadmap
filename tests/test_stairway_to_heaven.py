import unittest
import pytest
from data_structures_and_algorithms.stairway_to_heaven import *
import params_stairway as par


@pytest.mark.parametrize(
    "func",
    [
        at_least_one_even,
    ],
)
@pytest.mark.parametrize("nums, expected", par.AT_LEAST_ONE_EVEN_PARAMS)
def test_at_least_one_even(benchmark, func, nums, expected):
    assert benchmark(func, nums) == expected


@pytest.mark.parametrize(
    "func",
    [
        count_char_occurrence,
    ],
)
@pytest.mark.parametrize("_string, char, expected", par.CHAR_OCCURENCE_PARAMS)
def test_count_char_occurrence(benchmark, func, _string, char, expected):
    assert benchmark(func, _string, char) == expected


@pytest.mark.parametrize(
    "func",
    [common_element, common_elementSet, common_elementSetBug],
)
@pytest.mark.parametrize("l_1, l_2, exp", par.COMMOM_ELEMENT_PARAM)
def test_common_element(benchmark, func, l_1, l_2, exp):
    assert benchmark(func, l_1, l_2) == exp


@pytest.mark.parametrize(
    "func",
    [common_element, common_elementSet, common_elementSetBug],
)
@pytest.mark.parametrize("l_1, l_2, exp", par.COMMOM_ELEMENT_LARGE_PARAMS)
def test_common_element_large(benchmark, func, l_1, l_2, exp):
    assert benchmark(func, l_1, l_2) == exp


@pytest.mark.parametrize(
    "func",
    [binary_search, binary_search_2, binary_search_with_order_check],
)
@pytest.mark.parametrize("search_list, value, exp", par.BS_PARAMS)
def test_bs(benchmark, func, search_list, value, exp):
    assert benchmark(func, search_list, value) == exp


@pytest.mark.parametrize(
    "func",
    [binary_search_with_order_check],
)
@pytest.mark.parametrize("search_list, value, exp", par.BS_PARAMS)
def test_bs_order_check(benchmark, func, search_list, value, exp):
    assert benchmark(func, search_list, value) == exp


def test_bs_order_check_raises():
    with pytest.raises(ListNotSortedError):
        binary_search_with_order_check([3, 1, 2], 1)


# --- exercise 5
def test_closest_to_zero():
    assert EX5().closest_to_zero([-1, 1, 2, 3]) == 1


# --- exercise 6
@pytest.mark.parametrize("method_name", ["needle_in_haystack"])
@pytest.mark.parametrize("needle, haystack, exp", par.EX6_PARAMS)
def test_needle_in_haystack(method_name, needle, haystack, exp):
    ex = EX6(needle, haystack)
    assert getattr(ex, method_name)() == exp


# --- exercise 7
@pytest.mark.parametrize(
    "method_name", ["reverse_string_with_for", "reverse_string_with_while"]
)
@pytest.mark.parametrize("s, exp", par.EX7_PARAMS)
def test_reverse_string(method_name, s, exp):
    ex = Ex7()
    assert getattr(ex, method_name)(s.copy()) == exp


# --- exercise 8
ex8 = Ex8()


@pytest.mark.parametrize(
    "method_name",
    ["reverse_integer_by_digit_extraction", "reverse_integer_by_shifting"],
)
@pytest.mark.parametrize("n, exp", par.EX8_PARAMS)
def test_reverse_integer(method_name, n, exp):
    assert getattr(ex8, method_name)(n) == exp


class TestReverseInteger(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(ex8.reverse_integer_by_shifting(123), 321)

    def test_positive_no_assertEqual_method(self):
        assert ex8.reverse_integer_by_shifting(123) == 321
