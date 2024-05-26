import io, sys
import pytest
from .boj_1920 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """5
4 1 5 2 3
5
1 3 7 9 5""",
            """1
1
0
0
1""",
        ),
        (
            """5
4 1 6 2 3
5
1 3 7 9 5""",
            """1
1
0
0
0""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
