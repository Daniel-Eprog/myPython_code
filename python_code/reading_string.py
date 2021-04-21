word = input("Please enter your desired word. ")
count = 0

for letter in word:
    if letter == 'a':
        count = count + 1
    print(letter)
print("There are",count, "a's in the word",word)
print(word,"is",len(word),"digits long.")
