import io, sys
import pytest
from .boj_11659 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """5 3
5 4 3 2 1
1 3
2 4
5 5""",
            """12
9
1""",
        ),
        (
            """7 4
1 2 3 4 5 6 7
5 7
2 5
3 6
1 7""",
            """18
14
18
28""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
