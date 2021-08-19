total = 0
count = 0
average = 0
while True:
    inp = input('Enter a nubmer: ')
    if inp == 'done':
        print(total, count, average)
        break
    try:
        number = float(inp)
    except:
        print('Invalid input')
        number = float(input('Enter a number: '))
    total += number
    count += 1
    average = total / count


