import io, sys
import pytest
from .c import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """3
1 1 3 2 3 2 2 3 1""",
            """1 3 2""",
        ),
        (
            """1
1 1 1""",
            """1""",
        ),
        (
            """4
2 3 4 3 4 1 3 1 1 4 2 2""",
            """3 4 1 2""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
