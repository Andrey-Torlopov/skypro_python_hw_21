from storage import Storage
from exceprions import CapacityException

class Store(Storage):
    _items: dict[str, int]
    def __init__(self, capacity: int = 100):
        self._capacity = capacity
        self._items = {}

    def __str__(self):
        return f"\nDetails:\nCapacity: {self._capacity}\n{self.get_items()}"
    
    @property
    def items(self) -> dict[str, int]:
        return self._items

    @property
    def capacity(self) -> int:
        return self._capacity

    def add(self, name: str, count: int) -> None:
        if self._capacity - count >= 0:
            name_value = name.lower()
            current_count = self._items.get(name_value, 0)
            self._items[name_value] = current_count + count
            self._capacity -= count
        else:
            raise CapacityException(self._capacity)

    def remove(self, name: str, count: int) -> None:
        name_value = name.lower()
        current_count = self._items.get(name_value, 0)
        
        if current_count - count < 0:
            raise StorageRemoveException()
        
        self._items[name_value] = current_count - count
        self._capacity += current_count

    def get_free_space(self) -> int:
        return self._capacity
    
    def get_items(self) -> dict[str, int]:
        return self._items

    def get_unique_items_count(self) -> int:
        return list(self._items.keys())
    
    def can_add_element(self, name: str, count: int) -> bool:
        c = self.capacity
        c1 = count
        return self.capacity - count >= 0