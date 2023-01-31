def clean_data_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except KeyError:
            return "Invalid value"
    return wrapper
        
class DataCapture:
        
    data = []
    sorted_unique_data = []
    indexed_data = {}
    
    def __init__(self):
        self.data = []
        self.sorted_unique_data = []
        self.indexed_data = {}

    def add(self, value):
        self.data.append(value)

    @clean_data_decorator
    def between(self, from_value, to_value):
        response = "the firts value passed to the function most be lower than the second one"
        if from_value < to_value:
            response =  self.indexed_data[to_value] + 1 - self.indexed_data[from_value]
        return response
    
    def build_stats(self):
        self.data.sort()
        [self.sorted_unique_data.append(key) for key in self.data if key not in self.sorted_unique_data]
        self.indexed_data = {x: self.data.index(x) for x in self.sorted_unique_data}

    @clean_data_decorator
    def greater(self, value):
        return self.indexed_data[self.sorted_unique_data[-1]] - (self.indexed_data[value] if self.indexed_data[value] != 0 else 1)
        
    @clean_data_decorator
    def less(self, value):        
        return self.indexed_data[value]
