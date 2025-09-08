# Created by JimBobJoe36
# NOTE This is a .pyw file, so it doesn't have a terminal. To terminate, terminate python processes in Task Manager.
from plyer import notification
from datetime import datetime
from time import sleep
# Functions
def schedule(Stunden, Minuten):
    ''' To change, update Stunden (hour) and Minuten (minute) with your schedule. You can change the sendNotification("CHANGE") to send a different notification.
    To add more, just duplicate an "elif" statement and change the values. It uses the 24 hour clock. It sleeps for one minute so it doesn't spam notifications
    '''
    if Stunden == "00" and Minuten == "00": #  0000 (Midnight)
        sendNotification("Period 1")
        sleep(60)
    elif Stunden == "02" and Minuten == "30": # 0230 AM
        sendNotification("Period 2")
        sleep(60)
    elif Stunden == "05" and Minuten == "00": # 0500 AM
        sendNotification("Period 3")
        sleep(60)
    elif Stunden == "07" and Minuten == "30": # 0730 AM
        sendNotification("Period 4")
        sleep(60)
    elif Stunden == "10" and Minuten == "00": # 1000 AM
        sendNotification("Period 5")
        sleep(60)

def sendNotification(period):
    ''' If this doesn't work, type in Powershell "pip install plyer". '''
    notification.notify(
        # The notification title
        title="Alarm 1",
        # The body of the notification
        message=f"Next destination: {period}",
        timeout=10
    )

while True:
    now = datetime.now()
    # Gives the hour alone
    hour = now.strftime("%H")
    # Gives the minute alone
    minute = now.strftime("%M")

    schedule(hour, minute)