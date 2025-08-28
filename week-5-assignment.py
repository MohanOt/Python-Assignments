# Assignment 1: Smartphone Class

# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"

# Derived class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # call parent constructor
        self.storage = storage
        self.battery = battery
    
    # Method: check battery
    def check_battery(self):
        return f"Battery level: {self.battery}%"
    
    # Method: simulate installing an app
    def install_app(self, app_name):
        return f"{app_name} installed successfully on {self.device_info()}!"
    
    # Method: show storage info
    def storage_info(self):
        return f"Available storage: {self.storage}GB"

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 85)
phone2 = Smartphone("Apple", "iPhone 14", 128, 65)

# Using methods
print(phone1.device_info())
print(phone1.check_battery())
print(phone1.install_app("WhatsApp"))
print(phone2.storage_info())


# Activity 2: Polymorphism with Vehicles

class Vehicle:
    def move(self):
        pass  # abstract behavior (to be overridden)

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Demonstrating polymorphism
for v in vehicles:
    print(v.move())
