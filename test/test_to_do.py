from lib.to_do import *
import pytest

def test_for_empty_string():
    with pytest.raises(Exception) as e:
        to_do("")
    error_message = str(e.value)
    assert error_message == "The task list is empty"

def test_to_do_is_included():
    result = to_do("I have something #TODO")
    assert result == "Yes, you have something #TODO"

def test_to_do_is_not_included():
    result = to_do('I have nothing to do')
    assert result == "No, you have nothing to do"

def test_to_do_in_lower_cases():
    result = to_do("I have something #todo")
    assert result == "No, you have nothing to do"

def test_to_do_mix_lower_and_upper_cases():
    result = to_do("I have something #TodO")
    assert result == "No, you have nothing to do"

def test_to_do_with_none_entrance():
    with pytest.raises(Exception) as e:
        to_do(None)
    error_message = str(e.value)
    assert error_message == "No task list provided"