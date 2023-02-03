from DataCapture import DataCapture

capture = DataCapture()
capture.add(3)
capture.add(3)
capture.add(4)
capture.add(6)
capture.add(9)
capture.add(9)
capture.add(13)
capture.add(13)
capture.add(24)
capture.add(43)
capture.add(46)

capture.build_stats()
less_value = capture.less(30)
between_value = capture.between(6, 43)
greater_value = capture.greater(113)


print(less_value)
print(between_value)
print(greater_value)
