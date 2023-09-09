import sqlite3
import re

zp = 1500
income = 1000
percent = 0.05
income = income - zp

final = zp + income * percent

print(final)