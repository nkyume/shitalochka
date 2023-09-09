import re


def main():
    with open('input.txt', encoding='utf8') as raw_input:
        text = raw_input.readlines()
        
        total_income = 0
        cash = 0
        transaction = 0

        groomers = []
        groomer = None
        
        date_current = None
        for line in text:
            line = line.strip()
            line = line.split(':')
            
            
            
            if line == ['']:
                continue
            
            match = re.search('\d{2}[.,]\d{2}[.,]\d{4}', str(line))
            if match:
                date_new = match.string[2:len(match.string)-2]
                
                if not date_current:
                    date_current = date_new  
                    continue
                elif not date_current == date_new:
                    date_current = date_new
                    
                    continue
            
            elif 'Мастер' in line:
                if groomer:
                    groomers.append(groomer)
                groomer = {'name': ,
                           'salary': 0}
                      
            elif 'Способ оплаты' in line:
                payment_method = line[1].strip().lower()
            
            elif 'Стоимость' in line:
                case_income = 0
                if payment_method == 'наличные':
                    case_income += int(line[1].strip())
                    cash += case_income
                    
                elif payment_method == 'перевод':
                    case_income += int(line[1].strip())
                    transaction += case_income
                       
                elif payment_method == 'наличные + перевод' or 'перевод + наличные':
                    tmp_money = line[1].strip().split('+')
                    for mney in tmp_money:
                        case_income += int(mney.strip().split(' ')[0].strip())
                        if 'наличные' in mney:
                            cash += case_income   
                        elif 'перевод' in mney:
                            transaction += case_income
            
            elif 'Доп. услуги' in line:
                if line[1] == '':
                    pass
                else:
                    line = line[1].strip().split(' ')
                    case_income += int(line[0])
    print(groomers)
            
            
def calculate_groomer_income(percent, case_income):
    percent = percent * 0.01
    groomer_income = case_income * percent
    return groomer_income
    
              
if __name__ == "__main__":
    main()