import io, sys
import pytest
from .a import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """8
beginner""",
            """bbeeggiinnnneerr""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
