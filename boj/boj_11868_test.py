import io
import sys

import pytest
from .boj_11868 import main


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """1
1""",
            """koosaga""",
        ),
        (
            """1
2""",
            """koosaga""",
        ),
        (
            """2
1 1""",
            """cubelover""",
        ),
        (
            """2
1 2""",
            """koosaga""",
        ),
        (
            """2
2 2""",
            """cubelover""",
        ),
        (
            """4
1 2 3 4""",
            """koosaga""",
        ),
        (
            """6
9 8 9 8 9 9""",
            """cubelover""",
        ),
        (
            """3
2 4 6""",
            """cubelover""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    main()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
