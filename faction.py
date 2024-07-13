from .client import *

class faction(client):
    def __init__(self, key:str):
        super().__init__(key)

    def get(self, selections:str="", id:str=""):
        data = self.call("faction", selections, id)
        if selections in data.keys():
            return data[selections]
        return data

    def chain(self, id:str=""):
        return self.get("chain", id)

    def positions(self):
        return self.get("positions")

    # ...

