import pytest
from leet_code.problems import *


@pytest.mark.parametrize(
    ("s", "t", "exp"),
    [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("acb", "ahbgdc", False),
        ("aza", "abzba", True),
    ],
)
def test_is_sub_sequence(s, t, exp):
    assert isSubsequence(s, t) == exp
    assert isSubsequenceWhile(s, t) == exp


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ],
)
def test_two_sums(nums, target, expected):
    assert twoSum(nums, target) == expected
    assert twoSumHash(nums, target) == expected


@pytest.mark.parametrize(
    ("test", "expected"),
    [
        ("0P", False),
        (" ", True),
        ("race a car", False),
        ("A man, a plan, a canal: Panama", True),
        ("amorA", False),
        ("aMa", True),
    ],
)
def test_valid_palindrome(test, expected):
    assert isPalindrome2(test) == expected


@pytest.mark.parametrize(
    ("test", "expected"),
    [
        ([1, 1, 1, 1, 1], (2, [1, 1])),
        ([1, 1, 2, 2, 3], (5, [1, 1, 2, 2, 3])),
        ([1, 1, 1, 2, 2, 3], (5, [1, 1, 2, 2, 3])),
        ([1, 2, 2, 2, 2, 3], (4, [1, 2, 2, 3])),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], (7, [0, 0, 1, 1, 2, 3, 3])),
        (
            [
                1,
                1,
                2,
                2,
                2,
                2,
                3,
                3,
                3,
                3,
                3,
                5,
            ],
            (7, [1, 1, 2, 2, 3, 3, 5]),
        ),
    ],
)
def test_remove_duplicates_from_sorted_array(test, expected):
    assert removeDuplicatesFromSorted(test) == expected
