import math
import os
import random
import re
import sys


def staircase(n):
    for i in range(1, n + 1):
        espacos = " " * (n - i)
        degraus = "#" * i
        print(espacos + degraus)
