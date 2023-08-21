import sqlite3

def main():
    with open('input.txt', encoding='utf8') as raw_input:
        lines = raw_input.readlines()
        
        total_income = 0
        cash = 0
        transaction = 0

        groomers = []
        groomer = None
        
        for line in lines:
            #print(line, end="")
            line = line.strip()
            
            
            if 'Мастер:' in line:
                if groomer:
                    groomers.append(groomer)
    
                groomer = {'name': line.split(':')[1].strip(),
                           'salary': 0}
                
            # Money amount
            elif 'Стоимость:' in line:
                case_total = 0
                line = line.split(':')
                try:
                    money = int(line[1].strip())   
                    case_total += money
                except ValueError:
                    cost = line[1].strip().split('+')
                    
                    for info in cost:
                        info = info.strip()
                        if 'наличные' in info:
                            cash += int(info.split(' ')[0])
                            case_total += cash        
                        elif 'перевод' in info:
                            transaction += int(info.split(' ')[0])
                            case_total += transaction
            
            # Payment method           
            elif 'Способ оплаты:' in line:
                if line == 'Способ оплаты: перевод':
                    transaction += money
                    
                elif line == 'Способ оплаты: наличные':
                    cash += money
                total_income += case_total
                
            # Groomer percent
            elif 'Процент мастеру:' in line:
                line = line.split(':')
                percent = int(line[1]) / 100
                
                groomer['salary'] += case_total * percent
                
            # Administrator    
            elif 'Администратор:' in line:
                groomers.append(groomer)
                line = line.split(':')
                admin_name = line[1].strip()
            elif 'Администратор ЗП:' in line:
                line = line.split(':')
                admin_salary = int(line[1].strip())
                
            elif 'Администратор %:' in line:
                line = line.split(':')
                admin_percent = int(line[1].strip())
                admin_percent = admin_percent / 100
                
    saloon_income = total_income   
        
    for groomer in groomers:
        saloon_income -= groomer['salary'] 
                 
    saloon_income -= admin_salary
    if saloon_income < 0:
        admin_salary = admin_salary + (admin_salary * admin_percent)
    else:
        admin_salary = admin_salary + (saloon_income * admin_percent)   
    
    saloon_income -= saloon_income * admin_percent
            
                                              
    print()                
    print(f"Всего {total_income} рублей")
    print(f"Наличные: {cash} рублей")
    print(f"Перевод: {transaction} рублей")
    
    for groomer in groomers:
        print()
        print(f'Имя мастера: {groomer["name"]}')
        print(f'Зарплата мастера: {groomer["salary"]}')
        
    print()
    print(f'ЗП администратора: {admin_salary}')
    
    print(f'Доход салона: {saloon_income}')
    
         
    
             
if __name__ == "__main__":
    main()