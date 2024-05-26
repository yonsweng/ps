import io, sys
import pytest
from .boj_27558 import solve


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (
            """17
abc
abc
BBC
ABC
abc
bbc
ABCD
BACD
aBcDeFaCcDF
CCcACFCAcAF
CAB
ABC
ABCD
BADC
ABCD
BABA
ABCD
BABC
ABCD
BDBC
qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM
wertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMq
qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMa
qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMa
qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNN
qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM
abcd
caac
abcde
bcaec
abcde
ccdec
qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM
wertyuiopasdfghjklzxcvbnmqQWERTYUIOPASDFGHJKLZXCVBNM""",
            """0
-1
1
3
5
4
6
4
4
4
-1
0
-1
4
5
5
-1""",
        ),
    ],
)
def test(input, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys.stdin, "readline", io.StringIO(input).readline)
    solve()
    out, _ = capsys.readouterr()
    assert out.rstrip() == expected
