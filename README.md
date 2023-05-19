# Appointment-Alert-Web-Scraper

I created this project after becoming a foster for rescue dogs in Houston, to address frustrations with the city's system for processing dogs. This tool made the process easier! Currently on my 4th foster dog and counting.

The scripts navigate to Houston's animal shelter website and check the HTML for open appointments for foster dogs for the current and subsequent month, and chime an alert sound if there is an opening. A CronJob runs the script every 5 minutes when the computer is awake. For use in a desktop/browser environment. Works for two different appointment types, either intake (processing) or surgery (for spay/neuter). Functional as of May 2023.
