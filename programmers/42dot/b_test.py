import pytest
from b import solution


@pytest.mark.parametrize(
    ("friends", "user_id", "expected"),
    [
        (
            [
                ["david", "frank"],
                ["demi", "david"],
                ["frank", "james"],
                ["demi", "james"],
                ["claire", "frank"],
            ],
            "david",
            ["james"],
        ),
        (
            [["david", "demi"], ["frank", "demi"], ["demi", "james"]],
            "frank",
            ["david", "james"],
        ),
    ],
)
def test(friends, user_id, expected):
    answer = solution(friends, user_id)
    assert answer == expected
