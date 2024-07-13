from .client import *

class property(client):
    def __init__(self, key:str):
        super().__init__(key)

    def get(self, selections:str="", id:str=""):
        return self.call("property", selections, id)

    # ...
