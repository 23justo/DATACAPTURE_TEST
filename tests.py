from DataCapture import DataCapture

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
capture.build_stats()

def test_add() -> None:
    capture.add(10)
    assert 10 in capture.data

def test_between() -> int:
    between_result = capture.between(4,6)
    assert between_result == 2

def test_between_invalid_index() -> str:
    greater_result = capture.between(4,15)
    assert greater_result == "Invalid value"

def test_between_invalid_params() -> str:
    between_result = capture.between(9,4)
    assert between_result == "the firts value passed to the function most be lower than the second one"

def test_greater() -> int:
    greater_result = capture.greater(3)
    assert greater_result == 3

def test_greater_invalid_index() -> str:
    greater_result = capture.greater(15)
    assert greater_result == "Invalid value"

def test_less() -> int:
    greater_result = capture.less(6)
    assert greater_result == 3

def test_less_invalid_index() -> int:
    greater_result = capture.less(15)
    assert greater_result == "Invalid value"


