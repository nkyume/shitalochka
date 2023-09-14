import re
import datetime

class Pet:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Case:
    def __init__(self, date, time, groomer_name, groomer_percent,
                pet, price, extra, notes):
        self.date = date
        self.time = time

        self.transaction = 0
        self.cash = 0
        self.__add_money(price)
        self.__add_money(extra)
        
        self.pet = pet
        self.groomer_name = groomer_name
        self.groomer_percent = groomer_percent * 0.01
        
        self.notes = notes
    
    
    @property    
    def groomer_income(self):
        return self.raw_income - self.raw_income * self.groomer_percent
    
    @property
    def saloon_income(self):
        return self.raw_income - self.groomer_income
    
    @property
    def raw_income(self):
        return self.cash + self.transaction
    
    def __add_money(self, raw_price):
        transaction = cash = 0
        raw_price = raw_price.split('+')
        for payment in raw_price:
            payment = payment.strip().split(' ')
            if 'наличные' in payment or 'наличка' in payment:
                cash += int(payment[0].strip())
            elif 'перевод' in payment or 'по карте' in payment:
                transaction += int(payment[0].strip())
        self.cash += cash
        self.transaction += transaction 
                
                                             
class DailyReport:
    def __init__(self, date):
        self.date = date
        self._cases = []
    
    def add_case(self, case):
        self._cases.append(case)
        
    @property    
    def report(self):
        cash = 0
        transaction = 0
        for case in self._cases:
            cash += case.cash
            transaction += case.transaction
            raw = cash + transaction
        return {
                'date': self.date,
                'cash': cash,
                'transaction': transaction,
                'raw': raw,
                'saloon': self.saloon_income,
                'groomers': self.groomers_income,
                'admin': {self.admin_name: self.admin_income}
                }
        
    @property   
    def saloon_income(self):
        total = 0
        for case in self._cases:
            total += case.saloon_income
        return total
        
    @property
    def groomers_income(self):
        groomers = {}
        for case in self._cases:
            if not case.groomer_name in groomers:
                groomers[case.groomer_name] = 0
            groomers[case.groomer_name] += case.groomer_income
        return groomers
      
    @property        
    def admin_income(self):
        if self.admin_percent == 0:
            return self.admin_salary
        return self.admin_salary + self.saloon_income * self.admin_percent
                
    def set_admin(self, admin_name, admin_salary, admin_percent):
        self.admin_name = admin_name
        self.admin_salary = admin_salary
        self.admin_percent = admin_percent * 0.01
       
                                           
class WeeklyReport:
    def __init__(self):
        self.__days = []
    
    def add_day(self, day):
        self.__days.append(day)
    
    @property
    def income(self):
        for day in self.__days:
            daily_report = day.get_money()
    @property    
    def report(self):
        raw = 0
        cash = 0
        transaction = 0
        saloon = 0
        groomers = {}
        admins = {}
        for day in self.__days:
            raw += day.report['raw']
            cash += day.report['cash']
            transaction += day.report['transaction']
            saloon += day.report['saloon']
            for key in day.report['groomers']:
                if not key in groomers:
                    groomers[key] = 0
                groomers[key] += day.report['groomers'][key]
            for key in day.report['admin']:
                if not key in admins:
                    admins[key] = 0
                admins[key] += day.report['admin'][key]
        return {
            'Наличные': cash,
            'Перевод': transaction,
            'Всего': raw,
            'Доход салона': saloon,
            'Мастер': groomers,
            'Администратор': admins    
        }
                       
def main():
    with open('input.txt', encoding='utf8') as raw_input:
        text = raw_input.readlines()
    week = WeeklyReport()    
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
        
        # start new day if date True and not == current_date
        date_match = re.search('\d{2}\.\d{2}\.\d{4}', str(info))
        
        if date_match:
            date = date_match.string
            date = create_date(date)
            if not current_date:
                current_date = date
                day = DailyReport(date)
                week.add_day(day) 
            elif not current_date == date:
                current_date = date
                day = DailyReport(date)
                week.add_day(day)
               
        # print(info, line)
        match info:
            case 'Мастер':
                groomer_name = line[0].strip()
            case 'Администратор':
                admin_name = line[0].strip()
            case 'Администратор ЗП':
                admin_salary = int(line[0].strip())
            case 'Администратор процент':
                admin_percent = int(line[0].strip())
                day.set_admin(admin_name=admin_name,
                              admin_salary=admin_salary,
                              admin_percent=admin_percent)
                # print(day.report())
            case 'Номер':
                pass   
            case 'Имя':
                pet_name = line[0].strip()
            case 'Порода':
                pet_breed = line[0].strip()
            case 'Время':
                if len(line) > 1:
                    line = ':'.join(line)
                    time = line
                else:
                    time = line[0].replace('.', ':')
            case 'Стоимость':
                price = line[0].strip()
            case 'Доп. услуги':
                extra = line[0].strip()
            case 'Процент мастеру':
                groomer_percent = int(line[0].strip())
            case 'Тип записи':
                pass
            case 'Примечания':
                notes = line[0] 
                
                pet = Pet(pet_name, pet_breed)
                case = Case(date=date,
                            time=time,
                            groomer_name=groomer_name,
                            groomer_percent=groomer_percent,
                            pet=pet,
                            price=price,
                            extra=extra,
                            notes=notes
                            )
                day.add_case(case)  
                
    with open('output.txt', encoding='utf8', mode='w') as file:
        for key in week.report:
            if key == 'Мастер':
                file.write(f'\n{key}: \n')
                for groomer in week.report[key]:
                    file.write(f'{groomer}: {week.report[key][groomer]} рублей\n')
                continue
                
            elif key == 'Администратор':
                file.write(f'\n{key}: \n')
                for admin in week.report[key]:
                    file.write(f'{admin}: {week.report[key][admin]} рублей\n')
                continue
                
            file.write(f'{key}: {week.report[key]} рублей\n')

        
    
    
    
    
def create_date(date):
    day, month, year = date.split('.')
    day = remove_first_zero_from_number(day)
    month = remove_first_zero_from_number(month)
    year = int(year)
    
    return datetime.date(day=day, month=month, year=year)
    
def remove_first_zero_from_number(number):
    if number[0] == 0:
        number = number[1]
    return int(number) 
                
if __name__ == "__main__":
    main()