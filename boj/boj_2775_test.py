import io, sys
import pytest
from boj_2775 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """2
1
3
2
3""",
            """6
10""",
        )
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
