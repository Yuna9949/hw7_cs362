def leapyear(y):
    LYChk = False
    if y % 4 == 0:
        LYChk = True
    return LYChk


#y = int(input('Input year : '))
#if leapyear(y):
#    print(y, end='')
#    print(' is a leap year.')
#else :
#    print(y, end='')
#    print(' is not a leap year.')
