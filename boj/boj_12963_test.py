import io, sys
import pytest
from .boj_12963 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """3 2
0 1
1 2""",
            """1""",
        ),
        (
            """4 4
0 1
1 3
0 2
2 3""",
            """10""",
        ),
        (
            """3 1
0 1""",
            """0""",
        ),
        (
            """5 0""",
            """0""",
        ),
        (
            """6 9
1 3
1 2
2 3
0 1
4 5
3 5
0 2
1 4
4 3""",
            """39""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
