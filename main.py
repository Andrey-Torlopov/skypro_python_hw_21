from request import Request
from storage import Storage
from store import Store
from shop import Shop
from exceprions import RequestException
from courier_proccessor import CourierProccessor

storages: dict[str, Storage] = {}

def prepeare_storages() -> dict[str, Storage]:
    store1 = Store()
    store2 = Store()
    shop1 = Shop()
    store1.add("A1", 20)
    store1.add("A2", 10)
    store1.add("A3", 5)
    store1.add("A4", 10)
    store1.add("A5", 15)
    store1.add("A6", 30)
    
    store2.add("A1", 10)
    store2.add("A2", 20)
    store2.add("A3", 30)
    store2.add("A4", 10)

    
    storages["s1"] = store1
    storages["s2"] = store2
    storages["m"] = shop1
    
    return storages
    
storages = prepeare_storages()

def main():
    while True:
        print("")
        user_input = input(
            "Введите запрос: (f.e. 'Доставить 3 печеньки из склад в магазин')\n"
            "Напишите 'stop' для выхода \n"
            "Напишите 'list' для отображения всех складов и магазинов\n"
            )

        if user_input.lower() == "list":
            print("")
            for item in storages.items():
                name, s = item
                print(name, s)
            continue

        if user_input.lower() == "stop":
            exit(0)

        try:
            request = Request(request_string=user_input)
            courier = CourierProccessor(request=request, storages=storages)
            courier.execute()
        except RequestException as e:
            print(f'\nНекорректный запрос: {str(e)}\nПопробуйте ввести снова')

    
if __name__ == '__main__':
    main()