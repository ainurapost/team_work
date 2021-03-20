# from app.py import car
#
# a = Car(model, year, host )

class Car:
    def __init__(self, model, year, host):
        self.model = model
        self.year = year
        self.host = host

    def get_info(self):
        print(f"Your model is {self.model}")
        print(f"Your year is {self.year}")
        print(f"Host of this car {self.host}")
        