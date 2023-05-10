# Import random
import random

class Vehicle:
    # Initialize the objects
    def __init__(self, color, speed, name,  model, year):
        self.color = color
        self.speed = speed
        self.name = name
        self.model = model
        self.year = year

    # Define vehicle method
    def start(self):
        self.speed = self.speed - random.randint(50, 100)
    # Define vehicle method
    def accelerate(self):
        self.speed = self.speed + 30
    # Define vehicle method
    def brake(self):
        self.speed = self. speed - 24
    # Define vehicle method
    def stop(self):
        self.speed = 0
     
    # Define the speed, name, color, model and year
    def get_speed(self):
        return self.speed
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year