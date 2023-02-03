from DataCapture import DataCapture

capture = DataCapture()
capture.add(3)
capture.add(3)
capture.add(106)
capture.add(4)
capture.add(16)
capture.add(6)
capture.add(9)
capture.add(110)
capture.build_stats()


def test_data_capture_class_min():
    assert capture.get_min() == 3

def test_data_capture_class_max():
    assert capture.get_max() == 110

def test_data_capture_class_unsorted_data_list_before_build_stats():
    capture_test = DataCapture()
    capture_test.add(3)
    capture_test.add(3)
    capture_test.add(106)
    capture_test.add(4)
    capture_test.add(16)
    capture_test.add(6)
    capture_test.add(9)
    capture_test.add(110)
    assert [3, 3, 106, 4, 16, 6, 9, 110] == capture_test.get_data()

"""Check if after calling build_stats the data gets sorted"""
def test_data_capture_class_sort_data_list():
    assert [3, 3, 4, 6, 9, 16, 106, 110] == capture.get_data()

def test_data_capture_class_less_before_build_stats():
    capture_test = DataCapture()
    less_result = capture_test.less(10)
    assert less_result == "Cant use this function before calling build_stats method"

def test_add():
    capture.add(10)
    assert 10 in capture.get_data()

def test_add_missing_value():
    add_result = capture.add()
    assert add_result == "Please supply a int value to the function in the range (0, 999), it will be skipped"

def test_add_negative_value():
    add_result = capture.add(-10)
    assert add_result == "Value -10 most be a positive integer in the range (0, 999), it will be skipped"

def test_add_wrong_value_type():
    add_result = capture.add('10')
    assert add_result == "Value 10 most be a positive integer in the range (0, 999), it will be skipped"


def test_between():
    between_result = capture.between(4,26)
    """ returns 4 wich are 4,6,9,16"""
    assert between_result == 4

def test_between_index_not_present_on_capture():
    greater_result = capture.between(2,100)
    assert greater_result == 6

def test_between_invalid_params() -> str:
    between_result = capture.between(9,4)
    assert between_result == "the firts value passed to the function most be lower than the second one"

def test_between_missing_values():
    greater_result = capture.between(2,)
    assert greater_result == "Please supply both positive integer values to the function in the range (0, 999)"

def test_between_negative_values():
    between_result = capture.between(9,-4)
    assert between_result == 'Value 9 and -4 most be a positive integer in the range (0, 999)'


def test_greater():
    greater_result = capture.greater(3)
    assert greater_result == 6

def test_greater_index_not_present_on_capture():
    greater_result = capture.greater(15)
    assert greater_result == 3

def test_greater_missing_value():
    greater_result = capture.greater()
    assert greater_result == "Please supply a int value to the function in the range (0, 999), it will be skipped"

def test_greater_negative_value():
    greater_result = capture.greater('4')
    assert greater_result == 'Value 4 most be a positive integer in the range (0, 999), it will be skipped'

def test_greater_value_out_of_range():
    greater_result = capture.greater(1100)
    assert greater_result == 'Value 1100 most be a positive integer in the range (0, 999), it will be skipped'

def test_less():
    greater_result = capture.less(6)
    assert greater_result == 3

def test_less_index_not_present_on_capture():
    less_result = capture.less(15)
    assert less_result == 5

def test_less_missing_value():
    less_result = capture.less()
    assert less_result == "Please supply a int value to the function in the range (0, 999), it will be skipped"

def test_less_negative_value():
    greater_result = capture.less('4')
    assert greater_result == 'Value 4 most be a positive integer in the range (0, 999), it will be skipped'

def test_greater_value_out_of_range():
    less_result = capture.less(1100)
    assert less_result == 'Value 1100 most be a positive integer in the range (0, 999), it will be skipped'