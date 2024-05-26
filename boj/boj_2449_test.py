import pytest
from .boj_2449 import solution


@pytest.mark.parametrize(
    "n, k, lights, expected",
    [
        (10, 3, [1, 1, 2, 3, 3, 3, 2, 2, 1, 1], 2),
        (10, 4, [1, 2, 3, 1, 2, 2, 3, 1, 4, 2], 6),
    ]
)
def test_solution(n, k, lights, expected):
    assert solution(n, k, lights) == expected
