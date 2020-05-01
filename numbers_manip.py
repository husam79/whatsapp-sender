"""
Manipulating and filtering raw telephone numbers, so 
they will be used later with whatsapp_sender script.

Note: it is not garantee that all numbers will be corrected. Some phone numbers will still un correct, So this 
script will add pre- '*' character before the suspect number.

"""
source = []
final = []

syr_initials = ['093','095','096','099','094','092','097','098']
turk_initials = ['053']

with open('raw-numbers.csv', 'r', encoding='utf-8') as csv_file:
    source = csv_file.readlines()

for num in source:
    number = num.strip()
    print(number)
    if number[0] == '+':
        final.append('00' + number[1:] + '\n')
    elif number[0:3] in syr_initials:
        final.append('00963' + number[1:] + '\n')
    elif number[0:3] in turk_initials:
        final.append('0090' + number[1:] + '\n')
    elif number[0:2] == '00':
        final.append(number + '\n')
    else:
        final.append('*' + number + '\n')


with open('source-numbers.csv', 'w', encoding='utf-8') as csv_file:
    csv_file.writelines(final)


print('finish')