class TimeMap:
    map = {}

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.map:
            times = self.map[key]
            times[timestamp] = value
        else:
            newMap = {}
            newMap[timestamp] = value
            self.map[key] = newMap
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            times = self.map[key]
            if timestamp in times:
                return times[timestamp]
            else:
                lastTime: int = None
                for time in times.keys():
                    if time < timestamp:
                        lastTime = time
                if lastTime is not None:
                    return times[lastTime]

        return ""
        
