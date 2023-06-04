import io, sys
import pytest
from boj_12928 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """4 3""",
            """1""",
        ),
        (
            """4 2""",
            """1""",
        ),
        (
            """3 2""",
            """0""",
        ),
        (
            """5 4""",
            """1""",
        ),
        (
            """50 600""",
            """1""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
