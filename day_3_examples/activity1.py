class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def start(self):
        print("Vroom!")

    def talk(self, driver):
        print(f"Hello, {driver}, I am {self.name}.")

class Driver:
    def __init__(self, name, age, ranking):
        self.name = name
        self.age = age
        self.ranking = ranking

    def get_ranking(self):
        return self.ranking 
    
    def __str__(self):
        return f"{self.name} is ranked {self.ranking}."

class Race:
    def __init__(self, name, driver_limit) -> None:
        self.name = name
        self.driver_limit = driver_limit
        self.drivers = []

    def add_driver(self, driver):
        # If the number of drivers already assigned to the race does not exceed the driver_limit,
        # it should add a driver to the drivers list
        if len(self.drivers) == 0:
            self.drivers.append(driver)
        elif len(self.drivers) < self.driver_limit:
            # Add logic to the Race.add_driver method that prevents a driver from being 
            # added to a race if they are not within 10 points of the current average ranking 
            # in that race
            if abs(driver.get_ranking() - self.get_average_ranking()) <= 10:
                self.drivers.append(driver)

    def get_average_ranking(self):
        # Calculate the average ranking of all drivers in the drivers list
        driver_average = 0.00
        driver_total = 0
        for driver in self.drivers:
            driver_total += driver.get_ranking()
        driver_average = driver_total / len(self.drivers)
        return driver_average
    
    def get_drivers(self):
        driver_strings = []
        for driver in self.drivers:
            driver_strings.append(str(driver))
        return driver_strings
    
    def get_number_drivers(self):
        return len(self.drivers)

if __name__ == "__main__":
    my_car = Car("Kitt", 180)
    my_other_car = Car("Speedy", 55)

    my_car.talk("Michael")

    my_course = Race("Seattle 500", 4)

    my_driver = Driver("Dale Earnharft", 29, 100)
    print(str(my_driver))

    driver1 = Driver("Lewis Hamilton", 36, 83)
    driver2 = Driver("Eliud Kipchoge", 36, 95)
    driver3 = Driver("Sebastian Vettel", 34, 76)
    driver4 = Driver("Ayrton Senna", 34, 99)

    my_course.add_driver(driver1)
    my_course.add_driver(driver2)
    my_course.add_driver(driver3)
    my_course.add_driver(driver4)
    print(my_course.get_drivers())

    print(my_course.get_average_ranking())


