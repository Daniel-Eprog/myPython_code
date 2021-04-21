max = 0
min = -1
file_name = input("Please enter your file name:")

try:
    file_handle = open(file_name)
except:
    print("File cannot be opened: ",file_name)
    quit()

x = int(input("Would you like to find the max or min? 1) Max 2) Min: "))

if x == 1:
    for line in file_handle:
        line = line.rstrip()
        line = int(line)
        if max < line:
            max = line
    print(max)
elif x == 2:
    for line in file_handle:
        line = line.rstrip()
        line = int(line)
        if min > line:
            min = line
    print(min)
else:
    print("Sorry, that is an invalid entry.")
