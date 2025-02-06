class Car:
    def __init__(self, brand, model):
        self.model = model
        #making it private by putting __
        self.__brand = brand

    def get_brand(self):
        return self.brand

    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "Petrol or diesel"

class Electric_car(Car):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity
    def specs(self):
        return f"{self.brand} {self.model} with a capacity of {self.capacity} kW"
    def fuel_type(self):
        return "Petrol or diesel"    


#constructor is a special method that is called when an object is created

my_car = Car("Toyota", "Corolla")
print(my_car.brand)

my_other_car = Car("Honda", "Civic")
print(my_other_car.full_name())

my_car = Electric_car("Tesla", "Model 3", 70)
print(my_car.specs())

#encapsulation is the process of restricting access to methods and variables
#polymorphism is the process of having many forms