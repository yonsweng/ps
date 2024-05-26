import io, sys
import pytest
from .boj_27560 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """2
2 4""",
            """RRLRLL""",
        ),
        (
            """3
2 4 4""",
            """RRRLLRRLLL""",
        ),
        (
            """5
3 1 2 6 2""",
            """RLRRRRRLLRLRLL""",
        ),
        (
            """5
1 1 1 1 1""",
            """RRRRR""",
        ),
        (
            """5
2 2 2 2 2""",
            """RRRRRLLLLL""",
        ),
        (
            """1
1""",
            """R""",
        ),
        (
            """1
10""",
            """RLRLRLRLRL""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
