import io, sys
import pytest
from boj_2667 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """7
0110100
0110101
1110101
0000111
0100000
0111110
0111000""",
            """3
7
8
9""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
