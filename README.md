# Data capture challenge

Clone the repository and run this commands to execute the main code or tests

## Program structure explanation
DataCapture.py file
In this file you can check the class which is being used to generate the statistics.

Functions to generate and activate some features on this program.
- build_stats.

the funcions you are going to be using are, this functions are locked if the build_stats method hasnt been called except the add function
- add: recieves a positive integer inside the range (0,999).
- less: recieves a positive integer inside the range (0,999).
- between: recieves two positive integer inside the range (0,999) the first integer must be lower than the second one.
- greater: recieves a positive integer inside the range (0,999)

the public getters are:
- get_data
- get_min
- get_max

the logic is private to the class the related functions are:
- __range_generator
- __set_indexed_dict


## :bulb: **Tip:** how to run and add values to the program
you can check the main.py file inside this repository to get an overall idea on how to use it, if you want to add your own values modify this same file on your local machine.

1. Import the DataCapture class<br/>
```from DataCapture import DataCapture```
2. Create an instance of the DataCapture class<br/>
```capture = DataCapture()```
3. Add values to the capture, this values are the ones that the statistic will check. 
> this integer values must be inside the range (0,999).
```
capture.add(3)
capture.add(10)
```
4. Call the build_stats method, its important to take into consideration that only the added numbers before this function call will be added to the statistics.
```
capture.build_stats()
```
5. At this moment you can use functions that werent available before, such as:
```
less_value = capture.less(30)
between_value = capture.between(4, 15)
greater_value = capture.greater(113)
```
8. Print the output you can also use the pdb lib to debug:<br/>
```print(less_value)```

7. Run the program:<br/>
```python main.py```

## :bulb: **Tip:** Run tests
The tests code is inside tests.py file, you need to install the pytest dependency
1. Install dependency
```pip install pytest```
2. Run test
```pytest tests.py```

Inside the tests.py file you can find a bunch of tests.
theres testing for inputing validation and the basic logic.
