from .client import *

class torn(client):
    def _torn(self, key:str):
        super().__init__(key)

    def get(self, selections:str="", id:str=""):
        return self.call("torn", selections, id)

    def properties(self):
        return self.get("properties")

    # ...
