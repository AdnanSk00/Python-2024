class Vector:
    def __init__(self, list):
        self.list = list  

    def __len__(self):
        return len(self.list)


# Test the implementation
v1 = Vector([1, 2, 3, 6])

print(len(v1)) 