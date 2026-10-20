# car fleet
# https://neetcode.io/problems/car-fleet/question
# code by aveia@github

class Solution:
    # def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
    #     from dataclasses import dataclass

    #     @dataclass
    #     class Car:
    #         pos: int
    #         speed: int
    #         fleet: int
    #         ttt: float # time to target

    #     cars = [
    #         Car(position[i], speed[i], i, (target - position[i]) / speed[i])
    #         for i in range(len(speed))
    #     ]
    #     cars.sort(key=lambda c: (c.pos, -c.speed))

    #     for i in range(len(speed) - 1, 0, -1):

    #         front = cars[i]
    #         rear = cars[i - 1]

    #         if rear.ttt <= front.ttt:
    #             rear.fleet = front.fleet
    #             rear.ttt = front.ttt

    #     fleets = set()
    #     for car in cars:
    #         fleets.add(car.fleet)

    #     return len(fleets)

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        cars = sorted([
            (position[i], (target - position[i]) / speed[i])
            for i in range(len(speed))
        ])

        fleets = len(speed)

        for i in range(len(speed) - 1, 0, -1):
            if cars[i - 1][1] <= cars[i][1]:
                cars[i - 1] = cars[i]
                fleets -= 1

        return fleets
