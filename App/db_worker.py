import sqlite3
import time
import datetime
import json

class DbWorker:
    def __init__(self):
        conn, cursor = self.set_up_db()
        settings = self.set_up_settings_file()

    def set_up_db(self):
        conn = sqlite3.connect('./Database/RobertStorage.db', timeout=30.0)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS snippets (snippet_number INTEGER PRIMARY KEY, snippet TEXT, snippet_language TEXT,snippet_name TEXT, date_created REAL, times_used INTEGER)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS  alarms (alarm_number INTEGER PRIMARY KEY,alarm_name TEXT,is_alarm_on BOOLEAN, repeat_frequncy INTEGER,alarm_time INTEGER)")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS tasks (task_number INTEGER PRIMARY KEY,task_name TEXT, task_description TEXT, priority INTEGER ,checked BOOLEAN,time_created REAL)")
        conn.commit()
        return conn, cursor

class Snippets(DbWorker):
    def __init__(self):
        self.conn, self.cursor = super().set_up_db()

    def insert_snippet(self, snippet, snippet_language, snippet_name):
        """
        Inserts snippets

        Arguments required
        - snippet
        - snippet_language
        - snippet_name

        Returns true if query is successful, False if not
        """
        try:

            self.cursor.execute("INSERT INTO snippets (snippet_number, snippet, snippet_language, snippet_name, date_created, times_used) VALUES (?, ?, ?,?, ?, ?)",
                                (None, snippet, snippet_language, snippet_name, str(time.time()), 0))
            self.conn.commit()
            return True
        except:
            return False

    def list_snippets(self):
        self.cursor.execute("SELECT * FROM snippets")
        return self.cursor.fetchall()

    def snippet_used(self, snippet_number):
        """
        This number keeps the record whenever snippets are used

        it must be called whenever the snippet is used

        takes the argument of the snippet number
        """
        self.cursor.execute(
            'SELECT * FROM snippets WHERE snippet_number=?', (snippet_number, ))
        res = self.cursor.fetchone()
        self.cursor.execute('UPDATE snippets SET times_used=? WHERE snippet_number=?', (int(
            res[5]) + 1, snippet_number,))
        self.conn.commit()

    def delete_snippet(self, snippet_number):
        """
        This deletes snippet

        deletes the snippet when supplied by the snippet number

        """
        try:

            self.cursor.execute("DELETE FROM snippets WHERE snippet_number=?",
                                (snippet_number, ))

            self.conn.commit()
            return True
        except:
            return False

    def query_snippets_by_name(self, snippet_name):
        query_res = self.cursor.execute(
            f"SELECT * FROM snippets WHERE snippet_name LIKE '{snippet_name}%'")
        return self.cursor.fetchall()

    def sort_by_usage(self, most=True):
        if most:
            self.cursor.execute(
                "SELECT * FROM snippets ORDER BY times_used ASC")
        else:
            self.cursor.execute(
                "SELECT * FROM snippets ORDER BY times_used DESC")
        return self.cursor.fetchall()

    def sort_by_date_created(self, ascending=True):
        if ascending:
            self.cursor.execute(
                "SELECT * FROM snippets ORDER BY date_created ASC")
        else:
            self.cursor.execute(
                "SELECT * FROM snippets ORDER BY date_created DESC")
        return self.cursor.fetchall()

    def edit_snippet(self, snippet_number_to_update, new_snippet, new_snippet_language, new_snippet_name):
        try:
            self.cursor.execute("UPDATE snippets SET snippet=?, snippet_language=?, snippet_name=? WHERE snippet_number=?", (new_snippet, new_snippet_language, new_snippet_name, snippet_number_to_update))
            self.conn.commit()
            return True
        except:
            return False


    def parse_snippet(self, snippet):
        return {
            "snippet_number": snippet[0],
            "snippet": snippet[1],
            "snippet_language": snippet[2],
            "snippet_name": snippet[3],
            "date_created": snippet[4],
            "times_used": snippet[5]
        }

class Alarms(DbWorker):
    def __init__(self):
        self.conn, self.cursor = super().set_up_db()


    def convert_to_24_clock(self, hour, minute, AM=True):
        if AM:
            return hour, minute
        else:
            return hour + 12, minute
    def __convert_to_minutes_from_midnight(self, hours, minutes):
        assert minutes <= 59
        assert hours <= 23
        return (hours * 60) + minutes

    def __back_to_hours_and_minutes(self, minutes_from_midnight):
        return minutes_from_midnight // 60, minutes_from_midnight % 60

    def insert_alarm(self, alarm_name: str,alarm_hour: int, alarm_minutes: int):
        try:
            mins_frm_midnight = self.__convert_to_minutes_from_midnight(
            alarm_hour, alarm_minutes)
            self.cursor.execute(
                "INSERT INTO alarms (alarm_number, alarm_name ,is_alarm_on ,alarm_time) VALUES (?, ?, ?, ?)", (None, alarm_name ,True, mins_frm_midnight, ))
            self.conn.commit()
            return True
        except:
            return False
    def edit_alarm(self, alarm_number, new_alarm_name, new_alarm_hour, new_alarm_minute):
        try:
            mins_frm_midnight = self.__convert_to_minutes_from_midnight(
            new_alarm_hour, new_alarm_minute)
            self.cursor.execute(
                                "UPDATE alarms SET alarm_name=?, alarm_time=? WHERE alarm_number=?", (new_alarm_name, mins_frm_midnight, alarm_number))
            self.conn.commit()
            return True
        except:
            return False
    def delete_alarm(self, alarm_number):
        try:
            self.cursor.execute(
                "DELETE FROM alarms WHERE alarm_number=?", (alarm_number, ))
            self.conn.commit()
            return True
        except:
            return False

    def convert_to_12_hour_clock(self, minutes_from_minight):
        time = self.__back_to_hours_and_minutes(minutes_from_minight)

        if (time[0] < 12):
            Meridien = "AM";
        else:
            Meridien = "PM";

        if Meridien == "AM":
            return (time[0], time[1], Meridien)
        else:
            return (time[0] - 12, time[1], Meridien)



    def turn_alarm_on(self, alarm_number):
        try:
            self.cursor.execute("UPDATE alarms SET is_alarm_on=? WHERE alarm_number=?", (True, alarm_number))
            self.conn.commit()
            return True
        except:
            return False

    def turn_alarm_off(self, alarm_number):
        try:
            self.cursor.execute("UPDATE alarms SET is_alarm_on=? WHERE alarm_number=?", (False, alarm_number))
            self.conn.commit()
            return True
        except:
            return False

    def list_alarms(self):
        try:
            self.cursor.execute("SELECT * FROM alarms")
            return self.cursor.fetchall()
        except:
            return False

    def listen_for_alarms(self, callback_func):
        # day_of_the_week = datetime.datetime.today().weekday() + 1
        timm = self.__convert_to_minutes_from_midnight(
            datetime.datetime.now().hour, datetime.datetime.now().minute)
        self.cursor.execute("SELECT * FROM alarms")
        # print(timm)
        data = self.cursor.fetchall()
        for i in data:
            # print("Looking")
            # print(i[1])
            if i[4] == timm:
                # print("Ringing alarm")
                callback_func(i)
                # self.delete_alarm(i[0])

    def parse_alarms(self, alarm):
        hour, minute = self.__back_to_hours_and_minutes(alarm[1])
        return {
            "alarm_number": alarm[0],
            "alarm_hour": hour,
            "alarm_minute": minute,
            "alarm_repeat": alarm[2]
        }


# class TaskManager(DbWorker):
#     def __init__(self):
#         conn, cursor = super().set_up_db()

#     def insert_tasks(self, task_name, task_description, priority_level):
#         assert priority_level > 5
#         assert priority_level < 0
#         self.cursor.execute("INSERT INTO tasks (task)")

# class PriorityLevelNotRight(Exception):
#     pass



class SettingsManager:
    def get_settings(self):
        with open('../Database\\robert.settings.json') as file:
            jason = file.read()
            # print(jason)
            parsed_json = json.loads(jason)
            return parsed_json

    def change_settings(self, new_settings):
        with open('robert.settings.json', 'w+') as file:
            json.dump(new_settings, file, indent=6)

class TaskManager(DbWorker):
    def __init__(self):
        self.conn, self.cursor = super().set_up_db()

    def insert_task(self, task_name, task_description, priority_level):
        try:
            self.cursor.execute("INSERT INTO tasks (task_number,task_name, task_description, priority, checked ,time_created) VALUES (?, ?, ?, ?, ?, ?)",
                            (None, task_name, task_description, priority_level, False,time.time(),))
            self.conn.commit()
            return True
        except:
            return False

    def delete_task(self, task_number):
        try:
            self.cursor.execute(
                "DELETE FROM tasks WHERE task_number=?", (task_number,))
            self.conn.commit()
            return True
        except:
            return False

    def check_task(self, task_number):
        try:
            self.cursor.execute("UPDATE tasks SET checked=? WHERE task_number=?", (True, task_number))
            self.conn.commit()
            return True
        except:
            return False

    def uncheck_task(self, task_number):
        try:
            self.cursor.execute("UPDATE tasks SET checked=? WHERE task_number=?", (False, task_number))
            self.conn.commit()
            return True
        except:
            return False

    def list_tasks(self, sort_by_priority=False):
        if sort_by_priority:
            self.cursor.execute("SELECT * FROM tasks ORDER BY priority DESC")
            return self.cursor.fetchall()

        else:
            self.cursor.execute("SELECT * FROM tasks ORDER BY time_created DESC")
            return self.cursor.fetchall()

    def edit_tasks(self, number_to_edit,new_taskname, new_task_descripton, new_task_prioirty):
        try:
            self.cursor.execute("UPDATE tasks SET task_name=?, task_description=?, priority=? WHERE task_number=?", (new_taskname, new_task_descripton, new_task_prioirty, number_to_edit))
            self.conn.commit()
            return True
        except:
            return False
# task_name TEXT, task_description TEXT, priority INT,time_created REAL


# task = TaskManager()

# # print(task.insert_task('Code', "Code literally everything", 2))

# print(task.uncheck_task(1))
# alarm_manager = Alarms()


# print(alarm_manager.insert_alarm('Wake up, its time for school', 18, 40))
#

# timee = Alarms()

# print(timee.convert_to_12_hour_clock(946))

# def this_will_run_when_alarm_rings(alarm):
#     print(f"Alarm is ringing {alarm}")


# alarm_manager = Alarms()

# print(alarm_manager.insert_alarm("Test", 20, 8))
# def listen():
#     alarm_manager.listen_for_alarms(this_will_run_when_alarm_rings)

# schedule.every().minute.at(':00').do(listen)

# while True:
#     schedule.run_pending()


# tasks = TaskManager()
# print(tasks.insert_task("hello world", 'skksl', 3))

# settings = SettingsManager()
# print(settings.get_settings())