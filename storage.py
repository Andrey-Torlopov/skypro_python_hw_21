from abc import ABC, abstractmethod

class Storage(ABC):
    @property
    @abstractmethod
    def items(self) -> dict[str, int]:
        ...

    @property
    @abstractmethod
    def capacity(self) -> int:
        ...
    
    @abstractmethod
    def add(self, name: str, count: int) -> None:
        ...
        
    @abstractmethod
    def remove(self, name: str, count: int) -> None:
        ...
    
    @abstractmethod
    def get_free_space(self) -> int:
        ...
    
    @abstractmethod
    def get_items(self) -> dict[str, int]:
        ...
    
    @abstractmethod
    def get_unique_items_count(self) -> int:
        ...
        
    @abstractmethod
    def can_add_element(self, name: str, count: int) -> bool:
        ...
    