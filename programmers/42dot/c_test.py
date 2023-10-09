import pytest
from c import solution


@pytest.mark.parametrize(
    ("parking", "expected"),
    [
        (
            [[1, 2], [3, 4], [-1, -1], [-1, -1], [-1, -1]],
            4,
        ),
        (
            [
                [1, 2],
                [3, 4],
                [5, 6],
                [-1, 7],
                [8, 9],
                [-1, -1],
                [-1, -1],
                [-1, -1],
                [-1, -1],
                [-1, -1],
            ],
            26,
        ),
    ],
)
def test(parking, expected):
    answer = solution(parking)
    assert answer == expected
