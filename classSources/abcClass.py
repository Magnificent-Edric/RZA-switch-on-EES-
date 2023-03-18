from abc import ABC, abstractmethod

class Object(ABC):
    def __init__(self, name, cVolt, number):
        self._name = name
        self._cVolt = cVolt
        self._number = number
    
    def get_name(self):
        return self._name
    
    def get_number(self):
        return self._number
    
    def get_vol(self):
        return self._cVolt
    
    def set_name(self, name):
        self._name = name
    
    def set_number(self, number):
        self._number = number

    def set_volt(self, volt):
        self._cVolt = volt

    @abstractmethod
    def object_work(self, res, vlFix):
        pass
