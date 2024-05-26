import io
import sys
import pytest
from .boj_1605 import main


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """28
tellmetellmetetetetetetellme""",
            """11""",
        ),
        (
            """5
jykim""",
            """0""",
        ),
        (
            """6
banana""",
            """3""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    main()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
