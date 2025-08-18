import time
from plyer import notification
try:
 while True:
    notification.notify(
        title = "Please Drink Water",
        message = "Drinking water is good for your health",
    )
    time.sleep(5)
except KeyboardInterrupt:
    print("Program terminated by user")