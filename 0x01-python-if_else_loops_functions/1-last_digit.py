#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
num = number % 10:
if num > 5:
  print("Last digit of", number, "is", num, "and is greater than 5")
elif num == 0:
  print("Last digit of", number, "is", num, "and is 0")
else:
  print(f"The last digit of"{number} "is"{num} "and is less than 6 and not 0")
