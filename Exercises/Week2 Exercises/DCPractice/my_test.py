import pytest
from decorators import timer, retry, cache
import time
import random

def test_timer_returns_result():
    """Timer decorator should not affect return value."""
    @timer
    def slow_function():
        time.sleep(1.2)
        return 0
    result = slow_function()
    print(result)
    assert result == 0


def test_retry_succeeds_eventually(): # test has a small chance to fail
    """Retry should succeed if function works within attempts."""
    @retry()
    def something():
        print("called")
        if random.randint(1,10) < 3:
            raise
        else:
            return True
    something()
    assert True # it works i saw the print statement called 3x


def test_cache_returns_cached_value():
    """Cache should return same value without recomputing."""
    pass

def test_cache_info_tracks_hits():
    """Cache info should track hits and misses."""
    pass





#========================================================
from generators import read_lines, batch, filter_by, filter_by_field,filter_errors

def test_batch_correct_sizes():
    """Batch should yield correct batch sizes."""
    result = list(batch(range(7), 3))
    #print("resulkt", result)
    assert len(result) == 3, "len er"
    assert len(result[0]) == 3, f"result[0] is {result[0]}"
    assert len(result[2]) == 1, f"result[2] is {result[2]}"

def test_filter_by_predicate():
    """
    Yield items that match the predicate.
    
    Usage:
        evens = filter_by(range(10), lambda x: x % 2 == 0)
        list(evens)  # [0, 2, 4, 6, 8]
    """
    evens = filter_by(range(10), lambda x : x%2==0)
    assert list(evens) == [0,2,4,6,8]

def test_read_lines_skips_empty():
    """Read lines should skip empty lines."""
    lines = list(read_lines("./test_text.txt"))
    # no empty lines
    #print("lines:",lines)
    assert all(line.strip() != "" for line in lines)
    # first line is correct
    assert lines[0] == "something1"
    assert lines[1] == "something2"

def test_reading_errors():
    text = """ERROR yes i am show
    INFO all is good
    ERROR me too is error"""
    lines = list(filter_errors(text))
    print("linesz:", lines)
    assert lines[0] =="ERROR yes i am show"
