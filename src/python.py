import datetime
from typing import reveal_type


def now() -> float:
     now = datetime.datetime.now()
     milliseconds = now.timestamp() * 1_000
     return milliseconds

# print(now())
# print(type(now()))

def timelapse(function_to_test):
    initial_time:datetime = now()
    function_to_test
    final_time:datetime = now()
    timelapse: int= final_time - initial_time
    print(f"L'éxécution a duré {timelapse} millisecondes")

def calculate(number1, number2)->int:
    return number1 + number2

print(timelapse(calculate(6, 5)))

# def