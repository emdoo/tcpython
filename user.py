from .client import *

class user(client):
    def __init__(self, key:str):
        super().__init__(key)

    def get(self, selections:str="", id:str=""):
        return self.call("user", selections, id)

    def crimes(self):
        return self.get("crimes")

    # ...
