"""
Generate Anki cards for Roman numerals from 1 to 4999.
Probably a bad idea.

Works with Python 2 and 3.

"""
import csv

import roman  # pip/pip3 install roman

with open('roman_numerals.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(1, 5000):
        writer.writerow([roman.toRoman(i), i])
