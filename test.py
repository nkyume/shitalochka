import sqlite3
import re

zp = 1500
income = 2000
percent = 0.05
income = income - zp
if not percent == 0:
    final = zp + income * percent
else:
    final = zp
    
print(int(final))