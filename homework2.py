import time
import cProfile
import pstats

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def square_table(n):
    return {x: x**2 for x in range(n)}

def cube_table(n):
    return {x: x**3 for x in range(n)}

def delay(seconds):
    time.sleep(seconds)

profiler = cProfile.Profile()
profiler.enable()

factorial(124251)
square_table(2848474)
cube_table(4567823)
delay(3)

profiler.disable()

with open('profile_results.txt', 'w') as f:
    stats = pstats.Stats(profiler, stream=f)
    stats.strip_dirs().sort_stats('cumulative').print_stats()
