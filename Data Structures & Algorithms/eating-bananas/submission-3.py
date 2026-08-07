class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def hoursForSpeed(speed: int):
            hours: int = 0
            for naners in piles:
                time = (naners//(speed * -1)) * -1
                #print(f"naners: {naners}, time: {time}")
                hours += time

            #print(f"speed: {speed}, hours: {hours}")
            return hours

        min_speed: int = 1
        max_speed: int = max(piles)

        # binary search the speed
        counter = 100
        while min_speed <= max_speed and counter > 0:
            counter -= 1
            #print(f"min/max = {min_speed}/{max_speed}")
            if min_speed == max_speed:
                 return min_speed
            speed = (min_speed+max_speed) // 2

            hours = hoursForSpeed(speed)

            if hours > h:
                min_speed = speed + 1
                continue
            max_speed = speed

        return -1
                