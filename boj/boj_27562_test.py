import io, sys
import pytest
from boj_27562 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """2 4
1 5 2
7 9 3
2 9 2 3
1 6 2 8
1 2 4 2
6 9 1 5""",
            """10""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
