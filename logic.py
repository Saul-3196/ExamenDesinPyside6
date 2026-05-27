# logic.py
class CounterLogic:
    def __init__(self): 
        self._value = 0 

    def increment(self): 
        self._value += 1
        return self._value 

    def decrement(self): 
        self._value -= 1 
        return self._value 

    def get_value(self): 
        return self._value