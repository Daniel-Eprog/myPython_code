text_file = input('Please enter file name:')
file_handle = open(text_file)

array2 = dict()
for line in file_handle:
    words = line.split()
    for word in words:
        array2[word] = array2.get(word,0) + 1

biggest_word = None
biggest_count = None
for word, count in array2.items():
    if biggest_count is None or count > biggest_count:
        biggest_word = word
        biggest_count = count

print(biggest_word, biggest_count)
