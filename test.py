from tinydb import TinyDB, Query
import re
from dataclasses import dataclass


@dataclass
class Money:
    raw_income: int
    saloon_income: int
    groomers: list
    admins: list

income2 = Money(200,50,[{'name': 'vovchik', 'income': 10}, {'name': 'petya', 'income': 10}], [{'name': 'van', 'income': 5}])
income1 = Money(100,50,[{'name': 'vovchik', 'income': 10}, {'name': 'petya', 'income': 10}], [{'name': 'van', 'income': 5}])
print(income1)
print(income2)

db = TinyDB('db.json')

db.insert({'day': 29,
           'month': 7,
           'year': 2023,
           'raw income': income1.raw_income,
           'income': income1.saloon_income,
           'groomers': income1.groomers,
           'admins': income1.admins
           })
# test = Query()
# result = db.search(test.groomers.pupka > 0)

# for item in result:
#     print(item)
    
