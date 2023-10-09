import pytest
from a import solution


@pytest.mark.parametrize(
    ("card", "word", "expected"),
    [
        (
            ["ABACDEFG", "NOPQRSTU", "HIJKLKMM"],
            ["GPQM", "GPMZ", "EFU", "MMNA"],
            ["GPQM", "MMNA"],
        ),
        (
            ["AABBCCDD", "KKKKJJJJ", "MOMOMOMO"],
            ["AAAKKKKKMMMMM", "ABCDKJ"],
            ["-1"],
        ),
        (
            ["AABBCCDD", "KKKK", "JOMOMOMO"],
            ["AAKKMMOOOO", "ABCDKJ"],
            ["AAKKMMOOOO", "ABCDKJ"],
        ),
    ],
)
def test(card, word, expected):
    answer = solution(card, word)
    assert answer == expected
