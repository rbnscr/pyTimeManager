import time

class TimeManager:
    def __init__(self) -> None:
        self.recorded_times = dict()

    def start(self, name: str, unit: str, precision: int):
        if name in self.recorded_times.keys():
            print(f"Timer '{name}' already in use.")
            return
        else:
            self.recorded_times[name] = RecordedTime(name, unit, precision)

    def end(self, name: str):
        if name not in self.recorded_times.keys():
            print("Timer '{name}' already in use.")
        else:
            current_time: RecordedTime = self.recorded_times[name]
            current_time.end_time()
            self.recorded_times.pop(name)



class RecordedTime:
    def __init__(self, name: str, unit: str, precision: int) -> None:
        self.name = name
        self.unit = unit.lower()
        self.prec = precision
        self.time_mult()
        print(f"Timer {self.name} start!")
        self.start_time = time.time()
    
    def end_time(self):
        self.time_spend = (time.time() - self.start_time) * self.time_multiplier
        print(f"Elapsed time for {self.name}: {self.time_spend:.{self.prec}f} {self.unit}")

    def time_mult(self):
        self.time_multiplier = 10**0 * (self.unit == "s") + 10**3 * (self.unit == "ms") + 10**6 * (self.unit == "mus") + 10**9 * (self.unit == "ns")



