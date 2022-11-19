class CapacityException(Exception):    
    def __init__(self, capacity: int, *args):
        super().__init__(args)
        self._capacity = capacity
        
    def __str__(self):
        return f"Не могу добавить элемент. Доступно: {self._capacity}"
    
class RequestException(Exception):
    def __str__(self):
        return "Некорректный запрос"

class SrorageException(Exception):
    def __init__(self, name: str, *args):
        super().__init__(args)
        self._name = name
        
    def __str__(self):
        return f"Не корректное хранилище с названием '{self._name}'"

class StorageRemoveException(Exception):
    def __str__(self):
        return f"Не хватает элементов"

    
