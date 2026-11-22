class House:
    def __init__(self,builder):
        self.rooms = builder.rooms
        self.windows = builder.windows
        self.floors = builder.floors
    def represent(self):
        return f"{self.rooms},{self.windows},{self.floors}"

class HouseBuilder:
    def __init__(self):
        self.rooms = None
        self.windows = None
        self.floors = None

    def set_rooms(self,value):
        self.rooms = value

    def set_windows(self,value):
        self.windows = value

    def set_floors(self,value):
        self.floors = value

    def build(self):
        return House(self)

h1 = HouseBuilder()
h1.set_rooms(1)
h1.set_floors(1)
h1.set_windows(1)
h1=h1.build()
print(h1.represent())