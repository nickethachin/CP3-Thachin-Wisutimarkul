class Vehicle:
    licenseCode = ""
    serialCode = ""
    def sayHello(self):
        print("Hello! I'm %s." %(self.type))
    def turnOnEngine(self):
        print("Engine : ON")
    def turnOnAiConditioner(self):
        print("Aircondition : ON")

class Car(Vehicle):
    type = "Car"
    pass

class Pickup(Vehicle):
    type = "Pickup"
    capSize = ""

    def openCap(self):
        print("Back cap : Open")
    pass

pickup1 = Pickup()
pickup1.turnOnEngine()
pickup1.turnOnAiConditioner()
pickup1.sayHello()