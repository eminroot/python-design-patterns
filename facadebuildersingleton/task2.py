class House:

    def __init__(self,builder):
        self.rooms = builder.rooms
        self.floors = builder.floors
        self.windows = builder.windows

    def represent(self):
        return f"{self.rooms},{self.floors},{self.windows}"


class HouseBuilder:
    def __init__(self):
        self.rooms = None
        self.floors = None
        self.windows = None

    def set_rooms(self,value):
        self.rooms = value

    def set_floors(self,value):
        self.floors = value

    def set_windows(self,value):
        self.windows = value

    def build(self):
        return House(self)

h1 = HouseBuilder()
h1.set_rooms(1)
h1.set_floors(1)
h1.set_windows(1)
h1 = h1.build()
print(h1.represent())



class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.status = "hello"
        return cls._instance


config1 = Config()
config2 = Config()
print(config1.status)
print(config2.status)


class TV:
    def on(self):
        print("on")

class Speaker:
    def on(self):
        print("on")

class Light:
    def on(self):
        print("on")


class Facade:
    def __init__(self):
        self.light = Light()
        self.tv = TV()
        self.speaker = Speaker()

    def start(self):
        self.light.on()
        self.tv.on()
        self.speaker.on()


facade = Facade()
facade.start()