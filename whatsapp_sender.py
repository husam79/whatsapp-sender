from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")

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
    print("Sending the message to: {}".format(number))

    driver.get('https://web.whatsapp.com/send/?phone={}&text={}&type=phone_number&app_absent=0'.format(number, msg_to_send))

    #this number '16' is put by experiment.
    time.sleep(16)

    try:
        number_is_invalid_div = driver.find_element(By.XPATH, "//div[@data-testid='popup-contents']")
        if number_is_invalid_div.text.find("invalid") > -1:
            #this means the current phone number is not found (invalid)
            print("The number: {} is invalid or not found".format(number))
            missed_numbers.append(number)
            continue #take the next number
    except:
        pass

    try:
        send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send']")
        
        #this number '4' is put by experiment.
        time.sleep(4)

        send_button.click()

        #this number '4' is put by experiment.
        time.sleep(4)
        counter += 1
        
    except Exception as e:
        #in case for unexpected error, just log the last item we sent.
        with open('last_item.txt', 'w', encoding='utf-8') as log_file:
            log_file.writelines(str(counter + 1) + ' - ' + number)


with open('missed-numbers.csv', 'w', encoding='utf-8') as csv_file:
    csv_file.writelines(missed_numbers)


print('Finish')
