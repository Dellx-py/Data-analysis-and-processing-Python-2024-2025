from django.test import TestCase

# Create your tests here.


# print(ord('A'))
# print(ord('B'))
# print(ord('E'))

# print(ord('Z'))

# print(ord('a'))

# print(chr(65))

# for i in range(ord('A'), ord('Z')+1):
#     print ()
import pandas as pd

with open("parole.csv", "w") as fwriter:
    fwriter.write_through("parole")

df = pd.read_csv("parole.csv")