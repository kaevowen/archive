class Car():
    def __init__(self, name):
        self.name = name

    def run(self):
        print("차가 달립니다.")


class Truck(Car):
    def __init__(self, name, cap):
        super().__init__(name)
        self.cap = cap
        print(f'{name}에 {cap}kg 만큼의 ')

    def load(self):
        print("짐을 실었습니다.")

    def run(self):
        print("트럭이 달립니다.")


truck = Truck('트럭', '10')
truck.load()
truck.run()