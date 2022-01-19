#pytest func.py
import pytest

def func(x):
    return x + 2

def test_ans():
    assert func(4)== 8

def test_ans2():
    assert func(4)== 6

    
