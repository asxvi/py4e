#4.6
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))


def computePay(hours, rate):
    if(hours>=40):
        weekPay = (rate*40) + ((hours-40)*(1.5*rate))
    else:
        weekPay = float(hours) * float(rate)
    return(weekPay)
       
result = computePay(hours, rate)

print("Gross Pay", result)