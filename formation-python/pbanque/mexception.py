class BanqueException(Exception) :
    def __init__(self, message: str = ""):
        super().__init__()
        self.__message = message

    @property
    def message(self) -> str :
        return self.__message
    
class BanqueSoldeException(BanqueException):
    def __init__(self, message: str = ""):
        super().__init__(message)

class BanqueBlocageException(BanqueException):
    def __init__(self, message: str = ""):
        super().__init__(message)

class BanqueDaoException(BanqueException):
    def __init__(self, message: str = ""):
        super().__init__(message)

class BanqueDaoNotFoundException(BanqueDaoException):
    def __init__(self, message: str = ""):
        super().__init__(message)