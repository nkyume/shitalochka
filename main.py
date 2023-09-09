import re

class Pet:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

 
class Groomer:
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent
        self.income = 0
        
    def calculate_groomer_income(self, case):
        self.income += case.total_income * (self.percent * 0.01)
 
        
class Case:
    def __init__(self, date, time, pet, payment_method, price,
                 extra, total_income, trans, cash):
        
        self.day, self.month, self.year = date
        self.time = time
        
        self.pet = pet
        
        self.payment_method = payment_method
        self.price = price
        self.extra = extra 
        self.total_income = total_income
        self.transaction = trans
        self.cash = cash
        
                
class DailyReport:
    def __init__(self, date, admin):
        self.day, self.month, self.year = date
        self.cases = []
        
        self.admin = admin
        
    def add_case(self, case):
        self.cases.append[case]
        
        

class WeeklyReport:
    def __init__(self):
        pass
        


def main():
    with open('input.txt', encoding='utf8') as raw_input:
        text = raw_input.readlines()
        
    for line in text:
        if line == ['']:
            continue
        
        line = line.strip()
        line = line.split(':')
        line[0] = line[0].strip()
        if len(line) > 1:
            line[1] = line[1].strip()
            
        info = line.pop(0)
        
        
        # date match
        match = re.search('\d{2}[.,]\d{2}[.,]\d{4}', str(line))
        
        match info:
            case 'Имя':
                pet_name = line
            case 'Порода':
                pet_breed = line
            case 'Время':
                if len(line) > 1:
                    line = ':'.join(line)
                    time = line
            case 'Способ оплаты':
                if line == 'наличные':    
                    payment_method = 'cash'
                
                elif line == 'перевод':
                    payment_method = 'transaction'
                    
                elif 'наличные' in line and 'перевод' in line:
                    payment_method = 'both'
            case 'Стоимость':
                price = line
        
            case 'Доп. Услуги':
                extra = line
    
    
    
    
                
        
              
if __name__ == "__main__":
    main()
    
