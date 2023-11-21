#3.2
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    
except:
    print('error please enter numeric input')
    quit()

if(hours>=40):
    weekPay = (rate*40) + ((hours-40)*(1.5*rate))
    monthPay = weekPay * 4
    yearPay = weekPay * 46
    print('Weekly Pay: ', weekPay)
    print('Monthly Pay: ', monthPay)
    print('Yearly Pay: ', yearPay)


else:
    weekPay = float(hours) * float(rate)
    monthPay = weekPay * 4
    yearPay = weekPay * 46
    print('Weekly Pay: ', weekPay)
    print('Monthly Pay: ', monthPay)
    print('Yearly Pay: ', yearPay)
