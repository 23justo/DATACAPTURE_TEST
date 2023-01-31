from DataCapture import DataCapture

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
capture.add(13)
capture.add(9)
capture.add(43)
capture.add(24)
capture.add(46)
capture.build_stats()

less_value = capture.less(4)
between_value = capture.between(4, 24)
greater_value = capture.greater(13)

print('Full items list')
print(capture.data)
print('Order and cleaned list')
print(capture.sorted_unique_data)
print('dictionary values and indexes')
print(capture.indexed_data)
print("results")
print(less_value)
print(between_value)
print(greater_value)
