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
    def __init__(self, date):
        
        self.day, self.month, self.year = date
        self.time = None
        
        self.pet = None
        
        self.payment_method = None
        self.price = None
        self.extra = None
        self.total_income = None
        self.transaction = None
        self.cash = None
        
                
class DailyReport:
    def __init__(self, date):
        self.day, self.month, self.year = date
        self.cases = []
        
        self.admin = None
        
    def add_case(self, case):
        self.cases.append[case]
        
        
class WeeklyReport:
    def __init__(self):
        pass
        
        
def main():
    with open('input.txt', encoding='utf8') as raw_input:
        text = raw_input.readlines()
        
    current_date = None 
    
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
        date = re.search('\d{2}\.\d{2}\.\d{4}', str(line))
        case_number = re.search('^\d+\.?$', str(line))
        
        # if date True and not == to current_date: start new day
        if date == True:
            date = date.string
            if not current_date:
                current_date = date
                day = DailyReport(date.split('.'))
            elif not current_date == date:
                current_date = date
                day = DailyReport(date.split('.'))
              
                
        # if case_number == True: start new case
        if case_number == True:
            case = Case(date.split('.'))
            DailyReport.add_case(case)
        
        match info:
            case 'Имя':
                pet_name = line
            case 'Порода':
                pet_breed = line
                pet = Pet(pet_name, pet_breed)
                case.pet = pet
            case 'Время':
                if len(line) > 1:
                    line = ':'.join(line)
                    case.time = line
            case 'Способ оплаты':
                if line == 'наличные', 'наличка':    
                    case.payment_method = 'cash'
                elif line == 'перевод':
                    case.payment_method = 'transaction'
                elif 'наличные' in line and 'перевод' in line:
                    case.payment_method = 'both'
            case 'Стоимость':
                pass   
            case 'Доп. Услуги':
                extra = line
        
    
    
    
    
                
        
              
if __name__ == "__main__":
    main()
    
