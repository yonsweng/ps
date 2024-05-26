import io, sys
import pytest
from .boj_27559 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """2
RR 1
DD 10
100 500
4
1 1
1 1
1 1
2 1""",
            """602
701
602
701
1501""",
        ),
        (
            """4
RDDR 5
DRDR 10
RRDD 7
DDRR 13
7 8 4 12
5
1 2
2 3
4 4
1 1
3 1""",
            """186
186
171
164
166
151""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
