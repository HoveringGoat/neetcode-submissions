class DailyTemp:
    temp: int
    day: int

    def __init__(self, temp, day):
        self.temp = temp
        self.day = day

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # check stack against the current temp
        # if current temp is higher then pop from stack calc day offset and record in return list
        # reattempt if a pop was performed
        # add item 

        # init return array to zeros
        result: List[int] = [0] * len(temperatures)

        # stack is a list of tuples day, temp
        stack: List[DailyTemp] = []
        for day, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1].temp:
                popped = stack.pop()
                result[popped.day] = day - popped.day
            newDailyTemp = DailyTemp(temp, day)
            stack.append(newDailyTemp)
        return result