import pytest
from data_structures_and_algorithms.leet_code.problems import *
from params_leet_code import (
    CLOSEST_TO_ZERO_PARAMS,
    STR_STR_PARAMS,
    SUB_SEQ_PARAMS,
    TWO_SUM_PARAMS,
    PALINDROME_PARAMS,
    REMOVE_DUPLICATES_PARAMS,
)


@pytest.mark.parametrize(
    "func",
    [
        closest_to_zeroOnSq,
        closest_to_zeroOnWithGenerator,
        closest_to_zeroOverWriteList,
        closest_to_zeroDupRemoval,
        closest_to_zero,
        closest_to_zeroHashKey,
        closest_to_zeroHashSortedKey,
        closest_to_zeroOneMore,
    ],
)
@pytest.mark.parametrize("ts, expected", CLOSEST_TO_ZERO_PARAMS)
def test_closest_to_zero(benchmark, func, ts, expected):
    assert benchmark(func, ts) == expected


@pytest.mark.parametrize("func", [strStr])
@pytest.mark.parametrize("haystack, needle, exp", STR_STR_PARAMS)
def test_strStr(benchmark, func, haystack, needle, exp):
    assert benchmark(func, haystack, needle) == exp


@pytest.mark.parametrize(
    "func",
    [
        isSubsequence,
        isSubsequenceWhile,
        isSubsequenceRecursion,
        isSubsequenceMemo,
    ],
)
@pytest.mark.parametrize("s, t, exp", SUB_SEQ_PARAMS)
def test_is_sub_sequence(benchmark, func, s, t, exp):
    assert benchmark(func, s, t) == exp


@pytest.mark.parametrize("func", [twoSum, twoSumHash])
@pytest.mark.parametrize("nums, target, expected", TWO_SUM_PARAMS)
def test_two_sums(benchmark, func, nums, target, expected):
    assert benchmark(func, nums, target) == expected


@pytest.mark.parametrize("func", [isPalindrome2])
@pytest.mark.parametrize("test, expected", PALINDROME_PARAMS)
def test_valid_palindrome(benchmark, func, test, expected):
    assert benchmark(func, test) == expected


@pytest.mark.parametrize("func", [removeDuplicatesFromSorted])
@pytest.mark.parametrize("test, expected", REMOVE_DUPLICATES_PARAMS)
def test_remove_duplicates_from_sorted_array(benchmark, func, test, expected):
    assert benchmark(func, test) == expected
