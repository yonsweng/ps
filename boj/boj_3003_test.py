import io, sys
import pytest
from boj_3003 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """0 1 2 2 2 7""",
            """1 0 0 0 0 1""",
        ),
        (
            """2 1 2 1 2 1""",
            """-1 0 0 1 0 7""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
