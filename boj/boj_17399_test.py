import io
import sys

import pytest
from boj_17399 import main


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """4
1 2
1 3
1 4
2
2 3 4
1 2 3""",
            """1
-1""",
        ),
        (
            """2
1 2
2
1 1 2
2 2 2""",
            """-1
2""",
        ),
        (
            """6
1 2
2 3
2 4
3 5
5 6
1
1 4 6""",
            """3""",
        ),
        (
            """9
1 2
2 3
3 4
4 5
3 6
6 7
7 8
8 9
5
1 5 9
3 7 9
6 4 2
5 7 5
5 6 6""",
            """6
-1
3
3
-1""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    main()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
