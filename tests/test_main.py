# tests/test_main.py
import sys
sys.path.insert(0, '..')

from main import add

def test_add():
    assert add(1, 2) == 3
