from request import Request
from storage import Storage
from exceprions import CapacityException, SrorageException, StorageRemoveException

class CourierProccessor:
    # Курьер уже решает куда и что тащить и обрабатывать.
    # У него есть список складов-магазинов и сам запрос
    def __init__(self, request: Request, storages: dict[str, Storage]):
        self._request = request
        self._storages = storages
        
    def execute(self) -> None:
        # Find storage
        storage_name = self._request.departure
        storage = self._storages.get(storage_name)
        if storage is None:
            print(f'{storage_name} не найден. Запрос не может быть выполнен')
            return

        # Find shop
        destination_name = self._request.destination
        shop = self._storages.get(destination_name)
        if shop is None:
            print(f'{destination_name} не найден. Запрос не может быть выполнен')
            return

        # # Make transaction
        product = self._request.product
        amount = self._request.amount
        if storage.can_add_element(name=product, count=amount) == False:
            print(f"Не хватает на складе. Попробуйте заказать меньше.\n")
            return
        print("Нужное количество есть на складе")
        
        if shop.can_add_element(name=product, count=amount) == False:
            print('В магазине не хватает места. Попробуйте выбрать другой магазин')
            return
        
        print("Магазин может принять данное количество товара")
        
        # # Try get from storage
        try:
            storage.remove(name=product, count=amount)
            print(f"Курьер забрал {amount} {product} со {storage_name}")    
            print(f"Курьер везет {amount} {product} со {storage_name} в {destination_name}")
            shop.add(name=product, count=amount)
            print(f"Курьер доставил {amount} {product} со {storage_name} в {destination_name}")
        except StorageRemoveException as e:
            print(str(e))    
            return
        except CapacityException as e:
            print(str(e))
            return
        