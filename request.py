from storage import Storage
from exceprions import RequestException, SrorageException

class Request:
    def __init__(self, request_string: str):
        split_request = request_string.lower().split(' ')
        
        if len(split_request) != 7:
            raise RequestException()
        
        try:
            self.amount = int(split_request[1])
        except Exception as e:
            print(str(e))
            raise RequestException()
                
        self
        self.product = split_request[2]
        self.departure = split_request[4]
        self.destination = split_request[6]
        
        