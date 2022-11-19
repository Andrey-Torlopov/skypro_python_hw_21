from store import Store
from exceprions import CapacityException


class Shop(Store):

    def __init__(self, capacity: int = 20):
        super().__init__(capacity)
        self._title_capacity = 5

    def add(self, name: str, count: int) -> None:
        name_value = name.lower()
        titles = set(self._items.keys())
        titles.add(name_value)
        if len(titles) > self._title_capacity:
            raise CapacityException(self._title_capacity)

        if self._capacity - count >= 0:
            current_count = self._items.get(name_value, 0)
            self._items[name_value] = current_count + count
            self._capacity -= count
        else:
            raise CapacityException(self._capacity)

    def __str__(self):
        return f"\nDetails:\nCapacity: {self._title_capacity}\n{self.get_items()}"
    
    def can_add_element(self, name: str, count: int) -> bool:
        name_value = name.lower()
        unique_items = list(self.get_items().keys())
        unique_items.append(name_value)
        if len(set(unique_items)) > self._title_capacity:
            return False
        
        return self.capacity - count >= 0
    