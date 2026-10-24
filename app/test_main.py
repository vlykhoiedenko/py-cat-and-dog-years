from app.main import get_human_age


def test_should_return_zeros_when_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_before_first_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_ages_are_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_on_upper_edge_of_second_range() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_ages_are_twenty_four() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_before_third_human_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_cat_becomes_three_while_dog_is_still_two() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_dog_becomes_three_after_five_years_period() -> None:
    assert get_human_age(29, 29) == [3, 3]


def test_cat_becomes_four_while_dog_is_still_three() -> None:
    assert get_human_age(32, 32) == [4, 3]


def test_dog_becomes_four_after_second_five_years_period() -> None:
    assert get_human_age(34, 34) == [4, 4]


def test_should_not_mix_up_cat_and_dog_ages() -> None:
    assert get_human_age(28, 15) == [3, 1]


def test_should_keep_order_when_dog_is_older_than_cat() -> None:
    assert get_human_age(15, 28) == [1, 2]


def test_should_convert_middle_ages() -> None:
    assert get_human_age(50, 50) == [8, 7]


def test_should_convert_big_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
