# Whatsapp Sender

**whatsapp_sender.py**

This wrapper script is written using Python 3.11.4 and used to send automated WhatsApp messages through the WhatsApp web app. This script can send messages to phone numbers without the need for existing contacts.

To use this script you should first install Selenium Automator using the following command:

```
pip install -U selenium
```
Then you will need a driver (needed by selenium). You can find a list of available drivers for Google Chrome on the following link:
[https://selenium-python.readthedocs.io/installation.html#drivers](https://chromedriver.chromium.org/downloads)

**source-numbers.csv**

This is one column file, which contains the numbers you want to send the message to them. Each number should be a complete phone number,  for example:
```
90123456789
```

**numbers_manip.py**

This is a helper file, it is not required for the "whatsapp_sender.py" script, you can use it to reformat a numbers list if needed. 

This script expects there is a one-column file, which is named: "raw-numbers.csv", the output will be "source-numbers.cs". This file is able to manipulate Syrian mobile numbers as well as a small part of Turkish phone numbers. 

You can modify this script to fulfill your requirements.

Good luck!
