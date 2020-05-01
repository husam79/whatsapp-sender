from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

#just waiting while scanning the QR-code and open the web app.
w = input('When ready, press enter to continue..')

#each number should has the following format: 00[country-code][mobile-number]. Example: 00901234567890
source_numbers = []

#load phone numbers from file.
#this file is simple csv file contains just one field. This field is just a phone number with previous format.
with open('source-numbers.csv', 'r', encoding='utf-8') as csv_file:
    source_numbers = csv_file.readlines()

#this list to store the wrong phone numbers.
missed_numbers = []

msg_to_send = 'Hello there..'

counter = 0
for number in source_numbers:
    driver.get('https://web.whatsapp.com/send?phone={}'.format(number))

    #this number '16' is put by experiment.
    time.sleep(16)
    try:
        not_found_msg = driver.find_element_by_class_name('_3lLzD')
        missed_numbers.append(number)
        continue
    except:
        pass

    try:
        msg_box1 = driver.find_elements_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')[1]
        msg_box1.send_keys(msg_to_send)

        send_button = driver.find_element_by_class_name('_35EW6')

        #this number '1' is put by experiment.
        time.sleep(1)
        send_button.click()

        #this number '6' is put by experiment.
        time.sleep(6)
        counter += 1
        
    except:
        #in case for unexpected error, just log the last item we sent.
        with open('last_item.txt', 'w', encoding='utf-8') as log_file:
            log_file.writelines(str(counter) + ' - ' + number)


with open('missed-numbers.csv', 'w', encoding='utf-8') as csv_file:
    csv_file.writelines(missed_numbers)


print('Finish')
