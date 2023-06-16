import io, sys
import pytest
from boj_27847 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """2 4
0 0 100
50 0 200
0 50 50
1000 1000 0
50 0 200
10 0 170""",
            """2""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
