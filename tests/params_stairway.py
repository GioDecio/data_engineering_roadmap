import pytest

AT_LEAST_ONE_EVEN_PARAMS = [
    pytest.param([1, 1, 1, 1, 1], False, id="all_odd"),
    pytest.param([2, 3, 4, 5], True, id="even_at_start"),
    pytest.param([1, 3, 5, 7, 9], False, id="all_odd_2"),
    pytest.param([1, 3, 5, 7, 9, 20], True, id="even_at_end"),
    pytest.param([2], True, id="single_even"),
    pytest.param([1], False, id="single_odd"),
    pytest.param([0], True, id="zero_is_even"),
    pytest.param([0, 1, 3], True, id="zero_among_odds"),
    pytest.param([-2, 1, 3], True, id="negative_even"),
    pytest.param([-1, -3, -5], False, id="all_negative_odds"),
    pytest.param([-4, -3], True, id="negative_even_first"),
    pytest.param([1, 3, 5, 2], True, id="even_at_end_2"),
    pytest.param([100, 201, 303], True, id="large_even"),
    pytest.param([101, 201, 303], False, id="all_large_odds"),
    pytest.param([2, 4, 6, 8], True, id="all_even"),
    pytest.param([1, 2], True, id="even_in_two_element"),
    pytest.param([1000000, 3], True, id="large_even_number"),
    pytest.param([999999, 3], False, id="large_odd_number"),
    pytest.param([-2], True, id="single_negative_even"),
    pytest.param([-1], False, id="single_negative_odd"),
    pytest.param([1, 3, 5, 7, 9, 11, 13, 4], True, id="even_at_end_of_long_list"),
    pytest.param([1, 3, 5, 7, 9, 11, 13, 15], False, id="long_list_all_odd"),
    pytest.param([0, 0, 0], True, id="all_zeros"),
    pytest.param([-6, -3, -1], True, id="negative_even_first_2"),
    pytest.param([2, 2, 2], True, id="all_same_even"),
    pytest.param([3, 3, 3], False, id="all_same_odd"),
]

COMMOM_ELEMENT_PARAM = [
    pytest.param([1, 2, 3], [4, 5, 6], False, id="no_common"),
    pytest.param([1, 2, 3], [3, 4, 5], True, id="common_at_end"),
    pytest.param([1, 2, 3], [1, 4, 5], True, id="common_at_start"),
    pytest.param([1], [1], True, id="single_match"),
    pytest.param([1], [2], False, id="single_no_match"),
    pytest.param([], [1, 2, 3], False, id="first_empty"),
    pytest.param([1, 2, 3], [], False, id="second_empty"),
    pytest.param([], [], False, id="both_empty"),
    pytest.param([1, 2, 3], [4, 5, 1], True, id="common_at_end_of_second"),
    pytest.param(["a", "b"], ["c", "b"], True, id="strings_match"),
    pytest.param(["a", "b"], ["c", "d"], False, id="strings_no_match"),
    pytest.param([1, 2, 3], [1, 2, 3], True, id="identical_lists"),
    pytest.param([1, 2], [3, 4, 5, 6, 7, 2], True, id="common_in_long_second"),
    pytest.param([None], [None, 1], True, id="none_match"),
    pytest.param([None], [1, 2], False, id="none_no_match"),
]

COMMOM_ELEMENT_LARGE_PARAMS = [
    pytest.param(
        list(range(0, 10000)), list(range(10000, 20000)), False, id="large_no_match"
    ),
    pytest.param(
        list(range(0, 10000)), list(range(0, 20000)), True, id="large_match_start"
    ),
    pytest.param(
        list(range(0, 10000)), list(range(9999, 20000)), True, id="large_match_end"
    ),
]

CHAR_OCCURENCE_PARAMS = [
    pytest.param("hello", "l", 2, id="hello_l"),
    pytest.param("hello", "h", 1, id="hello_h"),
    pytest.param("hello", "z", 0, id="hello_z_missing"),
    pytest.param("", "a", 0, id="empty_string"),
    pytest.param("aaa", "a", 3, id="all_same_char"),
    pytest.param("aaa", "b", 0, id="all_same_char_missing"),
    pytest.param("banana", "a", 3, id="banana_a"),
    pytest.param("banana", "n", 2, id="banana_n"),
    pytest.param("abcabc", "c", 2, id="abcabc_c"),
    pytest.param("mississippi", "s", 4, id="mississippi_s"),
    pytest.param("mississippi", "i", 4, id="mississippi_i"),
    pytest.param("mississippi", "p", 2, id="mississippi_p"),
    pytest.param("a", "a", 1, id="single_char_match"),
    pytest.param("a", "b", 0, id="single_char_no_match"),
    pytest.param("  spaces  ", " ", 4, id="spaces"),
    pytest.param("Hello", "h", 0, id="case_sensitive_lower"),
    pytest.param("Hello", "H", 1, id="case_sensitive_upper"),
]


from data_structures_and_algorithms.stairway_to_heaven.problems._4_binary_search import (
    ListNotSortedError,
)

BS_PARAMS = [
    pytest.param([1, 3, 5, 7, 9], 5, 5, id="found_middle"),
    pytest.param([1, 3, 5, 7, 9], 1, 1, id="found_start"),
    pytest.param([1, 3, 5, 7, 9], 9, 9, id="found_end"),
    pytest.param([1, 3, 5, 7, 9], 4, None, id="not_present"),
    pytest.param([42], 42, 42, id="single_match"),
    pytest.param([], 9, None, id="empty_list_value"),
    pytest.param([], None, None, id="empty_list_no_value"),
    pytest.param([42], 1, None, id="single_no_match"),
    pytest.param(
        [3, 4, 1],
        None,
        None,
        id="not_sorted_small",
        marks=pytest.mark.xfail(raises=ListNotSortedError),
    ),
    pytest.param(list(range(0, 1000, 2)), 500, 500, id="large_found"),
    pytest.param(list(range(0, 1000, 2)), 501, None, id="large_not_found"),
]


EX6_PARAMS = [
    pytest.param("mia", "mammamia", True, id="standard_true"),
    pytest.param("cacao", "coccobello", False, id="standard_false"),
]


EX7_PARAMS = [
    pytest.param(list("hello"), "olleh"),
    pytest.param(list("Hannah"), "hannaH"),
    pytest.param(list("mamma"), "ammam"),
    pytest.param(list("pisa"), "asip"),
    pytest.param(list("super"), "repus"),
    pytest.param(
        list("supercalifragilistichespiralidoso"), "osodilaripsehcitsiligarfilacrepus"
    ),
    pytest.param(list("platone"), "enotalp"),
]


EX8_PARAMS = [
    pytest.param(1234, 4321),
    pytest.param(123456789, 987654321),
    pytest.param(3450, 543),
    pytest.param(-12, -21, id="negative value"),
]
