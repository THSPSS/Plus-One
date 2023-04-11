class ParkingSystem:
    #first attempt
    #using dictionary
    def __init__(self, big: int, medium: int, small: int):
        self.dict = {
            1: big,
            2: medium,
            3: small,
        }

    def addCar(self, carType: int) -> bool:
        if self.dict[carType] >= 1:
            self.dict[carType] -= 1
            return True
        return False


    #other solution
    #using list

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slots[carType - 1] > 0:
            self.slots[carType - 1] -= 1
            return True
        return False




# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))

