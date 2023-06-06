import io, sys
import pytest
from boj_15337 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """4
1 3
1 3
3 6
3 6""",
            """2 2""",
        ),
        (
            """4
1 2
2 3
1 3
3 4""",
            """3 2""",
        ),
        (
            """10
84 302
275 327
364 538
26 364
29 386
545 955
715 965
404 415
903 942
150 402""",
            """6 5""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
