import sys


def test_always_pass():
    """Always pass"""
    assert True

def test_always_pass_six_times():
    if sys.version_info.minor == 9:
        assert True
        assert True
        assert True
        assert True
        assert True
        assert True

def test_one_equals_one():
    assert 1 == 1
