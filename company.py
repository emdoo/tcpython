from .client import *

class company(client):
    def __init__(self, key:str):
        super().__init__(key)

    def get(self, selections:str="", id:str=""):
        return self.call("company", selections, id)

    def employees(self):
        return self.get("employees")

    # ...
