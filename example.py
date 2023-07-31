import time

from .timemanager import TimeManager 

tm = TimeManager()
tm.start("Test1", "ms", 3)
time.sleep(0.5)
tm.start("Test1", "ns", 3)
time.sleep(0.5)
tm.start("Test2", "ns", 2)
time.sleep(0.5)
tm.end("Test2")
tm.end("Test1")
tm.start("Test1", "ms", 3)
time.sleep(0.5)
tm.end("Test1")