try:
    h = float(input('enter hours'))
except:
    print('Error, please enter numeric input')
    h = float(input('enter hours'))
try:
    r = float(input('enter rate'))
except:
    print('Error, please enter numeric input')
    r = float(input('enter rate'))
if( h > 40):
    print('Pay:', 40*r +(h-40)*r*1.5)

else:
    print('Pay:', h*r)

