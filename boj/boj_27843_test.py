import io, sys
import pytest
from boj_27843 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """2
2 -3""",
            """2
3""",
        ),
        (
            """3
3 -10 4""",
            """1
6
1""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
