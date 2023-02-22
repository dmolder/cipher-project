import pytest
import caesar

def test_cipher():
    assert caesar.caesar_cipher('a', 1) == 'b'