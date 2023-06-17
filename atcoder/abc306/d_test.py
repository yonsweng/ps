import io, sys
import pytest
from .d import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """5
1 100
1 300
0 -200
1 500
1 300""",
            """600""",
        ),
        (
            """4
0 -1
1 -2
0 -3
1 -4""",
            """0""",
        ),
        (
            """15
1 900000000
0 600000000
1 -300000000
0 -700000000
1 200000000
1 300000000
0 -600000000
1 -900000000
1 600000000
1 -100000000
1 -400000000
0 900000000
0 200000000
1 -500000000
1 900000000""",
            """4100000000""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
