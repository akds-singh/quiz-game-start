# coding on __getattr__ , __setatttr__ , __delattr__

class TestAttr:
    def __init__(self):
        print("__init__")
        self.country = {"name": "india", "capital": "Delhi", "states": 30}


t = TestAttr()
print(t.country)