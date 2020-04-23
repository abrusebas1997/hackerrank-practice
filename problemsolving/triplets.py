"""Alice and Bob each created one problem
 for Hacker Rank. A reviewer rates the two challenges,
 awarding points on a scale from 1 to 100 for three categories:
  problem clarity, originality, and dificulty.
  Alice has a = (a[0], a[1], a[2]) and the rating for bob is
  the triplet b = (b[0], b[1], b[2]).
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    score_a = 0
    score_b = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            score_a += 1
        elif a[i] < b[i]:
            score_b += 1
    return score_a, score_b
