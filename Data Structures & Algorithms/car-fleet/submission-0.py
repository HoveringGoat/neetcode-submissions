class Arrival:
    arrivalTime: int = 0
    distance: int = 0

    def __init__(self, position, speed, target):
        self.distance = target - position
        self.arrivalTime = self.distance / speed

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calc arrival time for all cars
        arrivals: List[Arrival] = []
        
        for i in range(len(position)):
            arrivals.append(Arrival(position[i], speed[i], target))
        
        # sort arrivals by their original positions
        arrivals.sort(key=lambda x: x.distance)

        fleets: int = 1
        lastCar = arrivals[0]
        for car in arrivals[1:]:
            if car.arrivalTime > lastCar.arrivalTime:
                fleets += 1
                lastCar = car
        
        return fleets


