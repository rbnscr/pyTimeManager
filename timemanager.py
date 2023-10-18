import time
import builtins


def single_result(name, time_spend, prec, unit) -> str:
    return f"{name}: {time_spend:.{prec}f} {unit}"

def iter_result(name, time_spend, prec, unit, iteration) -> str:
    return f"{name} -> iteration: {iteration}: {time_spend:.{prec}f} {unit}"


class TimeManager:
    def __init__(self, verbose: bool = True) -> None:
        self.recorded_times = dict()
        self.recorded_iter_times = dict()
        self.verbose = verbose

    def start(self, name: str, unit: str, precision: int):
        if name in self.recorded_times.keys():
            self.print(f"Timer '{name}' already in use.")
            return
        else:
            self.print(f"Timer {name} start!")
            self.recorded_times[name] = RecordedTime(name, unit, precision)

    def stop(self, name: str):
        if name not in self.recorded_times.keys():
            self.print("Timer '{name}' not found.")
        else:
            current_time: RecordedTime = self.recorded_times[name]
            current_time.end_time()
            self.print(single_result(current_time.name, current_time.time_spend, current_time.prec, current_time.unit))
            # self.recorded_times.pop(name)

    def start_iter(self, name: str, unit: str, precision: int):
        if name in self.recorded_iter_times.keys():
            self.print(f"Timer '{name}' already in use.")
            return
        else:
            self.print(f"Timer {name} start!")
            self.recorded_iter_times[name] = RecordedTimeIter(name, unit, precision)


    def stop_iter(self, name: str, iteration):
        if name not in self.recorded_iter_times.keys():
            self.print(f"Timer '{name}' not found.")
        else:
            current_time: RecordedTimeIter = self.recorded_iter_times[name]
            current_time.time_step(iteration)
            self.print(iter_result(current_time.name, current_time.time_spend, current_time.prec, current_time.unit, iteration))

    def report(self):
        self.create_report()
        print(self.report)

    def write_report_to_csv(self):
        pass

    def create_report(self):
        self.report = ""

        if self.recorded_times.keys():
            self.report += "Name;Elapsed Time;Unit\n"
            for key in self.recorded_times.keys():
                ct: RecordedTime = self.recorded_times[key]
                self.report += f"{ct.name};{ct.time_spend:.{ct.prec}f};{ct.unit}\n"
        if self.recorded_times.keys():
            self.report += "Name;Iteration;Elapsed Time;Unit\n"
            for key in self.recorded_iter_times.keys():
                ct: RecordedTimeIter = self.recorded_iter_times[key]
                for iteration in ct.iterations.keys():
                    self.report += f"{ct.name};{iteration};{ct.time_spend:.{ct.prec}f};{ct.unit}\n"

    def print(self, text):
        match self.verbose:
            case True:
                print(text)
            case False:
                return

class RecordedTime:
    def __init__(self, name: str, unit: str, precision: int) -> None:
        self.name = name
        self.unit = unit.lower()
        self.prec = precision
        self.time_mult()
        self._start_time()
    
    def _start_time(self):
        self.start_time = time.time()

    def end_time(self):
        self.time_spend = (time.time() - self.start_time) * self.time_multiplier

    def time_mult(self):
        self.time_multiplier = 10**0 * (self.unit == "s") + 10**3 * (self.unit == "ms") + 10**6 * (self.unit == "mus") + 10**9 * (self.unit == "ns")

class RecordedTimeIter(RecordedTime):
    def __init__(self, name: str, unit: str, precision: int) -> None:
        self.name = name
        self.unit = unit.lower()
        self.prec = precision
        self.time_mult()

        self.iterations = dict()
        self._start_time()

    def time_step(self, iter_step):
        type_to_match = type(iter_step)
        if type_to_match == str:
            self.iterations[iter_step] = self.end_time()
        elif type_to_match == int: 
            self.iterations[f"{iter_step}"] = self.end_time()
        else:
            raise TypeError("Type not supported as key.")
        
        self._start_time()
