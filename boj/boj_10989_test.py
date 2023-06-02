import io, sys
import pytest
from boj_10989 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """10
5
2
3
1
4
2
3
5
1
7""",
            """1
1
2
2
3
3
4
5
5
7""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
