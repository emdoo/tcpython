from .client import *

class market(client):
    def __init__(self, key:str):
        super().__init__(key)

    def get(self, selections:str="", id:str=""):
        return self.call("market", selections, id)

    # ...
