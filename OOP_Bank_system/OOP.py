# class Vehicle():
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         print (f'The seating capacitt of a {self.name} is {capacity} passengers')

# class Bus(Vehicle):
#     def __init__(self, name, max_speed, mileage, seating_capacity=50):
#         self.seating_capacity = seating_capacity
#         super().__init__(name, max_speed, mileage)


# # OOP Excercise 4: Class inheritance

# bus1 = Bus('Volvo School', 200, 10)
# print(bus1.seating_capacity)



class Vehicle():
    vehicle_color = 'White'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def get_vehicle_color(self):
        print(f'Color {Vehicle.vehicle_color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}')

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


bus1 = Bus('Volvo School', 200, 10)
bus2 = Bus('Audi School', 300, 10)
print(bus1.vehicle_color)
print(bus2.vehicle_color)

bus1.get_vehicle_color()
bus2.get_vehicle_color()