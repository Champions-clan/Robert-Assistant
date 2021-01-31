import schedule
from App.db_worker import Alarms
from App.db_worker import convert_to_12_hour_clock
 # code required to get the alarm_listener working 
def this_will_run_when_alarm_rings(alarm):
    # alarm = Alarms()
    # print(alarm[4])
    time = convert_to_12_hour_clock(minutes_from_minight=alarm[4])
    from notifypy import Notify
    notification = Notify()
    notification.title = alarm[1]
    notification.message = f"The time is {time[0]}:{time[1]} {time[2]}"
    notification.icon = "./Assets/Robert Logo.png"
    notification.audio = "./Assets/beep.wav"
    notification.send()


alarm_manager = Alarms()

print(alarm_manager.insert_alarm("Test", 13, 54))
def listen():
    alarm_manager.listen_for_alarms(this_will_run_when_alarm_rings)

schedule.every().minute.at(':00').do(listen)

while True:
    schedule.run_pending()