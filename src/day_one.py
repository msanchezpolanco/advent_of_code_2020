from sys import stdin, stdout
import itertools
import numpy as np

nums = [int(x) for x in stdin.read().split()]

for numbers in itertools.combinations(nums, 2):
    if sum(numbers) == 2020:
        stdout.write(str((np.prod([number for number in numbers]))))
