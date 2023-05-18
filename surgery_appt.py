"""
This script navigates to Houston's animal shelter website and checks for open spay/neuter appointments 
for foster dogs for the current and subsequent month, and chimes an alert sound if there is an opening. 
A cronjob runs the script every 5 mins when the computer is awake.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # chromedriver executable file should be in same folder
import chime
import time

# instance of Options class allows us to configure Headless Chrome
options = Options()
  
# this parameter tells Chrome that it should be run without UI (Headless)
options.headless = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://barchouston.as.me/foster")

# Navigate to foster dog appointment calendar
driver.find_element("xpath", '//*[@id="step-pick-appointment"]/div[2]/div[1]/div[3]/div[1]/div[1]/button').click() 
time.sleep(1)

appointments_exist = False

# Check current month's calendar for active appointments
if "activeCalendarDay" in driver.page_source:
    appointments_exist = True

# Navigate to next month's calendar and check for appts
driver.find_element("xpath", '//*[@id="step-pick-appointment"]/div[2]/div[4]/div[1]/table[1]/tbody/tr/th[3]/a').click()
time.sleep(1)

if "activeCalendarDay" in driver.page_source:
    appointments_exist = True

# Ring alert sound
if appointments_exist:
    print('appointments exist!!!!')
    chime.info()
    chime.success()
    time.sleep(0.7)
    chime.info()
    chime.success()
    time.sleep(0.7)
    chime.info()
    chime.success()
else:
    print('no appointments')
    # chime.info()
    # chime.success()

    

''' to set up cron job that runs every 5 min M-F while computer is awake,
run the following in your terminal with the correct file paths:

% crontab -e
% i
% */5 * * * 1-5 cd /Users/ariellewoods/scripts && /usr/local/bin/python3 BARC_surgery.py
esq 
% :wq

% crontab -r  # to remove it when no longer needed

Solution from:
https://www.jcchouinard.com/python-automation-with-cron-on-mac/
'''