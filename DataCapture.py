"""check for positive integers and missing params"""
def clean_data_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            if isinstance(args[1], int) and args[1] > 0 and args[1] < 999:
                res = func(*args, **kwargs)
                return res
            return f'Value {args[1]} most be a positive integer in the range (0, 999), it will be skipped'
        except IndexError:
            return "Please supply a int value to the function in the range (0, 999), it will be skipped"
    return wrapper

"""check for positive integers and missing params"""
def clean_data_decorator_second_param(func):
    def wrapper(*args, **kwargs):
            try:
                if isinstance(args[1], int) and isinstance(args[2], int) and args[1] > 0 and args[1] < 999 and args[2] > 0 and args[2] < 999:
                    res = func(*args, **kwargs)
                    return res
                return f'Value {args[1]} and {args[2]} most be a positive integer in the range (0, 999)'
            except IndexError:
                return "Please supply both positive integer values to the function in the range (0, 999)"
    return wrapper


class DataCapture:
    def __init__(self):
        self.__status = False
        self.__max = 0
        self.__min = 0
        self.__data = []
        self.__range_indexes_dict = {}
    
    @clean_data_decorator
    def add(self, value: int) -> None:
        self.__data.append(value)

    """
    return the amount of values using this logic
    x2 + amount of x2 on collection
    minus x1 less values 
    we take the less values from the bigger one and sum the amount o repetitions he has on the list
    after that remove the less values of the lower one so we keep just a range between the both
    [2,2,1]
    [11,0,2]
    11 + 2 - 2 = 11
    theres 13 lower values 
    """
    @clean_data_decorator_second_param
    def between(self, from_value: int, to_value: int) -> int:
        if self.__status:
            response = "the firts value passed to the function most be lower than the second one"
            if from_value < to_value:
                response =  self.__range_indexes_dict[to_value][0] + self.__range_indexes_dict[to_value][2] - self.__range_indexes_dict[from_value][0]
            return response
        return "Cant use this function before calling build_stats method"
    
    """Set minimun and maximun values and sort the data added, enables the less,great,between fucntions"""
    def build_stats(self) -> None:
        self.__data.sort()
        self.__max = max(self.__data)
        self.__min = min(self.__data)
        self.__set_indexed_dict()
        self.__status = True

    """in case the value is higher than our max we return 0, if not just return the second position of the list asigned to that key on the dict"""
    @clean_data_decorator
    def greater(self, value: int) -> int:
        if self.__status:
            return self.__range_indexes_dict[value][1] if value < self.__max else 0
        return "Cant use this function before calling build_stats method"

    """return the len of the captured data if the value is greater than our max, other wise return position 0 on list"""
    @clean_data_decorator
    def less(self, value: int) -> int:    
        if self.__status:    
            return self.__range_indexes_dict[value][0] if value < self.__max else len(self.__data)
        return "Cant use this function before calling build_stats method"

    """Creates a list object with the next detail
        index 0: less values
        index 1: greater values
        index 2: amount of duplicates for this number 
    """
    def __range_generator(self) -> None:
        for x in range(0, 999):
            if x < self.__min:
                yield x, [0, len(self.__data), self.__data.count(x)]
            elif x >= self.__min and x <= self.__max:
                count = 0
                for val in self.__data:
                    if val < x:
                        count += 1
                """lower values, higher values , repetitions"""
                yield x, [count, len(self.__data) - self.__data.count(x) - count, self.__data.count(x)]
            elif x > self.__max:
                yield x, [len(self.__data), 0, self.__data.count(x)]
    
    def __set_indexed_dict(self) -> None:
        range_gen = self.__range_generator()
        while True:
            try:
                index, data = next(range_gen)
                self.__range_indexes_dict[index] = data
            except StopIteration:
                break
    
    """Public methods to show the protected attributes"""
    def get_data(self) -> list:
        return self.__data
    
    def get_min(self) -> list:
        return self.__min
    
    def get_max(self) -> list:
        return self.__max
    