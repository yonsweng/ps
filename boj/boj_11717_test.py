import io
import sys

import pytest
from boj_11717 import main


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """2 2
..
..""",
            """Second""",
        ),
        (
            """2 2
X.
..""",
            """First""",
        ),
        (
            """4 5
X....
...X.
.....
.....""",
            """First""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    main()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
