import pytest

CLOSEST_TO_ZERO_PARAMS = [
    pytest.param([15, 7.1, 9.2, 14.3, -7.1, 12.9], 7.1, id="abs_duplicate_positive_wins"),
    pytest.param([7.2, 2.4, 9.6, -5.7, 0.1, 100], 0.1, id="standard"),
    pytest.param([1, 2, 3], 1, id="all_positive"),
    pytest.param([-1, -2, -3], -1, id="all_negative"),
    pytest.param([-3, 3], 3, id="symmetric_positive_wins"),
    pytest.param([0, 5, -5], 0, id="with_zero"),
    pytest.param([100, -1], -1, id="one_min"),
    pytest.param([7.1, -7.1, 3.0], 3.0, id="symmetric_with_third"),
    pytest.param([7.1, 3.0, -7.1], 3.0, id="symmetric_with_third_reordered"),
    pytest.param([3, 3, 3, 3, 3, 3, 3], 3, id="all_same"),
    pytest.param([-4, -2, 1], 1, id="negatives_and_one_positive"),
    pytest.param([-1, -2], -1, id="two_negatives"),
    pytest.param([1, 3, 1, -1, 3, -3, 5, 4, 1, 1, 1, 1, -1], 1, id="mixed_duplicates"),
]

STR_STR_PARAMS = [
    pytest.param("sadbutsad", "sad", 0, id="needle_at_start"),
    pytest.param("hello", "ll", 2, id="needle_in_middle"),
    pytest.param("mammamia", "mia", 5, id="needle_at_end"),
]

SUB_SEQ_PARAMS = [
    pytest.param("abc", "ahbgdc", True, id="valid_subseq"),
    pytest.param("axc", "ahbgdc", False, id="invalid_subseq"),
    pytest.param("acb", "ahbgdc", False, id="wrong_order"),
    pytest.param("aza", "abzba", True, id="valid_subseq_with_gap"),
]

TWO_SUM_PARAMS = [
    pytest.param([2, 7, 11, 15], 9, [0, 1], id="first_two"),
    pytest.param([3, 2, 4], 6, [1, 2], id="last_two"),
    pytest.param([3, 3], 6, [0, 1], id="duplicates"),
    pytest.param([-1, -2, -3, -4, -5], -8, [2, 4], id="all_negative"),
]

PALINDROME_PARAMS = [
    pytest.param("0P", False, id="alphanumeric_false"),
    pytest.param(" ", True, id="single_space"),
    pytest.param("race a car", False, id="not_palindrome"),
    pytest.param("A man, a plan, a canal: Panama", True, id="classic_palindrome"),
    pytest.param("amorA", False, id="case_sensitive_false"),
    pytest.param("aMa", True, id="case_insensitive_true"),
]

REMOVE_DUPLICATES_PARAMS = [
    pytest.param([1, 1, 1, 1, 1], (2, [1, 1]), id="all_same"),
    pytest.param([1, 1, 2, 2, 3], (5, [1, 1, 2, 2, 3]), id="all_at_most_two"),
    pytest.param([1, 1, 1, 2, 2, 3], (5, [1, 1, 2, 2, 3]), id="one_triple"),
    pytest.param([1, 2, 2, 2, 2, 3], (4, [1, 2, 2, 3]), id="one_quadruple"),
    pytest.param([0, 0, 1, 1, 1, 1, 2, 3, 3], (7, [0, 0, 1, 1, 2, 3, 3]), id="mixed"),
    pytest.param([1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 5], (7, [1, 1, 2, 2, 3, 3, 5]), id="multiple_excess"),
]
