import io, sys
import pytest
from .boj_1012 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5""",
            """5
1""",
        ),
        (
            """1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0""",
            """2""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
