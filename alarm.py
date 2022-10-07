Alarm = 51
Day = 0
alarmHour = int(input("What hour is it?"))
alarmMinute = int(input("What minute is it?"))
amPm = str(input("pm or am?"))

if amPm == "pm":
  newHour = alarmHour + 12
  duration = newHour + Alarm
else:
  duration = alarmHour + Alarm
if duration >= 48:
  duration = duration - 24
  day = Day + 1
elif duration >=24:
  duration = duration - 24
  day = Day + 1

print("The alarm should go off at", newHour, ":", alarmMinute, "in", day, "day/s")
