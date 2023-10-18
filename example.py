import time

from timemanager import TimeManager 

tm = TimeManager(verbose=False)
tm.start("Test1", "ms", 3)
# time.sleep(0.5)
tm.start("Test1", "ns", 3)
# time.sleep(0.5)
tm.start("Test2", "ns", 2)
# time.sleep(0.5)

tm.start_iter("Iteration-Timer", "ns", precision=3)
for i in "Hallo hallo hallo, i bims".split():
    tm.stop_iter("Iteration-Timer", i)


tm.stop("Test2")
tm.stop("Test1")
tm.start("Test1", "ms", 3)
# time.sleep(0.5)
tm.stop("Test1")

tm.report()