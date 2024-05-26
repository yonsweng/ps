import io, sys
import pytest
from .boj_4344 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """6
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
1 100""",
            """40.000%
57.143%
33.333%
66.667%
55.556%
0.000%""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
