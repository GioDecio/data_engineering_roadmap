import pytest
from leet_code.problems import isPalindrome2
from leet_code.problems import removeDuplicatesFromSorted


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
        ([1, 1, 2, 2, 3], (5, [1, 1, 2, 2, 3])),
        ([1, 1, 1, 2, 2, 3], (5, [1, 1, 2, 2, 3])),
        ([1, 2, 2, 2, 2, 3], (4, [1, 2, 2, 3])),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], (7, [0, 0, 1, 1, 2, 3, 3])),
        (
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                2,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
                5,
            ],
            (8, [1, 1, 2, 2, 3, 3, 5, 5]),
        ),
    ],
)
def test_remove_duplicates_from_sorted_array(test, expected):
    assert removeDuplicatesFromSorted(test) == expected
