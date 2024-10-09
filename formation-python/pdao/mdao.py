class BaseDao :
    def __init__(self):
        pass

    def findAll(self):
        raise NotImplementedError()
    
    def findById(self, id):
        raise NotImplementedError()
    
    def create(self, obj):
        raise NotImplementedError()

    def update(self, obj):
        raise NotImplementedError()
    
    def deleteById(self, id):
        raise NotImplementedError()