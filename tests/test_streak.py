import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_all_positive_numbers():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak_with_zeros():
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_single_streak_with_negatives():
    assert longest_positive_streak([1, 2, -1, 3, 4, 5]) == 3

def test_multiple_streaks():
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 0, 1]) == 3

def test_streaks_at_beginning_and_end():
    assert longest_positive_streak([1, 2, 3, 0, -5, 4, 5]) == 3

def test_another_multiple_streaks():
    assert longest_positive_streak([0, 1, 2, 0, 1, 2, 3, 4, 0, 1, 2]) == 4

def test_list_with_single_zero():
    assert longest_positive_streak([0]) == 0

def test_list_with_single_positive():
    assert longest_positive_streak([5]) == 1

def test_list_with_single_negative():
    assert longest_positive_streak([-5]) == 0

def test_mixed_numbers():
    assert longest_positive_streak([1, -2, 3, 4, 0, 5, 6, 7, -8, 9]) == 3