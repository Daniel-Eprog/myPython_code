smallest_num = 'none'
for value in [2, 6, 7, -4, 10, -56, -6]:
    if smallest_num == 'none':
        smallest_num = value
    elif value < smallest_num:
        smallest_num = value
print(smallest_num)
