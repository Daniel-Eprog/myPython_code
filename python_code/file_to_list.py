email_list = list()

gmail_count = 0
hotmail_count = 0
yahoo_count = 0
aol_count = 0

file_name = input("Please enter your file name:")

try:
    file_handle = open(file_name)
except:
    print("File cannot be opened: ",file_name)
    quit()

for line in file_handle:
    line = line.rstrip()
    email_list.append(line)
    if '@gmail.com' in line:
        gmail_count = gmail_count + 1
    if '@yahoo.com' in line:
        yahoo_count = yahoo_count + 1
    if '@aol.com' in line:
        aol_count = aol_count + 1
    if '@hotmail.com' in line:
        hotmail_count = hotmail_count + 1

print(email_list)
print("There are ", gmail_count, "gmail emails in your list.")
print("There are ", aol_count, "aol emails in your list.")
print("There are ", yahoo_count, "yahoo emails in your list.")
print("There are ", hotmail_count, "hotmail emails in your list.")
