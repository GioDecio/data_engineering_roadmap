import pytest

FIND_NEEDLE_PARAMS = [
    pytest.param("sad", "sadbutsad", True, id="needle_at_start"),
    pytest.param("sad", "butsad", True, id="needle_at_end"),
    pytest.param("sad", "but", False, id="needle_not_present"),
    pytest.param("sad", "sa", False, id="needle_longer_than_haystack"),
    pytest.param("sad", "sad", True, id="exact_match"),
    pytest.param("", "sadbutsad", True, id="empty_needle"),
    pytest.param("aaa", "aaaa", True, id="repeated_chars"),
]
