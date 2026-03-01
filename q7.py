# Task 1: Define a Car class with attributes and methods
class Car:
    """A class to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize the Car with make, model, and year attributes.
        
        Args:
            make (str): The manufacturer of the car
            model (str): The model name of the car
            year (int): The year the car was manufactured
        """
        self.make = make
        self.model = model
        self.year = year
    
    def describe_car(self):
        """Print information about the car in the format: Year Make Model"""
        print(f"{self.year} {self.make} {self.model}")


# Task 2: Create an instance of the Car class and call describe_car method
# Create a Car instance with Toyota Corolla from 2020
my_car = Car(make="Toyota", model="Corolla", year=2020)

# Call the describe_car method to display the car information
my_car.describe_car()
