import io, sys
import pytest
from .boj_13896 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """3
5 5 1
1 5
3 4
3 5
2 1
1 1
1 2
0 5
1 5
1 3
1 5 1
1 1
1 1
0 1
1 1
1 1
13 5 1
1 2
1 3
1 4
2 5
2 6
3 7
3 8
3 9
5 10
6 11
6 12
8 13
1 3
0 8
1 6
0 11
1 1""",
            """Case #1:
5
1
5
2
Case #2:
1
1
1
1
Case #3:
5
3
7""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
