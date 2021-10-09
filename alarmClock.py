from datetime import datetime
from playsound import playsound
import time
alarmTime = input("Enter the time of alarm in HH:MM:SS AM/PM \n")
alarmHour = alarmTime[:2]
alarmMinute = alarmTime[3:5]
alarmSecond = alarmTime[6:8]
alarmPeriod = alarmTime[9:11].upper()

time.sleep(2)
print("Setting up alarm...")
time.sleep(2)


while True:
    currentTime = datetime.now()
    currentHour = currentTime.strftime("%I")
    currentMinute = currentTime.strftime("%M")
    currentSecond = currentTime.strftime("%S")
    currentPeriod = currentTime.strftime("%p")

    if(alarmPeriod == currentPeriod) and \
        (alarmHour == currentHour) and \
            (alarmMinute == currentMinute) and \
                (alarmSecond == currentSecond):
        print("Wake up!")
        playsound('Jehovah.mp3')
        break


