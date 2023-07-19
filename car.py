class Car:
#     pass #as a placeholder

#     make = None
#     model = None
#     year = None
#     color = None
    
##### These are the attributes of the object, describing the object #####
    def __init__(self, make, model, year, color): #use to construct objects for us
#         self.make = None
#         self.model = None
#         self.year = None
#         self.color = None
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
##### There are the methods related to the object, describing what it can do #####
    def drive(self): #self refers to the attribute using this function
#         print("This car is driving.")
        print(f"This {self.model} is driving")
    
    def stop(self):
#         print("This car is stopped")
        print(f"This {self.model} is stopped")

    def accelerate(self):
        print(f"This {self.model} is accelerating")
