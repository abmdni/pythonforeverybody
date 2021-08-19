file_name = input('Enter a file name:')
try:
    fhandle = open(file_name)
except:
    print('file cannot be opened:')
    quit()
for line in fhandle:
    print(line.rstrip().upper())
