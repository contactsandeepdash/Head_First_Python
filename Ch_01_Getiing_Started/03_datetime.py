import datetime
import time

today = datetime.date.today()
print ("today = " + str(today))
print("today day =  " + str(today.day))
print("today month = " + str(today.month))
print("today year = " + str(today.year))
print("iso today = " + str(datetime.date.isoformat(today)))

print("time in 12 hr format = " + str(time.strftime("%I:%M:%S %A %p")))
print("time in H:M = " + str(time.strftime("%H:%M")))
print("time in AM:PM = " + str(time.strftime("%A %p")))

