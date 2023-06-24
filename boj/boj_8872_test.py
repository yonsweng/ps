import io, sys
import pytest
from boj_8872 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """12 8 2
0 8 4
8 2 2
2 7 4
5 11 3
5 1 7
1 3 1
1 9 5
10 6 3""",
            """18""",
        ),
        (
            """14 11 8
0 8 4
2 12 7
8 2 2
7 4 4
2 7 4
5 11 3
5 1 7
1 3 1
7 13 5
1 9 5
10 6 3""",
            """28""",
        ),
        (
            """1 0 10000""",
            """0""",
        ),
        (
            """2 0 10000""",
            """10000""",
        ),
        (
            """2 1 10000
1 0 1""",
            """1""",
        ),
        (
            """4 2 10000
1 0 1
2 3 2""",
            """10003""",
        ),
        (
            """4 2 10000
1 0 1
0 2 2""",
            """10002""",
        ),
        (
            """6 4 2
0 1 1
1 2 4
2 3 2
5 2 2""",
            """7""",
        ),
        (
            """6 4 2
0 1 1
1 2 4
2 3 2
5 2 2""",
            """7""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
