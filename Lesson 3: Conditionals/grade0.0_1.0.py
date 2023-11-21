#3.3
try:
    score = float(input("Please input a number between 0 and 1.0: "))
except:
    print('error please enter numeric input between 0-1.0')
    quit()

if (score > 1.0):
    print('bad score')
elif (1.0 >= score >= .9):
    print('A')
elif (.9 >= score >= .8):
    print('B')
elif (.8 >= score >= .7):
    print('C')
elif (.7 >= score >= .6):
    print('D')
elif (.6 > score):
    print('F')