def computegrade(hours, rate):
    if(hours > 40):
        return 40*rate + (hours - 40)*rate*1.5
    else:
        return hours*rate

print(computegrade(45, 10))
