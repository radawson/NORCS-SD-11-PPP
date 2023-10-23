class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self):
        super.__init__()

    def boost(self):
        self.max_speed = self.max_speed * 2

class SebulbasPod(Podracer):
    def __init__(self):
        super.__init__()

    def flame_jet(self, podracer):
        podracer.condition = "trashed"

if __name__ == "__main__":
    pod1 = Podracer(10, "old", 200)
    print(pod1.condition)
    pod1.repair()
    print(pod1.condition)