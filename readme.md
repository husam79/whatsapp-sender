# Whatsapp Sender

**whatsapp_sender.py**

This wraper script is written using Python 3.7.4 and it used to send automated Whatsapp messages through whatsapp web app. This script can send messages to phone numbers without the need of existing previously as existing contacts.

To use this script you should first install selenium automator using the following command:

```
pip install selenium
```
Then you will need a driver (needed by selenium). You can find a list of available drivers for web browsers on the following link:
https://selenium-python.readthedocs.io/installation.html#drivers

If you prefer to work with Google Chrome, then you can find the following page:
https://sites.google.com/a/chromium.org/chromedriver/downloads

After you download the driver, unzip it, then copy the driver app into the current directory of the script.

**source-numbers.csv**

This is one column file, which contains the numbers you want to send the message to them. Each number should be a complete phone number,  for example:
```
0090123456789
```

**numbers_manip.py**

This is a helper file, it is not required for the "whatsapp_sender.py" script , you can use it to refomat a numbers list if needed. 

This script expect there is a one column file, which it is name: "raw-numbers.csv", the output will be "source-numbers.cs". This file is able to manipulate syrian mobile number as well as small part of turkish phone numbers. 

You can modify this script to fullfill your requirements.

Good luck!
