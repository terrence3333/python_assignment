# Base class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Encapsulated attribute

    # Method to display smartphone info
    def info(self):
        return f"{self.brand} {self.model} costs ${self.__price}"

    # Getter for price
    def get_price(self):
        return self.__price

    # Setter for price
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price

# Inheritance: AdvancedSmartphone inherits from Smartphone
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, price, camera_megapixels):
        super().__init__(brand, model, price)  # Call parent constructor
        self.camera_megapixels = camera_megapixels

    # Override info method to include camera
    def info(self):
        return f"{self.brand} {self.model} costs ${self.get_price()} and has {self.camera_megapixels}MP camera"

# Create objects
phone1 = Smartphone("Samsung", "Galaxy A12", 200)
phone2 = AdvancedSmartphone("Apple", "iPhone 14", 1000, 12)

print(phone1.info())
print(phone2.info())
