import io, sys
import pytest
from boj_13974 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32""",
            """300
864""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
